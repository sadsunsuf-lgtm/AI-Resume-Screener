import streamlit as st
import os
import pandas as pd
import json
import time
from dotenv import load_dotenv
from google import genai
from parser import extract_text_from_pdf
from tenacity import retry, stop_after_attempt, wait_exponential

# 1. SETUP
st.set_page_config(page_title="TalentGuard AI: Pro Dashboard", layout="wide")
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# --- PRO RETRY LOGIC (Runs in the background silently) ---
@retry(wait=wait_exponential(multiplier=2, min=10, max=120), stop=stop_after_attempt(3))
def safe_ai_call(prompt):
    return client.models.generate_content(model="gemini-flash-latest", contents=prompt)

# 2. UI ELEMENTS (CLEAN VERSION)
with st.sidebar:
    st.header("📋 Recruitment Settings")
    target_role = st.text_input("Target Role", placeholder="e.g. AI Engineer")
    # Removed the "Retry Logic is active" text from here

st.title("🏆 AI Resume Leaderboard")
jd_input = st.text_area("Detailed Job Description", height=200)
uploaded_files = st.file_uploader("Upload Resumes (PDF)", type="pdf", accept_multiple_files=True)

# 3. ANALYSIS ENGINE
if st.button("🚀 Process & Rank Candidates"):
    if target_role and jd_input and uploaded_files:
        results_list = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, file in enumerate(uploaded_files):
            status_text.text(f"Processing: {file.name}")
            with open("temp.pdf", "wb") as f:
                f.write(file.getbuffer())
            
            try:
                text = extract_text_from_pdf("temp.pdf")
                prompt = f"Role: {target_role}\nJD: {jd_input}\nResume: {text}\nReturn ONLY JSON: {{\"Name\": \"Name\", \"Score\": 85, \"Top_Skill\": \"Skill\", \"Verdict\": \"Hire\"}}"
                
                time.sleep(2) # Keeps the API happy
                response = safe_ai_call(prompt)
                
                raw_json = response.text.replace("```json", "").replace("```", "").strip()
                data = json.loads(raw_json)
                data["Score"] = pd.to_numeric(data.get("Score", 0), errors='coerce')
                results_list.append(data)
                
            except Exception as e:
                st.warning(f"Skipped {file.name} due to processing limit.")
            finally:
                progress_bar.progress((i + 1) / len(uploaded_files))
                if os.path.exists("temp.pdf"):
                    os.remove("temp.pdf")

        # 4. RESULTS DISPLAY
        if results_list:
            status_text.success("✅ Analysis Complete!")
            df = pd.DataFrame(results_list).sort_values(by="Score", ascending=False)
            
            st.divider()
            st.subheader("📊 Candidate Ranking Table")
            
            def color_verdict(val):
                return 'color: green' if "Hire" in str(val) else 'color: red'

            st.dataframe(
                df.style.background_gradient(cmap="Greens", subset=["Score"])
                        .map(color_verdict, subset=["Verdict"]),
                width="stretch"
            )

            # 5. PROTECTED MEMO (NO ERROR TEXT)
            st.divider()
            st.subheader("📝 AI Executive Memo")
            try:
                with st.spinner("Finalizing recommendation..."):
                    memo_prompt = f"Write a professional hiring memo for: {df.head(3).to_dict()}"
                    memo_res = safe_ai_call(memo_prompt)
                    st.info(memo_res.text) # Shows ONLY if successful
            except Exception:
                pass # Silently skip if the API is too busy, keeps screen clean
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Export CSV", data=csv, file_name="rankings.csv")
    else:
        st.warning("Please fill all inputs.")