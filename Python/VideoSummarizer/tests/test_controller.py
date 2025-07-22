from controller.video_controller import VideoController

def test_process_video(monkeypatch):
    controller = VideoController()
    # Mock model methods
    monkeypatch.setattr(controller.model, "download_video", lambda url: "test.mp4")
    monkeypatch.setattr(controller.model, "transcribe_video", lambda x: "Test text")
    monkeypatch.setattr(controller.model, "summarize_text", lambda x: "Summary of entire video.")

    summary = controller.process_video("https://youtube.com/test")
    
    assert summary == "Summary of entire video."

