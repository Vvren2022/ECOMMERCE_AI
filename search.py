import faiss
import numpy as np
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load FAISS index and metadata
index = faiss.read_index("products.index")
with open("products_metadata.json", "r") as f:
    products_metadata = json.load(f)

def search_products(user_query, top_k=5):
    # Embed query
    q_embed = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_query
    ).data[0].embedding

    q_embed = np.array(q_embed).astype("float32").reshape(1, -1)

    # Search in FAISS
    distances, indices = index.search(q_embed, top_k)
    retrieved = [products_metadata[i] for i in indices[0]]

    # Refine with GPT
    prompt = f"""
    You are a helpful product recommendation assistant.
    User Query: {user_query}
    Retrieved Products: {retrieved}

    From the retrieved products, select only those that match the user's intent.
    Return the results as a JSON list with fields: name, price, category, rating, description.
    """
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    try:
        refined_products = json.loads(resp.choices[0].message.content)
    except:
        refined_products = retrieved  # fallback

    return refined_products
