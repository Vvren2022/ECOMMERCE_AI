PROJECT SETUP
ecommerce_ai/
│
├── data/
│   └── products.json           # ✅ Include sample products
├── embeddings.py               # ✅ Script to build embeddings
├── search.py                   # ✅ Search + GPT refinement
├── app.py                      # ✅ Streamlit UI
├── requirements.txt            # ✅ Dependencies
├── README.md                   # ✅ Project documentation
└── .gitignore                  # ✅ Ignore sensitive files

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features
📦 Static product catalog (JSON-based)

🔍 Natural language search powered by OpenAI embeddings + GPT refinement

⚡ FAISS vector database for fast retrieval

🖥️ Minimal Streamlit UI

Tech Stack
Python 3.11

Streamlit (UI)

OpenAI API (embeddings + GPT)

FAISS (vector search)

dotenv (env management)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clone the repo
git clone https://github.com/yourusername/ecommerce_ai.git
cd ecommerce_ai

# Create a venv (with uv)
uv venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

# Install requirements
uv pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your OpenAI API key

# Build product embeddings
python embeddings.py

# Run the app
streamlit run app.py
