import tkinter as tk
from controller.video_controller import VideoController

class VideoView:
    def __init__(self, root):
        self.controller = VideoController()

        self.root = root
        self.root.title("Video Summarizer")

        # Video URL input
        self.url_label = tk.Label(root, text="Video URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        # Process button
        self.process_button = tk.Button(root, text="Summarize Video", command=self.process_video)
        self.process_button.pack()

        # Result text box
        self.result_text = tk.Text(root, wrap=tk.WORD, height=20, width=60)
        self.result_text.pack()

    #Handles button click to process the video and display the summary.
    def process_video(self):

        url = self.url_entry.get()
        self.result_text.delete(1.0, tk.END)
        summary = self.controller.process_video(url)
        self.result_text.insert(tk.END, summary)
