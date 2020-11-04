from unittest import result

from selenium.webdriver.common.by import By
from selenium import webdriver

from test_selenium.page.base_page import BasePage


class Register(BasePage):

    def register(self,corpname):
        self._driver.find_element(By.ID, "corp_name").send_keys(corpname)
        self._driver.find_element(By.ID, "submit_btn").click()
        return self

    def get_error_message(self):

        return self._driver.find_elements(By.CSS_SELECTOR,".js_error_msg")[1].text


