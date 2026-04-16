from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
import glob
import shutil
import sys

# import your existing scripts
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts"))
from ingest import ingest_url
from compile import compile_source

import anthropic

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.join(BASE_DIR, "wiki")
RAW_DIR = os.path.join(BASE_DIR, "raw")
GRAPH_PATH = os.path.join(WIKI_DIR, "graph.json")
CATEGORIES = ["concepts", "codes", "networks", "processes", "gaps"]


def find_all_articles():
    """Find all .md articles in wiki/ and all subfolders"""
    articles_by_cat = {cat: [] for cat in CATEGORIES}
    
    # search wiki root and all subfolders
    for md_file in glob.glob(os.path.join(WIKI_DIR, "**", "*.md"), recursive=True):
        filename = os.path.basename(md_file)
        if filename in ["index.md", "log.md"]:
            continue
            
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # extract category from frontmatter
        category = "concepts"  # default
        title = filename.replace(".md", "").replace("-", " ").title()
        summary = ""
        
        for line in content.split("\n"):
            if line.startswith("category:"):
                cat = line.replace("category:", "").strip().lower()
                # handle singular/plural mismatch
                cat_map = {"concept": "concepts", "code": "codes", "network": "networks", "process": "processes", "gap": "gaps"}
                cat = cat_map.get(cat, cat)
                if cat in CATEGORIES:
                    category = cat
            if line.startswith("title:"):
                title = line.replace("title:", "").strip()
                
        # extract summary
        in_summary = False
        for line in content.split("\n"):
            if line.strip() == "## Summary":
                in_summary = True
                continue
            if in_summary and line.startswith("##"):
                break
            if in_summary and line.strip():
                summary = line.strip()
                break
        
        articles_by_cat[category].append({
            "id": filename.replace(".md", ""),
            "title": title,
            "summary": summary,
            "path": md_file
        })
    
    return articles_by_cat


# Route 1: serve the knowledge graph
@app.route("/api/graph", methods=["GET"])
def get_graph():
    if not os.path.exists(GRAPH_PATH):
        return jsonify({"nodes": [], "edges": []})
    with open(GRAPH_PATH, "r", encoding="utf-8") as f:
        graph = json.load(f)
    return jsonify(graph)


# Route 2: serve a wiki article by ID
@app.route("/api/wiki/<article_id>", methods=["GET"])
def get_article(article_id):
    # search everywhere in wiki/
    for md_file in glob.glob(os.path.join(WIKI_DIR, "**", f"{article_id}.md"), recursive=True):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        # get category from frontmatter
        category = "concepts"
        for line in content.split("\n"):
            if line.startswith("category:"):
                cat = line.replace("category:", "").strip().lower()
                if cat in CATEGORIES:
                    category = cat
                break
        return jsonify({
            "id": article_id,
            "category": category,
            "content": content
        })
    return jsonify({"error": "Article not found"}), 404


# Route 3: list all articles grouped by category
@app.route("/api/articles", methods=["GET"])
def list_articles():
    return jsonify(find_all_articles())


# Route 4: compile new wiki from URLs
@app.route("/api/compile", methods=["POST"])
def compile_wiki():
    data = request.get_json()
    urls = data.get("urls", [])

    if len(urls) > 10:
        return jsonify({"error": "For this POC, you can add up to 10 links for Ingest + Compile."}), 400
    if len(urls) == 0:
        return jsonify({"error": "Please add at least one URL."}), 400

    try:
        # Step 1: clear old data
        if os.path.exists(RAW_DIR):
            shutil.rmtree(RAW_DIR)
        os.makedirs(RAW_DIR)

        # clear wiki articles but keep the folder
        for item in glob.glob(os.path.join(WIKI_DIR, "**", "*.md"), recursive=True):
            if os.path.basename(item) not in ["index.md", "log.md"]:
                os.remove(item)
        for cat in CATEGORIES:
            cat_dir = os.path.join(WIKI_DIR, cat)
            if os.path.exists(cat_dir):
                shutil.rmtree(cat_dir)
            os.makedirs(cat_dir)
        # remove old graph
        if os.path.exists(GRAPH_PATH):
            os.remove(GRAPH_PATH)

        # Step 2: ingest each URL
        for url in urls:
            ingest_url(url)

        # Step 3: compile all raw sources
        client = anthropic.Anthropic()
        sources = glob.glob(os.path.join(RAW_DIR, "*.md"))
        for source in sources:
            compile_source(source, client)

        # count what was created
        articles = find_all_articles()
        total = sum(len(v) for v in articles.values())

        return jsonify({
            "status": "success",
            "message": f"Wiki compiled: {total} articles from {len(urls)} sources",
            "article_count": total,
            "source_count": len(urls)
        })

    except Exception as e:
        return jsonify({
            "error": "Claude ran into some issues. Please try again later.",
            "details": str(e)
        }), 500


# Route 5: ask the wiki
@app.route("/api/ask", methods=["POST"])
def ask_wiki():
    data = request.get_json()
    question = data.get("question", "")

    if not question.strip():
        return jsonify({"error": "Please enter a question."}), 400

    try:
        # gather all wiki content for context
        context_parts = []
        for md_file in glob.glob(os.path.join(WIKI_DIR, "**", "*.md"), recursive=True):
            filename = os.path.basename(md_file)
            if filename in ["index.md", "log.md"]:
                continue
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            context_parts.append(f"--- Article: {filename} ---\n{content}\n")

        if not context_parts:
            return jsonify({"answer": "No wiki articles found. Please compile some sources first."})

        wiki_context = "\n".join(context_parts)

        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system="""You are a payments knowledge assistant. Answer questions using ONLY 
the wiki articles provided below. Cite specific articles when possible using [[article-name]] format.
If the wiki doesn't contain enough information, say so clearly.
Keep answers concise and practical.""",
            messages=[{
                "role": "user",
                "content": f"Wiki knowledge base:\n{wiki_context}\n\nQuestion: {question}"
            }]
        )

        answer = response.content[0].text
        return jsonify({"answer": answer})

    except Exception as e:
        print("ASK ERROR:", e)
        import traceback
        traceback.print_exc()
        return jsonify({
            "error": "Claude ran into some issues. Please try again later.",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)