import time
from Data.ExcelLib import read_locators
from library.selenium_wrapper import SeleniumWrapper


class LoginPage(SeleniumWrapper):
    # locator_phn_num = ("id", "phone-number-field")
    # locator_get_otp = ("xpath", "//div[text() = 'Get OTP']")
    # locator_verify_otp = ("xpath", "//div[text() = 'Verify OTP']")

    LoginPage_Objects = read_locators('LoginPage')
    def enter_phn_num(self, phn_num):
        locator_num = LoginPage.LoginPage_Objects['Phn_num']
        self.enter_text(locator_num, value=phn_num)

    def click_get_otp(self):
        locator_get_otp = LoginPage.LoginPage_Objects['get_otp']
        self.click_element(locator_get_otp)

    def enter_otp(self, otp):
        _otp = list(otp)
        for item in range(6):
            temp = ("id", f'otp-field-{item}')
            self.enter_text(temp, value=_otp[item])

    def click_verify_otp(self):
        locator_verify_otp = LoginPage.LoginPage_Objects['verify_otp']
        self.click_element(locator_verify_otp)

    def get_hierarchy_data(self):
        locator_hierarchy_data = LoginPage.LoginPage_Objects['hierarchy']
        return self.get_items_text(locator_hierarchy_data)








