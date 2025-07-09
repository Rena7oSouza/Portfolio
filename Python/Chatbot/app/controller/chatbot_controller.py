from app.model.chatbot_model import get_ai_response

def handle_user_message(user_message: str) -> str:
    return get_ai_response(user_message)
