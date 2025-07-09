import tkinter as tk
from app.controller.chatbot_controller import handle_user_message

def run_chatbot():
    window = tk.Tk()
    window.title("AI Chatbot (Local GPT-2)")
    window.geometry("500x600")

    chat_log = tk.Text(window, bg="white", fg="black", wrap="word")
    chat_log.pack(padx=10, pady=10, expand=True, fill="both")

    entry = tk.Entry(window, width=50)
    entry.pack(padx=10, pady=(0, 10), side="left", fill="x", expand=True)

    def send_message(event=None):
        message = entry.get()
        if message.strip():
            chat_log.insert(tk.END, f"You: {message}\n")
            entry.delete(0, tk.END)
            response = handle_user_message(message)
            chat_log.insert(tk.END, f"Bot: {response}\n\n")
            chat_log.see(tk.END)

    entry.bind("<Return>", send_message)

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack(padx=10, pady=(0, 10), side="right")

    window.mainloop()
