from app.controller.chatbot_controller import handle_user_message

def test_controller_returns_string():
    response = handle_user_message("What's your name?")
    assert isinstance(response, str)

def test_controller_response_not_empty():
    response = handle_user_message("Say something")
    assert len(response.strip()) > 0
