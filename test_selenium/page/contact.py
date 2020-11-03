import os

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

class Contact:
    add_memeber_button=(By.ID,"xxxx")

    def add_member(self,data):
        self.driver.find_element("添加成员").click()
        pass

    def search(self,name):

        pass

    def import_users(self,data):
        pass

    def set_department(self,data):
        pass

    def delete(self):
        pass

    def invite(self):
        pass

    def add_department(self):
        pass