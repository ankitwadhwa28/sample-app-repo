from pytest_bdd import given, when, then, parsers
from pages.practice_login_page import PracticeLoginPage
from utils.logger import logger


@given("I am on the practice login page", target_fixture="practice_login_page")
def open_practice_login_page(page):
    lp = PracticeLoginPage(page)
    lp.open()
    return lp


@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def do_login(practice_login_page, username, password):
    practice_login_page.login(username, password)


@then("I should be redirected to the secure page")
def verify_secure_redirect(practice_login_page):
    practice_login_page.wait_for_url("**/secure")
    assert practice_login_page.is_on_secure_page(), "Expected to land on the secure page after login"


@then(parsers.parse('I should see flash message "{message}"'))
def verify_flash_message(practice_login_page, message):
    actual = practice_login_page.get_flash_message()
    logger.info(f"Flash message: {actual}")
    assert message in actual, f"Expected flash to contain '{message}', got: '{actual}'"
