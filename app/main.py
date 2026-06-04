import streamlit as st

from app.config import INDEX_CHUNKS_JSONL, MATRIX_NPZ, TOP_K, VECTORIZER_PKL
from app.generator import ask
from app.prompts import MIN_SCORE
from app.retriever import Retriever

DEMO_QUESTIONS = [
    "how to make chicken soup?",
    "what ingredients do I need for pasta?",
    "how to bake chocolate cake?",
    "how to make pizza dough?",
]

def index_exists() -> bool:
    return all(p.exists() for p in (VECTORIZER_PKL, MATRIX_NPZ, INDEX_CHUNKS_JSONL))


@st.cache_resource
def load_retriever() -> Retriever:
    return Retriever()


def render_chunk(i: int, src: dict, expanded: bool = True) -> None:
    label = f"[{i}] doc_id={src['doc_id']} · score={src['score']:.4f}"
    with st.expander(label, expanded=expanded):
        st.markdown(f"**{src['name']}**")
        st.text(src["text"])


def main() -> None:
    st.set_page_config(page_title="Recipe RAG", layout="wide")
    st.title("🍳 Recipe RAG")
    st.caption("RAG system for recipes: TF-IDF retrieval + demo answer with sources")

    if not index_exists():
        st.error("Index not built. Run: `uv run python scripts/build_index.py`")
        st.stop()

    st.sidebar.header("Demo questions")
    for q in DEMO_QUESTIONS:
        if st.sidebar.button(q, use_container_width=True):
            st.session_state["question"] = q

    question = st.text_input("Your question", key="question")

    if st.button("Ask", type="primary"):
        if not question.strip():
            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("Searching..."):
            result = ask(question.strip(), k=TOP_K, retriever=load_retriever())

        st.subheader("Found fragments (top-k)")
        for i, src in enumerate(result["sources"], 1):
            render_chunk(i, src, expanded=src["score"] >= MIN_SCORE)

        st.subheader("Answer")
        st.text(result["answer"])


if __name__ == "__main__":
    main()
