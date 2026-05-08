from pytest_bdd import given, when, then, parsers
from pages.checkboxes_page import CheckboxesPage


@given("I am on the checkboxes page", target_fixture="checkboxes_page")
def open_checkboxes_page(page):
    cp = CheckboxesPage(page)
    cp.open()
    return cp


@when(parsers.parse("I check checkbox {index:d}"))
def check_checkbox(checkboxes_page, index):
    checkboxes_page.check(index)


@when(parsers.parse("I uncheck checkbox {index:d}"))
def uncheck_checkbox(checkboxes_page, index):
    checkboxes_page.uncheck(index)


@then("both checkboxes should be unchecked")
def verify_all_unchecked(checkboxes_page):
    count = checkboxes_page.get_count()
    for i in range(1, count + 1):
        assert not checkboxes_page.is_checked(i), f"Checkbox {i} should be unchecked by default"


@then(parsers.parse("checkbox {index:d} should be checked"))
def verify_checked(checkboxes_page, index):
    assert checkboxes_page.is_checked(index), f"Checkbox {index} should be checked"


@then(parsers.parse("checkbox {index:d} should be unchecked"))
def verify_unchecked(checkboxes_page, index):
    assert not checkboxes_page.is_checked(index), f"Checkbox {index} should be unchecked"
