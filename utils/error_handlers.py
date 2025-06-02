"""from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests
import openai
import anthropic
import google.api_core.exceptions
from streamlit import error as st_error

# Retry decorator for rate limits and transient errors
def handle_rate_limit_errors():
    return retry(
        stop=stop_after_attempt(3),  # Retry up to 3 times
        wait=wait_exponential(multiplier=1, min=4, max=10),  # Exponential backoff
        retry=retry_if_exception_type((
            openai.error.RateLimitError,
            anthropic.RateLimitError,
            google.api_core.exceptions.ResourceExhausted,
            requests.exceptions.ConnectionError,
        )),
    )

# Function to handle API-specific errors
def handle_api_error(e):
    if isinstance(e, openai.error.APIError):
        st_error("OpenAI API Error: Please check your API key and quota.")
    elif isinstance(e, anthropic.APIError):
        st_error("Claude API Error: Please check your API key and quota.")
    elif isinstance(e, google.api_core.exceptions.GoogleAPIError):
        st_error("Gemini API Error: Please check your API key and quota.")
    elif isinstance(e, requests.exceptions.RequestException):
        st_error("Network Error: Please check your internet connection.")
    else:
        st_error(f"An unexpected error occurred: {str(e)}")

# Generic error handler
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            handle_api_error(e)
            raise  # Re-raise the exception after handling
    return wrapper"""

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests
import openai
import anthropic
import google.api_core.exceptions
from streamlit import error as st_error

# Retry decorator for rate limits and transient errors
def handle_rate_limit_errors():
    return retry(
        stop=stop_after_attempt(3),  # Retry up to 3 times
        wait=wait_exponential(multiplier=1, min=4, max=10),  # Exponential backoff
        retry=retry_if_exception_type((
            openai.RateLimitError,  # Updated for OpenAI v1.0+
            anthropic.RateLimitError,
            google.api_core.exceptions.ResourceExhausted,
            requests.exceptions.ConnectionError,
        )),
    )

# Function to handle API-specific errors
def handle_api_error(e):
    if isinstance(e, openai.APIError):  # Updated for OpenAI v1.0+
        st_error("OpenAI API Error: Please check your API key and quota.")
    elif isinstance(e, anthropic.APIError):
        st_error("Claude API Error: Please check your API key and quota.")
    elif isinstance(e, google.api_core.exceptions.GoogleAPIError):
        st_error("Gemini API Error: Please check your API key and quota.")
    elif isinstance(e, requests.exceptions.RequestException):
        st_error("Network Error: Please check your internet connection.")
    else:
        st_error(f"An unexpected error occurred: {str(e)}")

# Generic error handler
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            handle_api_error(e)
            raise  # Re-raise the exception after handling
    return wrapper