from behave import given, when, then
from controller.video_controller import VideoController

@given('the video has been downloaded and transcribed')
def step_impl(context):
    context.controller = VideoController()
    context.url = "https://youtube.com/test"

    # Mocking download and transcription for BDD
    context.controller.model.download_video = lambda url: "test.mp4"
    context.controller.model.transcribe_video = lambda x: "BDD test text"

@when('the user requests a summary of the entire video')
def step_impl(context):
    # Mocking summarization for BDD
    context.controller.model.summarize_text = lambda x: "BDD summary of entire video."
    context.result = context.controller.process_video(context.url)

@then('the system returns a summary of the entire video')
def step_impl(context):
    assert context.result == "BDD summary of entire video."
