from pages.base_page import BasePage
from utils.config import PRACTICE_BASE_URL
from utils.logger import logger


class CheckboxesPage(BasePage):
    URL = f"{PRACTICE_BASE_URL}/checkboxes"

    CHECKBOXES = "input[type='checkbox']"

    def open(self):
        self.navigate(self.URL)

    def _checkbox(self, index: int):
        return self.page.locator(self.CHECKBOXES).nth(index - 1)

    def check(self, index: int):
        logger.info(f"Checking checkbox {index}")
        self._checkbox(index).check()

    def uncheck(self, index: int):
        logger.info(f"Unchecking checkbox {index}")
        self._checkbox(index).uncheck()

    def is_checked(self, index: int) -> bool:
        return self._checkbox(index).is_checked()

    def get_count(self) -> int:
        return self.page.locator(self.CHECKBOXES).count()
