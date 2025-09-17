import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)


def show_members_with_borrowed_books():
    members_resp = sb.table("members").select("*").execute()
    members = members_resp.data
    print("\n=== Members and Borrowed Books ===")
    for m in members:
        print(f"\nMember ID: {m['member_id']} | Name: {m['name']} | Email: {m['email']} | Joined: {m['join_date']}")
        borrow_resp = sb.table("borrow_records").select("record_id, book_id, borrow_date, return_date").eq("member_id", m['member_id']).execute()
        borrow_records = borrow_resp.data
        if borrow_records:
            for br in borrow_records:
                if br['book_id'] is None:
                    print(f"  - ⚠️ Borrow record {br['record_id']} exists but has no linked book (book_id is NULL).")
                    continue

                book_resp = sb.table("books").select("title, author, category").eq("book_id", br['book_id']).execute()
                book = book_resp.data[0] if book_resp.data else None
                if book:
                    status = "Returned" if br['return_date'] else "Borrowed"
                    print(f"  - {book['title']} by {book['author']} | Category: {book['category']} | Status: {status} | Borrowed on: {br['borrow_date']}")
                else:
                    print(f"  - ⚠️ Book not found for book_id {br['book_id']}")
        else:
            print("  - No borrowed books.")



if __name__ == "__main__":
    show_members_with_borrowed_books()
