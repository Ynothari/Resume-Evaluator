import json
import re
from streamlit import warning as st_warning
import streamlit as st
import json
import re

def parse_response(response_text):
    """
    Parse the raw response from the LLM into a structured format.
    Handles both JSON and non-JSON responses.
    """
    try:
        # Attempt to parse the response as JSON
        response_dict = json.loads(response_text.strip())
        return response_dict
    except json.JSONDecodeError:
        # If parsing fails, try to extract key-value pairs from the raw response
        response_dict = {
            "Job Description Match": "N/A",
            "Missing Keywords": "N/A",
            "Suggested Improvements": "N/A",  # Default to the raw response
            "Relevant Experience": "N/A",
        }

        # Try to extract key-value pairs using regex
        match = re.search(r'"Job Description Match":\s*"(\d+%)"', response_text)
        if match:
            response_dict["Job Description Match"] = match.group(1)

        match = re.search(r'"Missing Keywords":\s*"([^"]+)"', response_text)
        if match:
            response_dict["Missing Keywords"] = match.group(1)

        match = re.search(r'"Suggested Improvements":\s*"([^"]+)"', response_text)
        if match:
            response_dict["Suggested Improvements"] = match.group(1)

        match = re.search(r'"Relevant Experience":\s*"([^"]+)"', response_text)
        if match:
            response_dict["Relevant Experience"] = match.group(1)

        return response_dict


def format_output(response_dict):
    """
    Format the parsed response for display in Streamlit.
    Uses Streamlit components for a structured and readable UI.
    """
    
    # Job Match Percentage
    job_match = response_dict.get("Job Description Match", "N/A")
    if job_match != "N/A":
        st.metric(label="🔍 Job Description Match", value=job_match)
        #st.markdown(label="🔍 Job Description Match", value=job_match)

    # Missing Keywords
    missing_keywords = response_dict.get("Missing Keywords", "N/A")
    if missing_keywords and missing_keywords != "N/A":
        st.warning(f"⚠️ **Missing Keywords:** {missing_keywords}")

    # Relevant Experience
    relevant_experience = response_dict.get("Relevant Experience", "N/A")
    if relevant_experience and relevant_experience != "N/A":
        st.markdown("### ✅ Relevant Experience")
        st.info(relevant_experience)

    # Suggested Improvements
    suggested_improvements = response_dict.get("Suggested Improvements", "N/A")
    if suggested_improvements and suggested_improvements != "N/A":
        st.markdown("### 🔧 Suggested Improvements")
        suggestions_list = suggested_improvements.split(". ")  # Split into bullet points
        st.markdown("\n".join([f"- {s}" for s in suggestions_list if s]))  # Display as list