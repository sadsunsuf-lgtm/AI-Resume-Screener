# 🏆 TalentGuard: AI-Powered Resume Leaderboard

An intelligent recruitment tool that uses Large Language Models (LLMs) to automatically rank resumes against job descriptions with high precision.

## 🚀 Live Demo
[Link to your Streamlit App]

## ✨ Key Features
- **Batch Processing:** Upload multiple PDF resumes simultaneously.
- **AI Scoring:** Uses Google Gemini 1.5 Flash to provide a 0-100 match score.
- **Executive Memo:** Automatically generates a professional hiring summary for the top 3 candidates.
- **Robust Error Handling:** Built-in exponential backoff to handle API rate limits (Free Tier).
- **Data Export:** Download the final leaderboard as a CSV for HR systems.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Engine:** Google GenAI (Gemini)
- **Data Handling:** Pandas
- **Logic:** Python, Tenacity (Retry Logic)

## ⚙️ Installation & Setup
1. Clone the repo: `git clone https://github.com/sadsunsuf-lgtm/AI-Resume-Screener.git`
2. Install requirements: `pip install -r requirements.txt`
3. Create a `.env` file and add your `GOOGLE_API_KEY`.
4. Run the app: `streamlit run main.py`

---
*Developed by [Sana Nasir](https://www.linkedin.com/in/sana-nasir-521937316/)*