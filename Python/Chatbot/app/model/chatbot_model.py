from transformers import pipeline, set_seed

# Load GPT-2 model locally
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")
set_seed(42)

def get_ai_response(user_input: str) -> str:
    result = chatbot(user_input, max_new_tokens=50, num_return_sequences=1)
    return result[0]['generated_text']
