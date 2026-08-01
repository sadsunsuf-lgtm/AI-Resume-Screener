# 🏆 TalentGuard: AI-Powered Resume Leaderboard

An intelligent recruitment tool that uses Large Language Models (LLMs) to automatically rank resumes against job descriptions with high precision.

## 🚀 Live Demo
https://ai-resume-screener-3bo3hybbryogebknycuje6.streamlit.app/

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
---
*Developed by [Sana Nasir](https://www.linkedin.com/in/sana-nasir-521937316/)*
