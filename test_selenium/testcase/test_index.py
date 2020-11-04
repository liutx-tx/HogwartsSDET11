import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.index import Index


class Test_Index:

    def setup(self):
        self.index = Index()

    def test_register(self):

        # self.driver.find_element(By.LINK_TEXT,"立即注册").click()

        # self.driver.find_element(By.ID,"corp_name_label").send_keys(("DK"))
        # self.driver.find_element(By.ID,"submit_btn").click()
        # index = Index(self.driver)
        self.index.goto_register().register("DK")


    def test_login(self):
        register_page = self.index.goto_login().goto_register().register("测吧")
        print(register_page.get_error_message())
        print("|".join(register_page.get_error_message()))
        assert "请选择" in register_page.get_error_message()

    def teardown(self):
        self.index.close()
