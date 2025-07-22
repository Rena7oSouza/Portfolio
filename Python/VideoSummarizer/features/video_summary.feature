Feature: Video summarization

  Scenario: Summarize YouTube video
    Given the video has been downloaded and transcribed
    When the user requests a summary of the entire video
    Then the system returns a summary of the entire video