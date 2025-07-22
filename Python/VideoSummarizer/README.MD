

A Python application that downloads a YouTube video, transcribes its audio using OpenAI Whisper, and summarizes the entire content using Hugging Face Transformers, following the **MVC design pattern** with a simple **Tkinter GUI**.

---

## 📂 **Project Structure**
```bash
project/
├── controller/
│ └── video_controller.py
├── model/
│ └── video_model.py
├── view/
│ └── video_view.py
├── tests/
│ ├── test_model.py
│ └── test_controller.py
├── features/
│ ├── video_summary.feature
│ └── steps/
│ └── video_summary_steps.py
├── main.py
└── requirements.txt
```

---

## 🚀 **Features**

✅ Downloads YouTube videos  
✅ Transcribes video audio using Whisper (tiny model for faster and lightweight execution)  
✅ Summarizes the entire transcription using DistilBART (`sshleifer/distilbart-cnn-12-6`)  
✅ GUI built with Tkinter  
✅ MVC architecture for clean code separation  
✅ Unit tests with Pytest  
✅ BDD tests with Behave

---

## 💻 **Installation**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/VideoResume.git
cd VideoResume
```
2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
## ⚙️ Running the Application
```bash
python main.py
```

The Tkinter GUI will open. Enter the YouTube video URL, click "Summarize Video", and the summarized text will appear in the text box.
## 🧪 Running Unit Tests
```basH
pytest tests/
```

## 📝 Running BDD Tests
```bash
behave features/
```

## ⚠️ Important Notes

    Uses Whisper tiny model (~75MB) for transcription to keep it lightweight.

    Uses DistilBART (sshleifer/distilbart-cnn-12-6, ~480MB) for summarization.

    Both models will download automatically the first time you run the app.

    If you want even smaller summarization models, change to t5-small in video_model.py.

## 🛠️ Technologies Used

    Python 3.12

    pytubefix

    openai-whisper

    transformers (Hugging Face)

    torch

    Tkinter

    pytest

    behave

## 💡 Future Improvements

    Replace local summarization with OpenAI ChatGPT API to avoid model downloads

    Add video/audio duration filters

    Save summaries to a SQLite database

    Implement user authentication for storing personal summaries

## 🙋‍♂️ Author

Developed by Renato Souza 🔗 https://rena7osouza.github.io/ 📫 renatofrancisco@hotmail.com

## 📝 Final Notes

✅ Tested on Ubuntu 24.04
✅ CPU execution (Whisper and Transformers models will run slower without CUDA GPU)
