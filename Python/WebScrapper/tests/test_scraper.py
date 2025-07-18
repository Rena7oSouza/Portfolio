import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.controller.scraper_controller import ScraperController

def test_get_exchange_rate():
    rate = ScraperController.get_exchange_rate()
    assert rate is not None
    assert float(rate.replace(',', '.')) > 0
