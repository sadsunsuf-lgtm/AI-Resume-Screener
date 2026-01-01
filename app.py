import os
from dotenv import load_dotenv
from google import genai
from parser import extract_text_from_pdf  # Importing your parser

# 1. Setup
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. Define the Job Description (The "Goal")
job_description = """
We are looking for a Python Developer with experience in AI and Web Automation. 
The ideal candidate should know how to work with APIs, extract data from documents, 
and build tools that save time.
"""

# 3. Extract text from your test resume
resume_path = "test_resume.pdf"
resume_text = extract_text_from_pdf(resume_path)

# 4. Create a Professional Prompt
# This instruction is what makes you an "AI Engineer"
prompt = f"""
You are an expert HR Recruitment Agent.
Analyze the following resume against the Job Description provided.

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Provide the following in your response:
1. Match Score (0 to 100).
2. Missing Skills (What is missing from the resume based on the job?).
3. Strengths (Why should we hire this person?).
4. Verdict (Hire / No Hire).
"""

# 5. Get the AI Result
try:
    print(f"Reading {resume_path}...")
    response = client.models.generate_content(
        model="gemini-flash-latest", 
        contents=prompt
    )
    print("\n--- SCREENING REPORT ---")
    print(response.text)
    
except Exception as e:
    print(f"Error during screening: {e}")

# ... (Keep your imports and client setup the same) ...

# 4. Updated SaaS-Grade Prompt
prompt = f"""
You are a Senior Talent Acquisition Specialist and AI Compliance Auditor.
Analyze the following resume against the Job Description.

JOB DESCRIPTION:
{jd_input}

CANDIDATE RESUME:
{resume_text}

Provide the analysis in this EXACT format:

### 🎯 Overall Match Score: [0-100]%
**Reasoning:** [1 sentence]

---

### 🛡️ Bias & Compliance Audit
* **Bias Check:** [Flag any biased language in the JD or Resume regarding age, gender, or ethnicity. If none, state "Clear"]
* **Recommendation:** [How to make the hiring process fairer for this specific candidate]

---

### 📈 Predictive Analytics (Success Forecast)
* **Success Probability:** [High/Medium/Low]
* **Retention Risk:** [e.g., Likely to stay 2+ years / At risk of poaching]
* **Key Growth Factor:** [What is the #1 skill they will bring to the team?]

---

### 📝 Executive Summary
* **Strengths:** [Top 3 bullet points]
* **Gaps:** [Top 2 missing skills]
* **Final Verdict:** [Strong Hire / Hire / Consider / Reject]
"""

# ... (Keep the rest of the logic to display the result) ...    

