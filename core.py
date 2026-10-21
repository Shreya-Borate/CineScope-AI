from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model = 'gemini-3.8-flash')

prompt = ChatPromptTemplate.from_messages(
    [
    (
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful, structured information from a movie paragraph and present it in a clean, readable format.

Rules:
- Do NOT add explanations.
- Do NOT add extra commentary.
- Follow the exact format specified below.
- If information is missing, write NULL.
- Keep the summary short (2–3 lines maximum).
- Do NOT guess unknown facts.

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:

Short Summary:
"""
    ),
    (
        "human",
        """
Extract information from this paragraph:

{paragraph}
"""
    )
]

)

para = input("Give your paragraph : ")

final_prompt = prompt.invoke(
    {"paragraph" : para}
)

response = model.invoke(final_prompt)
print(response.content[0]["text"])