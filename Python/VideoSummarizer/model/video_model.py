import whisper
from transformers import pipeline
import os
from pytubefix import YouTube

class VideoModel:
    def __init__(self):
        # Load Whisper model for transcription
        self.whisper_model = whisper.load_model("tiny")
        # Load summarization pipeline from Hugging Face Transformers
        self.summarizer = pipeline("summarization", model="t5-small")   
         
    #Downloads the highest resolution video from YouTube.
    def download_video(self, url):
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        original_path = ys.download()
        new_filename = "video.mp4"
        os.rename(original_path, new_filename)
        return new_filename
    
    #Transcribes the video using Whisper.
    def transcribe_video(self, video_filename):
        result = self.whisper_model.transcribe(video_filename, fp16=False)
        return result["text"]
    
    #Summarizes the transcribed text
    def summarize_text(self, text, max_chunk_size=500):
        chunks = []
        # Split text into chunks
        for i in range(0, len(text), max_chunk_size):
            chunk = text[i:i + max_chunk_size]
            summary = self.summarizer(chunk, max_length=100, min_length=30, do_sample=False)
            chunks.append(summary[0]["summary_text"])

        # Combine summaries into a final summary
        final_summary = " ".join(chunks)
        return final_summary


