import time

from library import *
from library.custom_wait import wait_


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait_()
    def enter_text(self, element, *, value):
        locator_type, locator_value = element
        self.driver.find_element(locator_type, locator_value).clear()
        self.driver.find_element(locator_type, locator_value).send_keys(str(value))

    @wait_()
    def click_element(self, element):
        locator_type, locator_value = element
        self.driver.find_element(locator_type, locator_value).click()
