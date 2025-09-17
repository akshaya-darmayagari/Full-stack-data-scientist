import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def list_books():
    resp = sb.table("books").select("*").execute()
    return resp.data

books = list_books()
for b in books:
    print(f"{b['book_id']} | {b['title']} | {b['author']} | {b['category']} | Stock: {b['stock']}")
