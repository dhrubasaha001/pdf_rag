from retriever import search_chunks
import ollama

def ask_question(question):

    # 1️⃣ Retrieve relevant chunks
    chunks = search_chunks(question)

    # 2️⃣ Combine chunks into context
    context = " ".join(chunks)

    # 3️⃣ Build prompt
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    # 4️⃣ Send to LLM
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    # 5️⃣ Extract answer
    answer = response["message"]["content"]

    return answer