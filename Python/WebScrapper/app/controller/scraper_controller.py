import requests
from bs4 import BeautifulSoup

class ScraperController:
    @staticmethod
    def get_exchange_rate():
        url = 'https://www.x-rates.com/calculator/?from=USD&to=BRL&amount=1'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Verifique a classe atual no site
        rate_span = soup.find('span', class_='ccOutputRslt')
        if rate_span:
            rate = rate_span.get_text().split(' ')[0]
            return rate
        else:
            print("[Controller] Could not find the exchange rate.")
            return None
