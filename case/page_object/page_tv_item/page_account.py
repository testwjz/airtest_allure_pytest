import allure

from case.page_object import *


@allure.step("断言会计财税打开")
def assert_account_open():
    poco_assert_exists(pocoObject("android.view.View", text='会计代理记账'))