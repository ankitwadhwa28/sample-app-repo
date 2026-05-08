from pytest_bdd import given, when, then, parsers
from pages.dropdown_page import DropdownPage


@given("I am on the dropdown page", target_fixture="dropdown_page")
def open_dropdown_page(page):
    dp = DropdownPage(page)
    dp.open()
    return dp


@when(parsers.parse('I select "{option}" from the dropdown'))
def select_from_dropdown(dropdown_page, option):
    dropdown_page.select_option(option)


@when(parsers.parse('I select country "{country}"'))
def select_country(dropdown_page, country):
    dropdown_page.select_country(country)


@then(parsers.parse('the selected option should be "{option}"'))
def verify_selected_option(dropdown_page, option):
    actual = dropdown_page.get_selected_option()
    assert actual == option, f"Expected selected option '{option}', got '{actual}'"


@then(parsers.parse('the selected country should be "{country}"'))
def verify_selected_country(dropdown_page, country):
    actual = dropdown_page.get_selected_country()
    assert actual == country, f"Expected selected country '{country}', got '{actual}'"
