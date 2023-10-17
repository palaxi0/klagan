import logging
from tkinter import Image
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class WikiPage:
    def __init__(self, driver):
        self.driver = driver
        self.info = "//p[contains(text() ,'En 1771 ')]"
        self.first_auto = ''

    def check_date(self):
        try:
            self.first_auto = self.driver.find_element(By.XPATH,  self.info)
            action = ActionChains(self.driver)
            action.move_to_element(self.first_auto).perform()
        except Exception as e:
            logging.exception(e)
        if self.first_auto != '':
            self.driver.save_screenshot("first.png")
