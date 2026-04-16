# ============================================================
# compile.py — The brain of Ledger
#
# What this does:
#   1. Reads CLAUDE.md (your schema/rules)
#   2. Reads a raw source file
#   3. Reads the current index (if it exists)
#   4. Sends all of this to Claude API
#   5. Claude writes wiki articles following your rules
#   6. Saves the articles to the right wiki/ subfolders
#   7. Updates index.md, graph.json, and log.md
#
# Think of it as: raw source + rules → wiki articles
# ============================================================

import anthropic              # Claude API library
import os                     # File and folder operations
import json                   # For reading/writing graph.json
from datetime import date     # For timestamps in the log


# ============================================================
# SETUP — find all the important file paths
# ============================================================

# Get the project root directory (one level up from scripts/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# All the key paths
RAW_DIR = os.path.join(PROJECT_ROOT, 'raw')
WIKI_DIR = os.path.join(PROJECT_ROOT, 'wiki')
SCHEMA_PATH = os.path.join(PROJECT_ROOT, 'CLAUDE.md')
INDEX_PATH = os.path.join(WIKI_DIR, 'index.md')
GRAPH_PATH = os.path.join(WIKI_DIR, 'graph.json')
LOG_PATH = os.path.join(WIKI_DIR, 'log.md')

# Wiki subfolders
WIKI_FOLDERS = {
    'concept': os.path.join(WIKI_DIR, 'concepts'),
    'code': os.path.join(WIKI_DIR, 'codes'),
    'network': os.path.join(WIKI_DIR, 'networks'),
    'process': os.path.join(WIKI_DIR, 'processes'),
    'gap': os.path.join(WIKI_DIR, 'gaps'),
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def read_file(filepath):
    """Read a file and return its contents as a string.
    Returns empty string if the file doesn't exist yet."""
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


def write_file(filepath, content):
    """Write content to a file, creating directories if needed."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Saved: {filepath}")


def append_to_file(filepath, content):
    """Append content to the end of a file."""
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(content)


def list_raw_sources():
    """List all .md files in the raw/ directory."""
    sources = []
    for filename in os.listdir(RAW_DIR):
        if filename.endswith('.md'):
            sources.append(filename)
    return sorted(sources)


def list_existing_articles():
    """Scan all wiki subfolders and return a list of existing articles."""
    articles = []
    for category, folder in WIKI_FOLDERS.items():
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                if filename.endswith('.md'):
                    articles.append(f"wiki/{category}s/{filename}")
    return articles


# ============================================================
# THE MAIN COMPILE FUNCTION
# ============================================================

def compile_source(source_filename, client):
    """
    Takes one raw source file and compiles it into wiki articles.
    
    This is where Claude does the heavy lifting:
    - Reads the schema (CLAUDE.md) to know the rules
    - Reads the raw source to know the content
    - Reads the current index to know what already exists
    - Writes new articles or updates to existing ones
    """
    
    print(f"\n{'='*60}")
    print(f"Compiling: {source_filename}")
    print(f"{'='*60}")
    
    # --- STEP 1: Read all the inputs ---
    
    # The schema — tells Claude HOW to write articles
    schema = read_file(SCHEMA_PATH)
    if not schema:
        print("ERROR: CLAUDE.md not found! Cannot compile without schema.")
        return
    
    # The raw source — the actual content to compile
    source_path = os.path.join(RAW_DIR, source_filename)
    source_content = read_file(source_path)
    if not source_content:
        print(f"ERROR: {source_filename} not found or empty!")
        return
    
    # The current index — what articles already exist
    current_index = read_file(INDEX_PATH)
    if not current_index:
        current_index = "# Ledger Wiki Index\n\n(No articles yet — this is the first compile.)"
    
    # The current graph — existing nodes and edges
    current_graph = read_file(GRAPH_PATH)
    if not current_graph:
        current_graph = '{"nodes": [], "edges": []}'
    
    # List of existing articles for context
    existing = list_existing_articles()
    existing_str = "\n".join(existing) if existing else "(No articles yet)"
    
    # --- STEP 2: Build the prompt ---
    # This is the most important part of the whole project.
    # The system prompt gives Claude the schema rules.
    # The user prompt gives Claude the specific task.
    
    system_prompt = f"""You are Ledger, a payments knowledge base compiler.

Your job is to read a raw source document and compile it into
structured wiki articles following the schema rules below.

SCHEMA RULES:
{schema}

EXISTING WIKI ARTICLES:
{existing_str}

CURRENT INDEX:
{current_index}

CURRENT GRAPH:
{current_graph}
"""

    user_prompt = f"""Compile this raw source into wiki articles.

SOURCE FILE: {source_filename}
SOURCE CONTENT:
{source_content}

INSTRUCTIONS:
1. Read the source carefully
2. Identify every payment concept, code, and process mentioned
3. For each one, decide: full article, update existing, or gap stub
4. Apply ALL domain rules from the schema (synonyms, cross-linking, 
   recency, incomplete info handling)
5. Search for cross-network comparisons where applicable

RESPOND WITH EXACTLY THIS JSON STRUCTURE (no other text):
{{
  "articles": [
    {{
      "filename": "the-article-name.md",
      "category": "CATEGORIZE STRICTLY: code = any specific error code, status code, response code, or identifier with a fixed value. process = any workflow, procedure, strategy, or step-by-step guide describing HOW to do something. network = anything specific to a platform, provider, vendor, or external system. concept = general knowledge, definitions, overviews, or explanations of WHAT something is. gap = referenced in other articles but not enough info to write a full article. SPREAD articles across categories. If a source describes steps to follow, those articles MUST be process. If a source lists specific codes or identifiers, those MUST be code.",
      "content": "the full markdown content of the article"
    }}
  ],
  "index_update": "the new complete index.md content",
  "graph_update": {{
    "nodes": [
      {{"id": "article-id", "title": "Article Title", "category": "concept", "network": "all", "status": "complete"}}
    ],
    "edges": [
      {{"source": "article-id-1", "target": "article-id-2", "type": "related"}}
    ]
  }},
  "log_entry": "the log entry for this compile operation (follow log format from schema)"
}}
"""

    # --- STEP 3: Call Claude API ---
    print("  Sending to Claude API... (this may take 30-60 seconds)")
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=16000,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
    except Exception as e:
        print(f"  ERROR calling Claude API: {e}")
        return
    
    # --- STEP 4: Parse Claude's response ---
    raw_response = response.content[0].text
    
    # Claude sometimes wraps JSON in ```json ... ``` markers
    # Strip those out if present
    cleaned = raw_response.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    if cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()
    
    try:
        result = json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"  ERROR: Claude's response wasn't valid JSON.")
        print(f"  Parse error: {e}")
        # Save the raw response so we can debug
        debug_path = os.path.join(PROJECT_ROOT, 'debug_response.txt')
        write_file(debug_path, raw_response)
        print(f"  Raw response saved to debug_response.txt for inspection.")
        return
    
    # --- STEP 5: Save the articles ---
    articles = result.get("articles", [])
    print(f"\n  Claude generated {len(articles)} articles:")
    
    for article in articles:
        filename = article.get("filename", "unknown.md")
        category = article.get("category", "concept")
        content = article.get("content", "")
        
        # Figure out which folder this article goes in
        folder = WIKI_FOLDERS.get(category, WIKI_FOLDERS['concept'])
        filepath = os.path.join(folder, filename)
        
        write_file(filepath, content)
    
    # --- STEP 6: Update the index ---
    index_content = result.get("index_update", "")
    if index_content:
        write_file(INDEX_PATH, index_content)
    
    # --- STEP 7: Update the graph ---
    graph_update = result.get("graph_update", {})
    if graph_update:
        # Load existing graph
        try:
            existing_graph = json.loads(current_graph)
        except:
            existing_graph = {"nodes": [], "edges": []}
        
        # Merge new nodes (avoid duplicates by id)
        existing_node_ids = {n["id"] for n in existing_graph["nodes"]}
        for node in graph_update.get("nodes", []):
            if node["id"] not in existing_node_ids:
                existing_graph["nodes"].append(node)
                existing_node_ids.add(node["id"])
        
        # Merge new edges (avoid exact duplicates)
        existing_edge_set = {
            (e["source"], e["target"], e["type"]) 
            for e in existing_graph["edges"]
        }
        for edge in graph_update.get("edges", []):
            edge_tuple = (edge["source"], edge["target"], edge["type"])
            if edge_tuple not in existing_edge_set:
                existing_graph["edges"].append(edge)
                existing_edge_set.add(edge_tuple)
        
        # Save merged graph
        write_file(GRAPH_PATH, json.dumps(existing_graph, indent=2))
    
    # --- STEP 8: Update the log ---
    log_entry = result.get("log_entry", "")
    if log_entry:
        # Add a separator and timestamp
        log_content = f"\n\n{log_entry}\n"
        append_to_file(LOG_PATH, log_content)
        print(f"  Log updated.")
    
    print(f"\n  Done compiling {source_filename}!")


# ============================================================
# MAIN — run the compiler
# ============================================================

if __name__ == "__main__":
    # Initialize the Claude API client
    # It reads ANTHROPIC_API_KEY from your environment automatically
    client = anthropic.Anthropic()
    
    # Show available sources
    sources = list_raw_sources()
    print("=== Ledger Compile Script ===\n")
    print(f"Found {len(sources)} raw sources:\n")
    for i, source in enumerate(sources, 1):
        print(f"  {i}. {source}")
    
    print(f"\nOptions:")
    print(f"  - Type a number (1-{len(sources)}) to compile one source")
    print(f"  - Type 'all' to compile everything")
    print(f"  - Type 'quit' to exit\n")
    
    while True:
        choice = input("Your choice: ").strip().lower()
        
        if choice == 'quit':
            print("Bye!")
            break
        elif choice == 'all':
            print(f"\nCompiling all {len(sources)} sources...\n")
            for source in sources:
                compile_source(source, client)
            print(f"\n{'='*60}")
            print(f"ALL DONE! Check your wiki/ folder.")
            print(f"{'='*60}")
            break
        else:
            try:
                num = int(choice)
                if 1 <= num <= len(sources):
                    compile_source(sources[num - 1], client)
                else:
                    print(f"Pick a number between 1 and {len(sources)}")
            except ValueError:
                print("Type a number, 'all', or 'quit'")