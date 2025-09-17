import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def update_book_stock(book_id, additional_copies):
    current_resp = sb.table("books").select("stock").eq("book_id", book_id).execute()
    if not current_resp.data:
        print(" Book not found")
        return
    
    current_stock = current_resp.data[0]['stock']
    new_stock = current_stock + additional_copies
    
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    print(f" Updated stock: Book ID {book_id} now has {new_stock} copies.")


def update_member_email(member_id, new_email):
    resp = sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    if resp.data:
        print(f" Member ID {member_id} email updated to {new_email}")
    else:
        print(" Member not found")


if _name_ == "_main_":
    print("\n=== Update Operations ===")
    print("1. Update Book Stock")
    print("2. Update Member Email")
    
    choice = input("Choose an option (1/2): ").strip()
    
    if choice == "1":
        bid = int(input("Enter Book ID: "))
        copies = int(input("Enter number of new copies purchased: "))
        update_book_stock(bid, copies)
    
    elif choice == "2":
        mid = int(input("Enter Member ID: "))
        email = input("Enter new email: ").strip()
        update_member_email(mid, email)
    
    else:
        print(" Invalid choice")