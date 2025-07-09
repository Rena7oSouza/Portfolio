Feature: AI Chatbot basic responses

  Scenario: Responds to greeting
    Given the user says "Hello"
    When the chatbot processes the message
    Then the chatbot should respond with text

  Scenario: Responds to question
    Given the user says "What is your favorite color?"
    When the chatbot processes the message
    Then the chatbot should respond with text

  Scenario: Responds to random statement
    Given the user says "Tell me something interesting"
    When the chatbot processes the message
    Then the chatbot should respond with text
