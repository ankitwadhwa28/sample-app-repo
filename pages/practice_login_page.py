from pages.base_page import BasePage
from utils.config import PRACTICE_BASE_URL
from utils.logger import logger


class PracticeLoginPage(BasePage):
    URL = f"{PRACTICE_BASE_URL}/login"

    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BTN = "button[type='submit']"
    FLASH_MSG = "#flash"

    def open(self):
        self.navigate(self.URL)

    def login(self, username: str, password: str):
        logger.info(f"Logging in as: {username}")
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BTN)

    def get_flash_message(self) -> str:
        self.page.locator(self.FLASH_MSG).wait_for(state="visible")
        return self.get_text(self.FLASH_MSG)

    def is_on_secure_page(self) -> bool:
        return "/secure" in self.page.url
