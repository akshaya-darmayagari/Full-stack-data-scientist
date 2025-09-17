import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def return_book(member_id: int, book_id: int):
    try:
        rec_resp = sb.table("borrow_records").select("record_id") \
            .eq("member_id", member_id).eq("book_id", book_id).is_("return_date", None).execute()
        if not rec_resp.data:
            return "No active borrow record found"

        record_id = rec_resp.data[0]["record_id"]
        return_iso = datetime.now(timezone.utc).isoformat()
        sb.table("borrow_records").update({"return_date": return_iso}).eq("record_id", record_id).execute()

        book_resp = sb.table("books").select("stock,title").eq("book_id", book_id).execute()
        old_stock = book_resp.data[0]["stock"]
        sb.table("books").update({"stock": old_stock + 1}).eq("book_id", book_id).execute()

        return f"{book_resp.data[0]['title']} returned by member {member_id}"

    except Exception as e:
        try:
            sb.table("borrow_records").update({"return_date": None}).eq("record_id", record_id).execute()
        except Exception:
            pass
        return f"Transaction failed, rolled back. Error: {e}"


def main():
    mid = int(input("Enter Member ID: ").strip())
    bid = int(input("Enter Book ID: ").strip())
    print(return_book(mid, bid))


if __name__ == "__main__":
    main()
