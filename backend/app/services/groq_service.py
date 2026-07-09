import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)


def ask_llm(prompt: str):
    response = llm.invoke(prompt)
    return response.content


def summarize_interaction(notes: str):
    prompt = f"""
You are an AI CRM assistant for pharmaceutical companies.

Below are doctor's meeting notes.

Notes:
{notes}

Generate:

Summary:
(2-3 lines)

Next Action:
(1 line)
"""

    response = llm.invoke(prompt)

    return response.content
