from pytest_bdd import given, when, then, parsers
from pages.form_validation_page import FormValidationPage


@given("I am on the form validation page", target_fixture="form_validation_page")
def open_form_validation_page(page):
    fv = FormValidationPage(page)
    fv.open()
    return fv


@when(parsers.parse('I fill contact name "{name}"'))
def fill_contact_name(form_validation_page, name):
    form_validation_page.fill_contact_name(name)


@when(parsers.parse('I fill contact number "{number}"'))
def fill_contact_number(form_validation_page, number):
    form_validation_page.fill_contact_number(number)


@when(parsers.parse('I fill pickup date "{date}"'))
def fill_pickup_date(form_validation_page, date):
    form_validation_page.fill_pickup_date(date)


@when(parsers.parse('I select payment method "{method}"'))
def select_payment_method(form_validation_page, method):
    form_validation_page.select_payment_method(method)


@when("I submit the form")
def submit_form(form_validation_page):
    form_validation_page.submit()


@then("the form should be submitted successfully")
def verify_form_success(form_validation_page):
    assert not form_validation_page.has_validation_errors(), (
        "Form submission should succeed with no validation errors"
    )


@then("I should see validation errors")
def verify_validation_errors(form_validation_page):
    assert form_validation_page.has_validation_errors(), (
        "Expected validation errors to be visible after invalid submission"
    )
