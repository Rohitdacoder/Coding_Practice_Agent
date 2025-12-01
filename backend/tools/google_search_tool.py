"""
Simple wrapper that returns a Google search URL for an editorial or explanation.
(We don't call Google programmatically to avoid needing API keys.)
Consumers can open the link in browser to view editorial pages.

If you want programmatic scraping of editorial pages, implement fetch + parse for each platform.
"""

from urllib.parse import quote_plus

def fetch_editorial(title: str):
    query = quote_plus(f"{title} editorial explanation")
    return f"https://www.google.com/search?q={query}"
