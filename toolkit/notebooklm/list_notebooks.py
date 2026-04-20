
import sys
import os
import json
sys.path.append(r'd:\Python311\Lib\site-packages')
from notebooklm_mcp.api_client import NotebookLMClient
from notebooklm_mcp.auth import load_cached_tokens

cached = load_cached_tokens()
if not cached:
    print("ERROR: No cached tokens found.")
    sys.exit(1)

client = NotebookLMClient(
    cookies=cached.cookies,
    csrf_token=cached.csrf_token,
    session_id=cached.session_id
)

try:
    notebooks = client.list_notebooks()
    print("---NOTEBOOKS_START---")
    for nb in notebooks:
        print(f"ID: {nb.id} | TITLE: {nb.title}")
    print("---NOTEBOOKS_END---")
except Exception as e:
    print(f"FAILED: {e}")
