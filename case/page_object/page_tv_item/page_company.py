import allure

from case.page_object import *


@allure.step("断言公司注册打开")
def assert_company_open():
    poco_assert_exists(pocoObject("android.view.View", text='选择合适的公司类型'))