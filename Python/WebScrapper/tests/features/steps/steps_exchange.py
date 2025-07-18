from behave import given, when, then
from app.controller.scraper_controller import ScraperController

@given('I access the exchange scraper')
def step_given_access_scraper(context):
    context.scraper = ScraperController

@when('I get the USD-BRL rate')
def step_when_get_rate(context):
    context.rate = context.scraper.get_exchange_rate()

@then('the rate should be a valid number')
def step_then_check_rate(context):
    assert context.rate is not None
    assert float(context.rate.replace(',', '.')) > 0
