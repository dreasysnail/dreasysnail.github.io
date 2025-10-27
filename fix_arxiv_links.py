#!/usr/bin/env python3
"""
Script to verify and fix arxiv links in publication markdown files.
"""

import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import time
import json

def extract_arxiv_id(url):
    """Extract arxiv ID from URL."""
    match = re.search(r'arxiv\.org/abs/(\d+\.\d+)', url)
    return match.group(1) if match else None

def get_arxiv_title_authors(arxiv_id):
    """Fetch title and authors from arxiv."""
    try:
        url = f"https://arxiv.org/abs/{arxiv_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title_elem = soup.find('h1', class_='title')
        if title_elem:
            title = title_elem.get_text().replace('Title:', '').strip()
        else:
            return None, None

        # Extract authors
        authors_elem = soup.find('div', class_='authors')
        authors = []
        if authors_elem:
            for author in authors_elem.find_all('a'):
                authors.append(author.get_text().strip())

        return title, authors
    except Exception as e:
        print(f"Error fetching {arxiv_id}: {e}")
        return None, None

def search_arxiv_by_title(title):
    """Search arxiv for a paper by title."""
    try:
        # Use arxiv API
        import urllib.parse
        query = urllib.parse.quote(title)
        url = f"http://export.arxiv.org/api/query?search_query=ti:{query}&max_results=5"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse XML response
        from xml.etree import ElementTree as ET
        root = ET.fromstring(response.content)

        # Namespace handling
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        entries = root.findall('atom:entry', ns)
        if entries:
            # Get the first (most relevant) result
            first_entry = entries[0]
            arxiv_url = first_entry.find('atom:id', ns).text
            arxiv_id = extract_arxiv_id(arxiv_url)
            entry_title = first_entry.find('atom:title', ns).text.strip().replace('\n', ' ')

            return arxiv_id, entry_title

        return None, None
    except Exception as e:
        print(f"Error searching arxiv: {e}")
        return None, None

def parse_publication_file(filepath):
    """Parse publication markdown file and extract metadata."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract front matter
    match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None

    front_matter = match.group(1)

    # Extract fields
    title_match = re.search(r'title:\s*["\']?(.*?)["\']?$', front_matter, re.MULTILINE)
    paperurl_match = re.search(r'paperurl:\s*["\']?(.*?)["\']?$', front_matter, re.MULTILINE)

    title = title_match.group(1) if title_match else None
    paperurl = paperurl_match.group(1) if paperurl_match else None

    # Check if paperurl contains arxiv
    if paperurl and 'arxiv.org' in paperurl:
        arxiv_id = extract_arxiv_id(paperurl)
        return {
            'filepath': filepath,
            'title': title,
            'paperurl': paperurl,
            'arxiv_id': arxiv_id,
            'content': content
        }

    return None

def fix_arxiv_link(pub_info):
    """Verify and fix arxiv link if incorrect."""
    arxiv_id = pub_info['arxiv_id']
    expected_title = pub_info['title']
    filepath = pub_info['filepath']

    print(f"\nChecking: {filepath.name}")
    print(f"  Expected title: {expected_title}")
    print(f"  Current arxiv ID: {arxiv_id}")

    # Get actual paper info from arxiv
    actual_title, actual_authors = get_arxiv_title_authors(arxiv_id)

    if actual_title is None:
        print(f"  ⚠️  Could not fetch arxiv data")
        return False

    print(f"  Actual title: {actual_title}")

    # Compare titles (case-insensitive, ignoring some punctuation)
    expected_clean = re.sub(r'[:\-\.,]', '', expected_title.lower()).strip()
    actual_clean = re.sub(r'[:\-\.,]', '', actual_title.lower()).strip()

    if expected_clean in actual_clean or actual_clean in expected_clean:
        print(f"  ✓ Link is correct")
        return False

    # Title mismatch - search for correct arxiv ID
    print(f"  ✗ Title mismatch! Searching for correct paper...")
    correct_id, found_title = search_arxiv_by_title(expected_title)

    if correct_id and correct_id != arxiv_id:
        print(f"  → Found correct ID: {correct_id}")
        print(f"  → Found title: {found_title}")

        # Update the file
        old_url = pub_info['paperurl']
        new_url = f"https://arxiv.org/abs/{correct_id}"

        content = pub_info['content']

        # Replace all occurrences of the old URL
        updated_content = content.replace(old_url, new_url)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"  ✓ Updated {old_url} → {new_url}")
        return True
    else:
        print(f"  ⚠️  Could not find correct arxiv ID")
        return False

def main():
    pub_dir = Path('/Users/yizhezhang/Documents/projects/dreasysnail.github.io/_publications')

    # Find all publication files with arxiv links
    publications = []
    for md_file in sorted(pub_dir.glob('*.md')):
        pub_info = parse_publication_file(md_file)
        if pub_info:
            publications.append(pub_info)

    print(f"Found {len(publications)} publications with arxiv links")

    # Check and fix each one
    fixed_count = 0
    for pub_info in publications:
        try:
            if fix_arxiv_link(pub_info):
                fixed_count += 1
            time.sleep(1)  # Be nice to arxiv servers
        except Exception as e:
            print(f"Error processing {pub_info['filepath'].name}: {e}")

    print(f"\n{'='*60}")
    print(f"Summary: Fixed {fixed_count} out of {len(publications)} publications")

if __name__ == '__main__':
    main()
