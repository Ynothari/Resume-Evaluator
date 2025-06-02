import os
import google.generativeai as genai
from openai import OpenAI
import anthropic
from tenacity import retry, stop_after_attempt, wait_exponential
from utils.error_handlers import handle_error, handle_rate_limit_errors

# Configure APIs
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#anthropic.api_key = os.getenv("CLAUDE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Anthropic client
anthropic_client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

# Initialize OpenRouter client
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,  # Use the OpenRouter API key here
)

@handle_error
@handle_rate_limit_errors()
def generate_response_from_gemini(prompt, **kwargs):
    model = genai.GenerativeModel("gemini-1.5-flash")
    generation_config = {
        "temperature": kwargs.get("temperature", 0.4),
        "top_p": kwargs.get("top_p", 1),
        "top_k": kwargs.get("top_k", 32),
        "max_output_tokens": kwargs.get("max_output_tokens", 4096),
    }
    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
@handle_error
def generate_response_from_openai(prompt, **kwargs):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        **kwargs
    )
    return response.choices[0].message.content

@handle_error
@handle_rate_limit_errors()
def generate_response_from_claude(prompt, **kwargs):
    # Ensure required arguments are present
    api_args = {
        "model": kwargs.get("model", "claude-3-5-sonnet-20241022"),  # Default model
        "max_tokens": kwargs.get("max_tokens", 1024),  # Default max tokens
        "messages": [
            {"role": "user", "content": prompt}  # Format the prompt
        ],
        **kwargs  # Include any additional arguments
    }

    # Call the Claude API
    response = anthropic_client.messages.create(**api_args)
    return response.content

@handle_error
@handle_rate_limit_errors()
def generate_response_from_openrouter(prompt, model, **kwargs):
    try:
        response = openrouter_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        if response and response.choices:
            return response.choices[0].message.content
        else:
            print("API returned no response or choices.")
            return None
    except Exception as e:
        print(f"OpenRouter API Error: {e}")
        return None