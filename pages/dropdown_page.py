from pages.base_page import BasePage
from utils.config import PRACTICE_BASE_URL
from utils.logger import logger


class DropdownPage(BasePage):
    URL = f"{PRACTICE_BASE_URL}/dropdown"

    SIMPLE_DROPDOWN = "select#dropdown"
    COUNTRY_DROPDOWN = "select#country"

    def open(self):
        self.navigate(self.URL)

    def select_option(self, option_text: str):
        logger.info(f"Selecting option: {option_text}")
        self.page.locator(self.SIMPLE_DROPDOWN).select_option(label=option_text)

    def get_selected_option(self) -> str:
        return self.page.locator(self.SIMPLE_DROPDOWN).evaluate(
            "el => el.options[el.selectedIndex].text"
        )

    def select_country(self, country: str):
        logger.info(f"Selecting country: {country}")
        self.page.locator(self.COUNTRY_DROPDOWN).select_option(label=country)

    def get_selected_country(self) -> str:
        return self.page.locator(self.COUNTRY_DROPDOWN).evaluate(
            "el => el.options[el.selectedIndex].text"
        )
