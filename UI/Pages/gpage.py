import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url = 'https://www.google.com/'


class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.searchbar = 'q'
        self.title = "//h3[contains(text(),'Automatización - Wikipedia, la enciclopedia libre')]"
        self.search = 'Automatizacion'

    def initialsearch(self):
        q = self.driver.find_element(By.NAME,  self.searchbar)
        q.click()
        q.send_keys('Automatizacion')
        q.send_keys(Keys.ENTER)

    def click_on_wiki_title(self):
        search = self.driver.find_element(By.XPATH, self.title)
        search.click()

    @staticmethod
    def getBaseUrl():
        return base_url
