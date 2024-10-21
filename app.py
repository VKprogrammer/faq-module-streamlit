%%writefile app.py
import streamlit as st
import json
from sentence_transformers import SentenceTransformer, util


with open("faqs.json", "r") as f:
    faqs = json.load(f)


faq_texts = []
faq_list = []  
for category, faq_items in faqs.items():
    for faq in faq_items:
        faq_texts.append(faq["question"])
        faq_list.append(faq)


model = SentenceTransformer('all-MiniLM-L6-v2')
faq_embeddings = model.encode(faq_texts, convert_to_tensor=True)

def search_faqs(query, top_k=1):
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.cos_sim(query_embedding, faq_embeddings)[0]
    top_indices = similarities.topk(top_k).indices.tolist()
    return [faq_list[i] for i in top_indices]

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Saras Info Hub", layout="centered")
local_css("styles.css")  # Load the external CSS file

st.markdown(
    "<div class='header-box'><h1>Saras AI Institute Information Hub</h1></div>",
    unsafe_allow_html=True,
)

st.markdown("<div class='container'>", unsafe_allow_html=True)
query = st.text_input("", placeholder="Ask your question here...", key="query_input")
button = st.button("Search")
st.markdown("</div>", unsafe_allow_html=True)

if button and query:
    results = search_faqs(query)
    if results:
        for result in results:
            st.markdown(
                f"<div class='results'><p><strong>Answer:</strong> {result['answer']}</p></div>",
                unsafe_allow_html=True
            )
    else:
        st.markdown("<p class='no-results'>No matching information found.</p>", unsafe_allow_html=True)
