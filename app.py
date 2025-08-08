import streamlit as st
from search import search_products
import json

st.set_page_config(page_title="AI E-commerce Search", layout="wide")

st.title("🛍️ AI-Powered Product Catalog")
st.write("Search products using natural language queries like:")
st.code("running shoes under $100 with good reviews")

query = st.text_input("Enter your search query:")

if query:
    results = search_products(query)
    st.subheader("Search Results")
    for product in results:
        st.markdown(f"### {product['name']}")
        st.write(f"**Price:** ${product['price']}  |  **Category:** {product['category']}  |  **Rating:** {product['rating']} ⭐")
        st.write(product['description'])
        st.markdown("---")
else:
    # Show full catalog if no query
    with open("products_metadata.json", "r") as f:
        all_products = json.load(f)
    st.subheader("All Products")
    for product in all_products:
        st.markdown(f"### {product['name']}")
        st.write(f"**Price:** ${product['price']}  |  **Category:** {product['category']}  |  **Rating:** {product['rating']} ⭐")
        st.write(product['description'])
        st.markdown("---")
