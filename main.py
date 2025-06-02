import streamlit as st
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from utils.file_handlers import extract_text_from_pdf, extract_text_from_docx
from utils.api_handlers import generate_response_from_gemini, generate_response_from_openai, generate_response_from_claude, generate_response_from_openrouter
from utils.prompts import RESUME_EVALUATION_PROMPT
from utils.config import MODEL_CONFIGS
from utils.response_parsers import parse_response, format_output

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Set the background color for the entire app */
        body { 
            background-color: #000000; /* Black background */
        }

        /* Style the main container */
        .stApp { 
            background: #000000; /* Black background */
            padding: 20px; 
            border-radius: 12px; 
        }

        /* Ensure all headings and text are white */
        h1, h2, h3, h4, h5, h6, p, div, span, .stMarkdown, .stText { 
            color: #FFFFFF !important; /* White text */
        }

        /* Center align headings */
        h1, h2, h3 { 
            text-align: center;
            font-weight: bold;
        }

        /* Style input fields */
        .stTextInput, .stTextArea { 
            background-color: rgba(255, 255, 255, 0.1) !important; /* Semi-transparent white */
            color: #FFFFFF !important; /* White text */
            border: 1px solid #4CAF50 !important; /* Green border */
            border-radius: 8px;
            padding: 10px;
        }

        /* Style buttons */
        .stButton>button { 
            background-color: #4CAF50 !important; /* Green background */
            color: white !important; /* White text */
            border-radius: 6px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }

        /* Style containers for better visibility */
        .stContainer {
            background-color: rgba(255, 255, 255, 0.1); /* Semi-transparent white */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        /* Improve readability for lists and other elements */
        ul, ol, li {
            color: #FFFFFF !important; /* White text */
        }

        /* Ensure tables are visible */
        .stTable {
            background-color: rgba(255, 255, 255, 0.1) !important; /* Semi-transparent white */
            color: #FFFFFF !important; /* White text */
        }

        /* Style links */
        a {
            color: #4CAF50 !important; /* Green links */
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Streamlit app layout
st.title("📄 Resume Feedback: Job Match Evaluation")

# Section 1: Job Description Upload
st.header("📌 Job Description")
job_description = st.text_area("Paste the Job Description", height=200)

# Section 2: Resume Upload
st.header("📂 Upload Resume")
uploaded_file = st.file_uploader("Upload Your Resume (PDF or DOCX)", type=["pdf", "docx"], help="Accepted formats: PDF, DOCX")

# Section 3: LLM Selection & Tuning
st.header("🤖 LLM Selection & Tuning")
llm_option = st.selectbox("Choose an LLM for evaluation:", ["Gemini", "OpenAI GPT", "Claude", "DeepSeek", "Llama", "Mistral"])

# Section 4: Processing & Output
if st.button("🔍 Evaluate Resume"):
    if uploaded_file is not None:
        with st.spinner("Processing your resume...⏳"):
            # Extract text from the uploaded file
            if uploaded_file.type == "application/pdf":
                resume_text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                resume_text = extract_text_from_docx(uploaded_file)
            
            # Format the prompt
            formatted_prompt = RESUME_EVALUATION_PROMPT.format(text=resume_text, job_description=job_description)

            # Call the selected LLM
            model_mapping = {
                "Gemini": (generate_response_from_gemini, "gemini"),
                "OpenAI GPT": (generate_response_from_openai, "openai"),
                "Claude": (generate_response_from_claude, "claude"),
                "DeepSeek": (generate_response_from_openrouter, "deepseek"),
                "Llama": (generate_response_from_openrouter, "llama"),
                "Mistral": (generate_response_from_openrouter, "mistral"),
            }

            model_func, model_key = model_mapping[llm_option]
            response = model_func(formatted_prompt, **MODEL_CONFIGS[model_key])
            response_dict = parse_response(response)

            st.success("✅ Evaluation Complete!")
            st.subheader("📊 ATS Evaluation Result")
            format_output(response_dict)
    else:
        st.error("⚠️ Please upload a resume file.")
