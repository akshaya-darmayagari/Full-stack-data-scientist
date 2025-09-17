import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def borrow_book(member_id: int, book_id: int):
    try:
        book_resp = sb.table("books").select("stock,title").eq("book_id", book_id).execute()
        if not book_resp.data:
            return "Book not found"
        book = book_resp.data[0]
        if book["stock"] <= 0:
            return "Book is out of stock"

        mem_resp = sb.table("members").select("member_id,name").eq("member_id", member_id).execute()
        if not mem_resp.data:
            return "Member not found"

        dup_resp = sb.table("borrow_records").select("record_id") \
            .eq("member_id", member_id).eq("book_id", book_id).is_("return_date", None).execute()
        if dup_resp.data:
            return "Member already has this book borrowed"

        old_stock = book["stock"]
        new_stock = old_stock - 1
        sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()

        borrow_payload = {
            "member_id": member_id,
            "book_id": book_id,
            "borrow_date": datetime.now(timezone.utc).isoformat()
        }
        insert_resp = sb.table("borrow_records").insert(borrow_payload).execute()
        if not insert_resp.data:
            sb.table("books").update({"stock": old_stock}).eq("book_id", book_id).execute()
            return "Failed to create borrow record, stock rolled back"

        return f"{book['title']} borrowed by member {member_id}"

    except Exception as e:
        try:
            sb.table("books").update({"stock": old_stock}).eq("book_id", book_id).execute()
        except Exception:
            pass
        return f"Transaction failed, rolled back. Error: {e}"


def main():
    mid = int(input("Enter Member ID: ").strip())
    bid = int(input("Enter Book ID: ").strip())
    print(borrow_book(mid, bid))


if __name__ == "__main__":
    main()
