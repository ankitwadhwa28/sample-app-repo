from pages.base_page import BasePage
from utils.config import PRACTICE_BASE_URL
from utils.logger import logger


class RadioButtonsPage(BasePage):
    URL = f"{PRACTICE_BASE_URL}/radio-buttons"

    def open(self):
        self.navigate(self.URL)

    def _radio(self, value: str):
        return self.page.locator(f"input[type='radio'][value='{value}']")

    def select_color(self, color: str):
        logger.info(f"Selecting color: {color}")
        self._radio(color.lower()).check()

    def select_sport(self, sport: str):
        logger.info(f"Selecting sport: {sport}")
        self._radio(sport.lower()).check()

    def is_color_selected(self, color: str) -> bool:
        return self._radio(color.lower()).is_checked()

    def is_sport_selected(self, sport: str) -> bool:
        return self._radio(sport.lower()).is_checked()
