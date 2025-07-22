from model.video_model import VideoModel

class VideoController:
    def __init__(self):
        self.model = VideoModel()

    #Orchestrates downloading, transcribing, and summarizing the video.
    def process_video(self, url):
        video_file = self.model.download_video(url)
        transcription = self.model.transcribe_video(video_file)
        summary = self.model.summarize_text(transcription)
        return summary

