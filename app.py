import streamlit as st
import os
import re

st.set_page_config(page_title="Arrowstack Foods - Knowledge Assistant", page_icon="🍔")
st.title("🍔 Arrowstack Foods - Knowledge Assistant")
st.write("Company policy gurinchi emaina adugu!")

def load_documents():
    docs = {}
    for file in os.listdir("."):
        if file.endswith(".txt"):
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    docs[file] = f.read()
            except:
                pass
    return docs

docs = load_documents()
st.success(f"Loaded documents: {list(docs.keys())}")

question = st.text_input("Your Question:", placeholder="Ex: What is WFH policy?")

if st.button("Ask"):
    if not question:
        st.warning("Please oka question type cheyi!")
    else:
        q_words = set(re.findall(r"\w+", question.lower()))
        best_file = None
        best_score = 0
        best_text = ""
        for name, text in docs.items():
            text_lower = text.lower()
            score = sum(1 for w in q_words if len(w) > 2 and w in text_lower)
            if score > best_score:
                best_score = score
                best_file = name
                best_text = text
        if best_file and best_score > 0:
            st.subheader(f"Answer from: {best_file}")
            lines = best_text.split("\n")
            found = []
            for line in lines:
                line_lower = line.lower()
                if any(w in line_lower for w in q_words if len(w) > 2):
                    found.append(line)
            if found:
                for l in found[:10]:
                    st.write(f"- {l}")
            else:
                st.write(best_text[:2000])
        else:
            st.error("Sorry, ee question ki answer documents lo dorakaledu.")
