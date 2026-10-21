import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Extract structured information from any movie paragraph using AI.")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Extract movie information from the provided paragraph.

STRICT RULES:
- Follow the exact output format below.
- Put every field on a separate line.
- Keep each field clearly separated.
- Use bullet points for Main Cast, Themes, and Notable Features.
- Never combine multiple fields on the same line.
- Use the provided information only. Do not invent facts.
- If information is missing, write "Not available".
- Keep the plot concise (2–3 sentences).
- Keep the short summary within 2–3 sentences.
- Do not add introductory or concluding remarks.

OUTPUT FORMAT:

## 🎬 Movie Information

**Movie Title:** 
**Release Year:** 
**Genre:** 
**Director:** 

**Main Cast:**
- Actor 1
- Actor 2
- Actor 3

**Setting / Location:** 

**Plot:**
Write a brief description of the movie's main storyline.

**Themes:**
- Theme 1
- Theme 2
- Theme 3

**Ratings:** 

**Notable Features:**
- Feature 1
- Feature 2
- Feature 3

---

### 📝 Short Summary
Write a concise 2–3 sentence summary of the movie.
"""
    ),
    (
        "human",
        """
Extract information from this paragraph:

{paragraph}
"""
    )
])

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)

paragraph = st.text_area(
    "Enter Movie Paragraph",
    placeholder="Paste a paragraph describing a movie here...",
    height=200
)

if st.button("Extract Movie Information", type="primary"):

    if paragraph.strip():

        try:
            with st.spinner("Extracting movie information..."):

                final_prompt = prompt.invoke({
                    "paragraph": paragraph
                })

                response = model.invoke(final_prompt)

                result = response.content

                if isinstance(result, list):
                    result = "\n".join(
                        block["text"]
                        for block in result
                        if block.get("type") == "text"
                    )

            st.subheader("Extracted Movie Information")
            st.markdown(result)

        except Exception as e:
            st.error(f"Something went wrong: {e}")

    else:
        st.warning("Please enter a movie paragraph first.")

