import numpy as np
import faiss


def create_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def search(query, model, index, chunks, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(query_vec, k)
    
    results = [chunks[i] for i in indices[0]]
    return results