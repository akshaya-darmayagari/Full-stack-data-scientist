import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

# 1. Top 5 most borrowed books
def top_borrowed_books():
    try:
        resp = sb.table("borrow_records").select("book_id").execute()
        if not resp.data:
            print("No borrow records found.")
            return

        borrow_count = {}
        for r in resp.data:
            book_id = r["book_id"]
            book_resp = sb.table("books").select("title,author").eq("book_id", book_id).execute()
            if book_resp.data:
                book = book_resp.data[0]
                key = (book["title"], book["author"])
                borrow_count[key] = borrow_count.get(key, 0) + 1

        if borrow_count:
            top5 = sorted(borrow_count.items(), key=lambda x: x[1], reverse=True)[:5]
            print("Top 5 Most Borrowed Books:")
            for (title, author), count in top5:
                print(f"{title} by {author} - Borrowed {count} times")
        else:
            print("No books have been borrowed yet.")

    except Exception as e:
        print("Error in top_borrowed_books:", e)

# 2. Members with overdue books (>14 days)
def overdue_members():
    try:
        resp = sb.table("borrow_records") \
                 .select("member_id, borrow_date") \
                 .is_("return_date", None) \
                 .execute()
        if not resp.data:
            print("No borrow records found.")
            return

        overdue_list = []
        for r in resp.data:
            borrow_date = datetime.fromisoformat(r["borrow_date"].replace("Z","+00:00"))
            if datetime.now(timezone.utc) - borrow_date > timedelta(days=14):
                member_id = r["member_id"]
                mem_resp = sb.table("members").select("name,email").eq("member_id", member_id).execute()
                if mem_resp.data:
                    member = mem_resp.data[0]
                    overdue_list.append((member["name"], member["email"], borrow_date.date()))

        if overdue_list:
            print("Members with Overdue Books (>14 days):")
            for name, email, date in overdue_list:
                print(f"{name} ({email}) borrowed on {date}")
        else:
            print("No members have overdue books.")

    except Exception as e:
        print("Error in overdue_members:", e)

# 3. Total books borrowed per member
def total_borrowed_per_member():
    try:
        resp = sb.table("borrow_records").select("member_id").execute()
        if not resp.data:
            print("No borrow records found.")
            return

        count_dict = {}
        for r in resp.data:
            member_id = r["member_id"]
            mem_resp = sb.table("members").select("name").eq("member_id", member_id).execute()
            if mem_resp.data:
                member = mem_resp.data[0]
                key = (member_id, member["name"])
                count_dict[key] = count_dict.get(key, 0) + 1

        if count_dict:
            print("Total Books Borrowed per Member:")
            for (mid, name), count in count_dict.items():
                print(f"{name} (ID: {mid}) - {count} books borrowed")
        else:
            print("No books have been borrowed by any member.")

    except Exception as e:
        print("Error in total_borrowed_per_member:", e)


def main():
    top_borrowed_books()
    print("\n")
    overdue_members()
    print("\n")
    total_borrowed_per_member()


if __name__ == "__main__":
    main()
