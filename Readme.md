
# 🎬 CineScope-AI | Movie Information Extractor

An AI-powered movie information extraction application built using **Python, LangChain, Google Gemini, and Streamlit**. It transforms unstructured movie descriptions into structured, readable information using a Large Language Model (LLM).

## 📌 Project Overview

CineScope-AI extracts important movie details from a paragraph and organizes them into a clean, consistent format. Users can enter a movie description and receive structured information without manually searching through lengthy text.

## ✨ Features

- 🎥 Extract movie title, release year, genre, and director
- 🎭 Identify main cast members
- 📍 Extract setting, location, and plot
- 💡 Identify major movie themes
- ⭐ Extract available ratings and notable features
- 📝 Generate a concise movie summary
- 🤖 Integrate Google Gemini using LangChain
- 🖥️ Interactive web interface built with Streamlit

## 🛠️ Tech Stack

- **Language:** Python
- **LLM Framework:** LangChain
- **LLM:** Google Gemini
- **Frontend:** Streamlit
- **Environment Management:** uv
- **Configuration:** python-dotenv

## ⚙️ How It Works

1. **User Input:** Enter a paragraph describing a movie.
2. **Prompt Engineering:** LangChain's `ChatPromptTemplate` formats the instructions and input.
3. **LLM Processing:** Google Gemini analyzes the paragraph.
4. **Information Extraction:** The model extracts relevant movie details.
5. **Output Display:** Streamlit displays the results in a readable format.

## 📂 Project Structure

```text
CineScope-AI/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> **Note:** The `.env` file stores your API key locally and must not be uploaded to GitHub.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/CineScope-AI.git
cd CineScope-AI
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
uv venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 5. Run the Application

```bash
uv run streamlit run app.py
```

The application will open in your browser.

## 🧪 Example

**Input:**

> Inception is a 2010 science fiction thriller directed by Christopher Nolan. It stars Leonardo DiCaprio as Dom Cobb, a thief who enters people's dreams to steal secrets. He is offered a chance to reunite with his children if he can plant an idea in someone's mind. The movie explores dreams, memory, guilt, and reality.

**Extracted Information:**

- **Movie Title:** Inception
- **Release Year:** 2010
- **Genre:** Science fiction thriller
- **Director:** Christopher Nolan
- **Main Cast:** Leonardo DiCaprio
- **Themes:** Dreams, memory, guilt, reality

The application also extracts the plot, setting, ratings, notable features, and a short summary when information is available.

## 🎯 Learning Outcomes

- Understanding Large Language Model integration
- Creating prompts using LangChain
- Extracting structured information from natural language
- Integrating Google Gemini API
- Managing API keys using environment variables
- Building interactive AI applications with Streamlit

## 🔮 Future Enhancements

- Integrate a movie database API for verified details
- Support multiple movie descriptions
- Add downloadable CSV and JSON results
- Implement structured output validation
- Add movie title-based search functionality

## 🔐 Security

- Store API keys in environment variables.
- Add `.env` and `.venv/` to `.gitignore`.
- Never commit API keys or other secrets to GitHub.

## 👩‍💻 Author

**Shreya Borate**

Interested in Data Science, Machine Learning, NLP, Generative AI, and LLM-based applications.

---

⭐ If you find this project useful, consider giving the repository a star!
