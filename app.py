# RAG Knowledge Assistant - Arrowstack Foods
# Simple version - No internet needed

import os
import re

# 1. Load all policy files
documents = {}
for file in os.listdir("."):
    if file.endswith("_policy.txt"):
        with open(file, "r", encoding="utf-8") as f:
            documents[file] = f.read()

print("="*50)
print("Arrowstack Foods - Knowledge Assistant")
print("Loaded documents:", list(documents.keys()))
print("Type 'exit' to stop")
print("="*50)

# 2. Ask questions loop
while True:
    question = input("\nYour Question: ")
    if question.lower() == "exit":
        print("Thank you! Bye!")
        break

    # Find best matching sentences
    # Remove small words
    stop_words = ["what", "is", "the", "how", "many", "do", "i", "have", "can", "are", "a", "an", "my", "for", "in", "on"]
    keywords = [w for w in re.findall(r"\w+", question.lower()) if w not in stop_words]

    best_answer = None
    best_score = 0
    best_source = ""

    for file_name, text in documents.items():
        # Split into lines
        for line in text.split("\n"):
            score = 0
            line_lower = line.lower()
            for kw in keywords:
                if kw in line_lower:
                    score += 1
            if score > best_score:
                best_score = score
                best_answer = line.strip()
                best_source = file_name

    # 3. Show answer with citation - Safety: No hallucination
    if best_score == 0 or not best_answer:
        print("\nAssistant: Not found in policy documents. Please ask HR team.")
    else:
        print(f"\nAssistant: {best_answer}")
        print(f"Source: {best_source}")