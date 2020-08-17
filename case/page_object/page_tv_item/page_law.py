import allure

from case.page_object import *


@allure.step("断言法律服务打开")
def assert_law_open():
    poco_assert_exists(pocoObject("android.view.View", text='民事案件'))