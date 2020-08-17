import allure

from case.page_object import *


@allure.step("断言网站营销打开")
def assert_website_open():
    poco_assert_exists(pocoObject("android.view.View", text='网站/域名'))