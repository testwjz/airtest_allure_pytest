import allure

from case.page_object import *


@allure.step("断言商标注册打开")
def assert_trademark_open():
    poco_assert_exists(pocoObject("android.view.View", text='商标注册'))