import time

from UI.Utils.Base import WebDriverSetup
from UI.Pages.gpage import GooglePage
from UI.Pages.wiki import WikiPage


class Test_Klagan(WebDriverSetup):

    def test_look_up_wikipedia(self):
        driver = self.driver
        self.driver.get(GooglePage.getBaseUrl())
        gpage = GooglePage(driver)
        gpage.initialsearch()
        gpage.click_on_wiki_title()
        wiki_page = WikiPage(driver)
        wiki_page.check_date()
