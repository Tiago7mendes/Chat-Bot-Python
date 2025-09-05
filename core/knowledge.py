import os

def load_knowledge(path="data/knowledge.txt"):
    knowledge = {}
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    knowledge[key.lower()] = value.strip()
    return knowledge

def search_knowledge(query, knowledge_base):
    query = query.lower()
    for key in knowledge_base:
        if key in query:
            return knowledge_base[key]
    return "I don't know about that yet."
