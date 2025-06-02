# LLM-Powered Resume Evaluator

## Overview
The **LLM-Powered Resume Evaluator** is a tool that allows users to evaluate their resume against a given job description using different **Large Language Models (LLMs)**.  
It provides feedback on how well the resume matches the job description and enables users to view results from multiple models, helping them optimize their resume for better job prospects and analyze how different LLMs generate outputs for the same task.

## Features
✅ **Resume Evaluation** – Get feedback on how well your resume aligns with a job description.  
✅ **Multi-LLM Support** – View evaluation results from **OpenAI (GPT), Gemini, Claude, LLaMA, DeepSeek, and Mistral**.  
✅ **Configurable Parameters** – Adjust model settings like `temperature`, `max_tokens`, `top-p`, and `top-k` for fine-tuned responses (in the code).  
✅ **User-Friendly Interface** – A **Streamlit-based UI** for easy input of resumes and job descriptions.  

---

## Setup & Installation

### Prerequisites  
Ensure you have **Python 3.8+** installed

### 1. Clone the Repository  
```bash
git clone https://github.com/Anamay23/Resume-Evaluator.git
cd llm-resume-evaluator
```

### 2. Create a Virtual Environment (Optional but Recommended)  
```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate  
# On Windows
venv\Scripts\activate  
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys and set up .env file 
To use this tool, you need API keys for different LLMs. Here’s how you can generate them and set them up:

🔑 Generate API Keys for OpenAI GPT, Gemini, and Claude
  Visit the API platform for each model:
    OpenAI (https://platform.openai.com/docs/overview)
    Google AI Studio (Gemini) (https://ai.google.dev/)
    Anthropic (Claude) (https://www.anthropic.com/)
  Sign in or create an account
  Navigate to the API Keys section and generate a new key
  Copy and save the key securely

🔑 Generate API Key for DeepSeek, LLaMA, and Mistral (via OpenRouter)
  Go to OpenRouter and log in/sign up (https://openrouter.ai/)
  Generate an API key from the API Keys section
  This single key works for DeepSeek, LLaMA, and Mistral
  
📝 Add Keys to the .env File
In your project directory, create a .env file (if it doesn’t exist) and add the keys like this:
```ini
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
CLAUDE_API_KEY=your_claude_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here  # Used for DeepSeek, LLaMA, and Mistral
```


### 5. Run the Application  
```bash
streamlit run app.py
```

---

## Usage
1. **Enter the job description** for which you want feedback.  
2. **Upload your resume**.  
3. **Select the LLMs** you want to use for evaluation.  
4. **View feedback** from different LLMs.  
5. **Optimize your resume** according to the generated feedback.

---

## Configuration  
Modify `config.py` to update default LLM settings:  

- **`temperature`** – Controls randomness in responses (higher = more creative, lower = more deterministic).  
- **`max_tokens`** – Sets the maximum response length.  
- **`top_p` / `top_k`** – Sampling methods for response diversity.  

---

## Roadmap & Future Enhancements  
🚀 **Add a feature** to compare results of different LLMs in a **table on the UI**.  
🚀 **Allow users** to modify **model parameters** (like `temperature` and `max_tokens`) directly from the UI.  
🚀 **Add a feature** that generates an **email to send to the recruitment team** based on your resume and job description.  

---

## Contributing  
Feel free to **fork the repo** and submit a **pull request**! Any contributions to improve the tool are welcome.  
