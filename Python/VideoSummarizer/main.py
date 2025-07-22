import tkinter as tk
from view.video_view import VideoView

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoView(root)
    root.mainloop()
