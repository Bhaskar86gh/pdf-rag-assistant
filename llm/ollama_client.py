import ollama

def generate(query, context):

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the given context.

Context:
{context}

Question:
{query}
"""

    response = ollama.chat(
        model="qwen3:8b",   # 🔥 BEST for your setup
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]