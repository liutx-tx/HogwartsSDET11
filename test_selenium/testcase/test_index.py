import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.index import Index


class Test_Index:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

        self.driver.get("https://work.weixin.qq.com/")

    def test_register(self):

        # self.driver.find_element(By.LINK_TEXT,"立即注册").click()

        # self.driver.find_element(By.ID,"corp_name_label").send_keys(("DK"))
        # self.driver.find_element(By.ID,"submit_btn").click()
        index = Index(self.driver)
        index.goto_register().register("DK")