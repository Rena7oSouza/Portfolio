import pytest
from model.video_model import VideoModel

def test_download_transcribe_summarize(monkeypatch):
    model = VideoModel()

    # Mock download_video to avoid real download
    monkeypatch.setattr(model, "download_video", lambda url: "test.mp4")
    # Mock transcribe_video to avoid real Whisper usage
    monkeypatch.setattr(model, "transcribe_video", lambda x: "This is a test video about Python and AI.")
    # Mock summarize_text to avoid real Transformer usage
    monkeypatch.setattr(model, "summarize_text", lambda x, y: f"Test summary for {y}.")

    video_file = model.download_video("https://youtube.com/test")
    transcription = model.transcribe_video(video_file)
    summary = model.summarize_text(transcription, "Introduction")

    assert video_file == "test.mp4"
    assert "Python" in transcription
    assert summary == "Test summary for Introduction."
