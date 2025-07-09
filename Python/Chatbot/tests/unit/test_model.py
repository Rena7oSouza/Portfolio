from app.model.chatbot_model import get_ai_response

def test_model_response_is_string():
    response = get_ai_response("Hello")
    assert isinstance(response, str)

def test_model_response_not_empty():
    response = get_ai_response("How are you?")
    assert len(response.strip()) > 0
