# Semantic Search Engine (Mini RAG)

A simple semantic search system that retrieves relevant information from text using embeddings and vector similarity.

---

## Overview

This project demonstrates how to perform context-based search instead of keyword matching. It converts text into embeddings and retrieves the most relevant chunks based on similarity.

---

## How It Works

1. Input text document
2. Split into chunks
3. Generate embeddings
4. Store in vector database
5. Query to retrieve top results

---

## Tech Stack

* sentence-transformers/all-MiniLM-L6-v2
* FAISS
* Python

---

## Project Structure

```
semantic-search-engine/
├── main.py
├── embed.py
├── search.py
├── utils.py
├── data/
│   └── sample.txt
```

---


## Usage

```
python main.py
```

---

## Example

Query:

```
fraud evidence
```

Output:

```
- The CFO confirmed financial irregularities...
- Internal audit revealed missing funds...
```

---

## Features

* Context-based retrieval
* Fast similarity search
* Modular structure

---

## Future Improvements

* Add PDF support
* Add API endpoints
* Integrate LLM for answers
