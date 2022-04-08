import time

from Data.ExcelLib import read_data
from POM.LoginPage import LoginPage
from pytest import mark

headers, data = read_data("LoginPage", "test_login")


@mark.parametrize(headers, data)
class Test_Login:

    def test_login(self, _driver, phone_number, otp):
        lp = LoginPage(_driver)
        lp.enter_phn_num(phone_number)
        lp.click_get_otp()
        lp.enter_otp(otp)
        lp.click_verify_otp()


