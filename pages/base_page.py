from playwright.sync_api import Page, expect
from utils.config import TIMEOUT
from utils.logger import logger


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(TIMEOUT)

    def navigate(self, url: str):
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def click(self, selector: str):
        logger.debug(f"Clicking: {selector}")
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        logger.debug(f"Filling '{selector}' with: {text}")
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        text = self.page.locator(selector).inner_text()
        logger.debug(f"Got text from '{selector}': {text}")
        return text

    def is_visible(self, selector: str) -> bool:
        visible = self.page.locator(selector).is_visible()
        logger.debug(f"Is visible '{selector}': {visible}")
        return visible

    def wait_for_url(self, url_pattern: str):
        logger.debug(f"Waiting for URL: {url_pattern}")
        self.page.wait_for_url(url_pattern)

    def assert_visible(self, selector: str):
        logger.debug(f"Asserting visible: {selector}")
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text(self, selector: str, text: str):
        logger.debug(f"Asserting text '{text}' on: {selector}")
        expect(self.page.locator(selector)).to_have_text(text)

    def screenshot(self, name: str):
        path = f"reports/{name}.png"
        logger.info(f"Taking screenshot: {path}")
        self.page.screenshot(path=path)
