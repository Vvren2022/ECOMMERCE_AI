import json
import faiss
import numpy as np
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load products
with open("data/products.json", "r") as f:
    products = json.load(f)

# Prepare text for embeddings
texts = [
    f"Name: {p['name']}, Price: {p['price']}, Category: {p['category']}, "
    f"Description: {p['description']}, Rating: {p['rating']}"
    for p in products
]

# Generate embeddings
embeddings = []
for text in texts:
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    embeddings.append(resp.data[0].embedding)

embeddings = np.array(embeddings).astype("float32")

# Store in FAISS
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "products.index")

# Save metadata
with open("products_metadata.json", "w") as f:
    json.dump(products, f)

print("✅ FAISS index and metadata saved.")
