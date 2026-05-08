from pages.base_page import BasePage
from utils.config import PRACTICE_BASE_URL
from utils.logger import logger


class FormValidationPage(BasePage):
    URL = f"{PRACTICE_BASE_URL}/form-validation"

    CONTACT_NAME = "#contactName"
    CONTACT_NUMBER = "#contactNumber"
    PICKUP_DATE = "#pickUpDate"
    PAYMENT_METHOD = "#paymentMethod"
    SUBMIT_BTN = "button[type='submit']"
    INVALID_INPUT = "input.is-invalid, select.is-invalid"
    INVALID_FEEDBACK = ".invalid-feedback"

    def open(self):
        self.navigate(self.URL)

    def fill_contact_name(self, name: str):
        self.fill(self.CONTACT_NAME, name)

    def fill_contact_number(self, number: str):
        self.fill(self.CONTACT_NUMBER, number)

    def fill_pickup_date(self, date: str):
        self.fill(self.PICKUP_DATE, date)

    def select_payment_method(self, method: str):
        logger.info(f"Selecting payment method: {method}")
        self.page.locator(self.PAYMENT_METHOD).select_option(label=method)

    def submit(self):
        self.click(self.SUBMIT_BTN)

    def has_validation_errors(self) -> bool:
        return self.page.locator(self.INVALID_INPUT).count() > 0

    def fill_valid_form(self, name: str, number: str, date: str, payment: str):
        self.fill_contact_name(name)
        self.fill_contact_number(number)
        self.fill_pickup_date(date)
        self.select_payment_method(payment)
