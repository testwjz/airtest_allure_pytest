import allure

from case.page_object import *


@allure.step("断言精选案例打开")
def assert_case_open():
    poco_assert_exists(pocoObject("android.widget.ImageView", text='精选'))