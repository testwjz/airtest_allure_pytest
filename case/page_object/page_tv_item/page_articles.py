import allure

from case.page_object import *


@allure.step("断言精选文章打开")
def assert_articles_open():
    poco_assert_exists(pocoObject("android.widget.ImageView", text='精选'))