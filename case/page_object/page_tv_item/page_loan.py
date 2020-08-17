import allure

from case.page_object import *


@allure.step("断言贷款服务打开")
def assert_loan_open():
    poco_assert_exists(pocoObject("android.view.View", text='信用贷款'))