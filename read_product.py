# add_product.py
import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def list_product():
    resp=sb.table("productsdatabase").select("*").order("product_id",desc=False).execute()
    return resp.data
if __name__=="__main__":
    products=list_product()
    if products:
        print("Products:")
        for p in products:
            print(f"{p['product_id']}:{p['name']}:{p['sku']}:{p['price']}:{p['stock']}:")
    
