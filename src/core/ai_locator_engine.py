from playwright.sync_api import Page

class AILocatorEngine:
    def __init__(self, page: Page):
        self.page = page

    def find(self, primary: str, fallbacks: list):
        try:
            locator = self.page.locator(primary)
            locator.wait_for(timeout=3000)
            return locator
        except:
            for fb in fallbacks:
                try:
                    locator = self.page.locator(fb)
                    locator.wait_for(timeout=3000)
                    return locator
                except:
                    pass
        raise Exception("All locator strategies failed")
