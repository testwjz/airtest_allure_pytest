import allure

from case.page_object import *

@allure.step("断言交易平台打开")
def assert_deal_open():
    poco_assert_exists(pocoObject("android.view.View", text='4000-962540'))