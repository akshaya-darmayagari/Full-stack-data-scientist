import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete_member(member_id):

    borrow_resp = sb.table("borrow_records").select("*").eq("member_id", member_id).is_("return_date", None).execute()
    
    if borrow_resp.data:
        print("Cannot delete member. They still have borrowed books.")
        return
    
    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    if resp.data:
        print(f"Member ID {member_id} deleted successfully.")
    else:
        print("Member not found.")


def delete_book(book_id):
    
    borrow_resp = sb.table("borrow_records").select("*").eq("book_id", book_id).is_("return_date", None).execute()
    
    if borrow_resp.data:
        print("Cannot delete book. It is currently borrowed.")
        return
    
    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    if resp.data:
        print(f" Book ID {book_id} deleted successfully.")
    else:
        print(" Book not found.")


if __name__ == "__main__":
    print("\n=== Delete Operations ===")
    print("1. Delete Member (if no borrowed books)")
    print("2. Delete Book (if not borrowed)")
    
    choice = input("Choose an option (1/2): ").strip()
    
    if choice == "1":
        mid = int(input("Enter Member ID to delete: "))
        delete_member(mid)
    
    elif choice == "2":
        bid = int(input("Enter Book ID to delete: "))
        delete_book(bid)
    
    else:
        print(" Invalid choice")
