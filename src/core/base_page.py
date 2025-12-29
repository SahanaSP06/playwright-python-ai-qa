from playwright.sync_api import Page
import logging

logging.basicConfig(level=logging.INFO)

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    def navigate(self, url: str):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url, timeout=30000)

    def click(self, locator):
        locator.click()

    def fill(self, locator, value: str):
        locator.fill(value)
