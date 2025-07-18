import tkinter as tk
from app.controller.scraper_controller import ScraperController
from app.model.exchange_model import ExchangeModel

class ExchangeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("USD-BRL Exchange Rate")
        self.window.geometry("300x150")
        
        self.label = tk.Label(self.window, text="Click to get USD-BRL rate", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.button = tk.Button(self.window, text="Get Rate", command=self.get_rate)
        self.button.pack(pady=5)
        
        self.result = tk.Label(self.window, text="", font=("Arial", 12))
        self.result.pack(pady=10)
        
        self.window.mainloop()
    
    def get_rate(self):
        rate = ScraperController.get_exchange_rate()
        if rate:
            exchange = ExchangeModel("USD-BRL", rate)
            exchange.save_to_csv()
            self.result.config(text=f"USD-BRL: R${rate}")
        else:
            self.result.config(text="Failed to get rate")
