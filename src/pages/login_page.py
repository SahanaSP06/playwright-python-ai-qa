from src.core.base_page import BasePage
from src.core.ai_locator_engine import AILocatorEngine

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.ai = AILocatorEngine(page)

    def login(self, username, password):
        user = self.ai.find("input[name='username']", ["#username"])
        pwd = self.ai.find("input[name='password']", ["#password"])
        btn = self.ai.find("button[type='submit']", ["#login"])

        self.fill(user, username)
        self.fill(pwd, password)
        self.click(btn)
