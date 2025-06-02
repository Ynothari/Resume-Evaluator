MODEL_CONFIGS = {
    "gemini": {
        "temperature": 0.4,  # Controls randomness; higher = more creative, lower = more deterministic
        "top_p": 1,  # Nucleus sampling; lower values reduce randomness
        "top_k": 32,  # Limits token selection to top-K probable tokens
        "max_output_tokens": 2048,  # Maximum tokens the model can generate
        "presence_penalty": 0.0,  # Encourages/discourages introducing new topics (higher = more new topics)
        "frequency_penalty": 0.0,  # Reduces repetition (higher = less repetitive output)
    },
    "openai": {
        "temperature": 0.7,  
        "max_tokens": 1000,  
        "top_p": 1,  
        "presence_penalty": 0.0,  
        "frequency_penalty": 0.0,  
        "stop": None,  # List of stop sequences to halt generation early
    },
    "claude": {
        "temperature": 0.5,  
        "max_tokens": 1000,  
        "model": "claude-3-5-sonnet-20241022",  # Specifies Claude model version
        "stop_sequences": [],  # Custom text sequences where output should stop
    },
    "deepseek": {
        "temperature": 0.6,  
        "max_tokens": 1024,  
        "top_p": 1,  
        "top_k": 50,
        "model": "deepseek/deepseek-r1:free",  
    },
    "llama": {
        "temperature": 0.7,  
        "max_tokens": 512,  
        "top_p": 1,  
        "top_k": 50,  
        "model": "meta-llama/llama-3.2-3b-instruct:free"
    },
    "mistral": {
        "temperature": 0.6,  
        "max_tokens": 1024,  
        "top_p": 1,  
        "top_k": 50,  
        "model": "mistralai/mistral-7b-instruct:free"
    },
}