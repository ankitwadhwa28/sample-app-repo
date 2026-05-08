from pytest_bdd import given, when, then, parsers
from pages.radio_buttons_page import RadioButtonsPage


@given("I am on the radio buttons page", target_fixture="radio_buttons_page")
def open_radio_buttons_page(page):
    rb = RadioButtonsPage(page)
    rb.open()
    return rb


@when(parsers.parse('I select color "{color}"'))
def select_color(radio_buttons_page, color):
    radio_buttons_page.select_color(color)


@when(parsers.parse('I select sport "{sport}"'))
def select_sport(radio_buttons_page, sport):
    radio_buttons_page.select_sport(sport)


@then(parsers.parse('color "{color}" should be selected'))
def verify_color_selected(radio_buttons_page, color):
    assert radio_buttons_page.is_color_selected(color), f"Color '{color}' should be selected"


@then(parsers.parse('sport "{sport}" should be selected'))
def verify_sport_selected(radio_buttons_page, sport):
    assert radio_buttons_page.is_sport_selected(sport), f"Sport '{sport}' should be selected"


@then(parsers.parse('color "{color}" should not be selected'))
def verify_color_not_selected(radio_buttons_page, color):
    assert not radio_buttons_page.is_color_selected(color), f"Color '{color}' should not be selected"
