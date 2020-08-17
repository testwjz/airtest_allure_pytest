import allure

from case.page_object import *


@allure.step("断言专利服务打开")
def assert_patent_open():
    poco_assert_exists(pocoObject("android.view.View", text='专利申请'))