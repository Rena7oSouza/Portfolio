from behave import given, when, then
from app.controller.chatbot_controller import handle_user_message

@given('the user says "{message}"')
def step_given_user_says(context, message):
    context.message = message

@when('the chatbot processes the message')
def step_when_chatbot_processes(context):
    context.response = handle_user_message(context.message)

@then('the chatbot should respond with text')
def step_then_check_response(context):
    assert isinstance(context.response, str)
    assert len(context.response.strip()) > 0
