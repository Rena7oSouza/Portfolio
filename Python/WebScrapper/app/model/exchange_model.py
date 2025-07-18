import pandas as pd

class ExchangeModel:
    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    def save_to_csv(self, filename='exchange_rate.csv'):
        df = pd.DataFrame([[self.currency, self.rate]], columns=['Currency', 'Rate'])
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"[Model] Exchange rate saved to {filename}")
