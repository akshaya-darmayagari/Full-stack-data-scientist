import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def search_books(keyword):
    resp = sb.table("books").select("*").or_(
        f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%"
    ).execute()
    return resp.data
def main():
        keyword = input("Enter keyword to search (title/author/category): ").strip()
        results = search_books(keyword)
        if results:
            print("\nMatching Books:")
            for b in results:
                print(f"{b['book_id']} | {b['title']} | {b['author']} | {b['category']} | Stock: {b['stock']}")
        else:
            print("No books found.")

if __name__ == "__main__":
    main()
