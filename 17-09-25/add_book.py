import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def add_book(title, author, category, stock):
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data
 
if __name__ == "__main__":
    name = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    category= (input("Enter category: ").strip())
    stock = int(input("Enter stock: ").strip())
 
    created = add_book(name, author, category, stock)
    print("Book Inserted:", created)