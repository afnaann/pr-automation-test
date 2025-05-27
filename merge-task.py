
import os
from datetime import date
from notion_client import Client



NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID  = os.environ["NOTION_DATABASE_ID"]

notion = Client(auth=NOTION_TOKEN)

print(NOTION_TOKEN)
def add_release(version, notes, repo, tested_android, status):
    new_page = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Version": {
                "title": [{ "text": { "content": version }}]
            },
            "Notes": {
                "rich_text": [{ "text": { "content": notes }}]
            },
            "Date": {
                "date": { "start": date.today().isoformat() }
            },
            "Repo": {
                # now rich_text, not select
                "rich_text": [{ "text": { "content": repo }}]
            },
            "Tested in Android?": {
                "checkbox": tested_android
            },
            "Status": {
                # use Notion's built-in status type
                "status": { "name": status }
            }
        }
    }
    notion.pages.create(**new_page)
    print(f"Added {version} to Notion DB")

if __name__ == "__main__":
    
    import sys
    
    _, version, notes, repo, tested, status = sys.argv
    add_release(version, notes, repo, tested.lower() == "true", status)
