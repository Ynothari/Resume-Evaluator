# 📄 LLM-Powered Resume Evaluator

## 🚀 Overview

The **LLM-Powered Resume Evaluator** helps you analyze how well your resume matches a given job description using various **Large Language Models (LLMs)**.  
It delivers AI-driven feedback, lets you compare outputs from multiple models, and supports fine-tuning to improve resume-job alignment.

---

## ✨ Features

- ✅ **Resume Evaluation** – Intelligent feedback on resume-job alignment  
- 🔄 **Multi-LLM Support** – Compare outputs from **OpenAI (GPT), Gemini, Claude, LLaMA, DeepSeek, and Mistral**  
- ⚙️ **Configurable Parameters** – Adjust `temperature`, `max_tokens`, `top_p`, and `top_k` for output customization  
- 💻 **User-Friendly Interface** – Clean **Streamlit UI** for uploading resumes and entering job descriptions  

---

## ⚙️ Setup & Installation

### 📌 Prerequisites

- Python 3.8 or later  
- API keys for supported LLMs (see below)

---

### 🧱 1. Clone the Repository

```bash
git clone https://github.com/Anamay23/Resume-Evaluator.git
cd llm-resume-evaluator
```

---

### 🛡️ 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
# Activate environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔐 4. Configure API Keys

#### Step 1: Get API Keys

- **OpenAI (GPT):** https://platform.openai.com/docs/overview  
- **Gemini (Google):** https://ai.google.dev/  
- **Claude (Anthropic):** https://www.anthropic.com/  
- **DeepSeek, LLaMA, Mistral (via OpenRouter):** https://openrouter.ai/

#### Step 2: Create `.env` File

In your project root, create a `.env` file and paste your keys like:

```env
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
CLAUDE_API_KEY=your_claude_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> 📝 `OPENROUTER_API_KEY` works for **DeepSeek**, **LLaMA**, and **Mistral**.

---

### ▶️ 5. Run the App

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501)

---

## 🧠 Usage

1. Paste or upload the **job description**.  
2. Upload your **resume** (PDF or plain text).  
3. Select one or more **LLMs** for evaluation.  
4. View and compare **AI-generated feedback**.  
5. **Improve** your resume using insights provided.

---

## 🧩 Configuration

Adjust defaults in `config.py`:

- `temperature`: creativity vs precision  
- `max_tokens`: response length  
- `top_p`, `top_k`: output diversity controls  

---

## 🗺️ Roadmap & Future Plans

- 🚀 Compare LLM results in a **side-by-side UI table**  
- 🛠️ Let users change model parameters **within the UI**  
- 📧 Auto-generate a **job application email** from resume + JD  

---

## 🤝 Contributing

We welcome contributions!  
Feel free to **fork** this repo, improve it, and **submit a pull request**.

---

## 📬 Contact

For queries or suggestions, please contact the project owner via GitHub: [@Anamay23](https://github.com/Anamay23)
