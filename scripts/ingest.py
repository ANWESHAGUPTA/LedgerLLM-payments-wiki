# ============================================================
# ingest.py — Ledger's first script
# 
# What this does:
#   Takes a URL, scrapes the webpage content, 
#   converts it to a clean markdown file,
#   and saves it in the raw/ folder.
#
# Think of it as: URL in → clean .md file out
# ============================================================

import requests                  # Library to fetch web pages (like a browser)
from bs4 import BeautifulSoup    # Library to parse HTML and extract text
import os                        # Library to work with file paths and folders
from datetime import date        # To stamp today's date on each file


def ingest_url(url):
    """
    Main function. Give it a URL, it will:
    1. Download the webpage
    2. Strip out the junk (nav bars, scripts, footers)
    3. Convert the useful content to markdown
    4. Save it as a .md file in raw/
    """

    # --- STEP 1: Fetch the webpage ---
    # This is like opening the URL in a browser, but in Python
    print(f"Fetching: {url}")
    response = requests.get(url)

    # Check if the page loaded successfully
    # Status 200 = success, anything else = problem
    if response.status_code != 200:
        print(f"Error: Could not fetch page (status {response.status_code})")
        return

    # --- STEP 2: Parse the HTML ---
    # BeautifulSoup takes the raw HTML and makes it searchable
    # Think of it as turning messy HTML into a structured tree
    soup = BeautifulSoup(response.text, 'html.parser')

    # Grab the page title (the text in the browser tab)
    title = soup.title.string if soup.title else "untitled"
    title = title.strip()    # Remove extra whitespace

    # --- STEP 3: Clean out the junk ---
    # Webpages have a lot of stuff we don't want:
    # scripts (JavaScript), styles (CSS), navigation bars, footers
    # decompose() completely removes these elements
    for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
        tag.decompose()

    # --- STEP 4: Extract the actual content ---
    # We only want the meaningful stuff: headings, paragraphs,
    # list items, and table cells
    content_parts = []

    # Loop through every heading, paragraph, list item, and table cell
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li', 'td', 'th', 'tr']):
        text = tag.get_text(strip=True)    # Get just the text, no HTML

        if text:    # Skip empty elements
            # Convert HTML headings to markdown headings
            # In markdown: # = h1, ## = h2, ### = h3, etc.
            if tag.name == 'h1':
                content_parts.append(f"# {text}")
            elif tag.name == 'h2':
                content_parts.append(f"## {text}")
            elif tag.name == 'h3':
                content_parts.append(f"### {text}")
            elif tag.name == 'h4':
                content_parts.append(f"#### {text}")
            # Convert HTML list items to markdown list items
            elif tag.name == 'li':
                content_parts.append(f"- {text}")
            # Everything else (paragraphs, table cells) — just keep the text
            else:
                content_parts.append(text)

    # Join all the parts with blank lines between them
    # This makes the markdown readable
    content = "\n\n".join(content_parts)

    # --- STEP 5: Create the filename ---
    # Turn the URL into a clean filename
    # e.g. "https://docs.stripe.com/declines/codes" → "codes.md"
    filename = url.split("/")[-1] or url.split("/")[-2]
    filename = filename.replace(".html", "").replace(".htm", "")
    filename = f"{filename}.md"

    # --- STEP 6: Build the frontmatter ---
    # Frontmatter is metadata at the top of the file
    # It tells us WHERE this came from, WHEN we grabbed it,
    # and WHAT category it belongs to
    # The --- lines are standard markdown frontmatter format
    frontmatter = f"""---
source: {url}
title: {title}
type: reference
domain: payments
ingested: {date.today()}
tags: []
---

# {title}

"""

    # --- STEP 7: Save the file ---
    # Navigate from scripts/ up to the project root, then into raw/
    raw_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'raw')
    filepath = os.path.join(raw_path, filename)

    # Write the frontmatter + content to the file
    # encoding='utf-8' handles special characters properly
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

    # Tell the user what happened
    print(f"Saved: {filepath}")
    print(f"Content length: {len(content)} characters")


# ============================================================
# This part runs when you execute the script
# It asks you for a URL, then calls the function above
# ============================================================
if __name__ == "__main__":
    url = input("Paste a URL to ingest: ")
    ingest_url(url)