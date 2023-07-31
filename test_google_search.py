import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def browser_window_size():
    browser.config.window_width = 500
    browser.config.window_height = 500


@pytest.fixture()
def open_google(browser_window_size):
    browser.open('https://google.com')


def test_from_first_lesson(open_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_search_nonexistent_result(open_google):
    request = 'hdfjhjfakjfhdjhkjdhkjghdjhgjhdk'
    browser.element('[name="q"]').should(be.blank).type(request).press_enter()
    browser.element('[class="card-section"]').should(have.text(f'По запросу {request} ничего не найдено'))
