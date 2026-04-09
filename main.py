from utils import chunk_text
from embed import get_embeddings, model
from search import create_index, search

with open("D:\\semantic-search\\data\\raw\\text.txt", "r") as f:
    text = f.read()

chunks = chunk_text(text)
embeddings = get_embeddings(chunks)
index = create_index(embeddings)

query = input("Enter your query: ")

results = search(query, model, index, chunks)

print("\nTop Results:\n")
for r in results:
    print("-", r, "\n")