import os

import allure

from case import templateDir
from case.page_object import *

DUMPTP = os.path.join(templateDir, "tpl1588159280341.png")
NODATATP = os.path.join(templateDir, "tpl1588236070211.png")
DELETETP = os.path.join(templateDir, "tpl1588745274105.png")
DUMP_V = Template(DUMPTP, record_pos=(0.424, -0.782), resolution=(1080, 2280))
NODATA_V = Template(NODATATP, record_pos=(0.003, 0.126), resolution=(1080, 2280))
DELETE_V = Template(DELETETP, record_pos=(0.309, -0.917), resolution=(1080, 2280))

@allure.step("搜索框输入内容")
def enter_content_into_search_box(content):
    airtest_text_wait_poco(pocoObject("android.view.View", text="搜索"), content)


@allure.step("点击删除叉叉")
def click_delete_button():
    airtest_touch_wait_tv(DELETE_V)


@allure.step("点击取消按钮")
def click_cancel_button():
    pocoObject("android.view.View", text="取消").click()


@allure.step("清空历史记录")
def clear_history():
    airtest_touch_wait_tv(DUMP_V)
    pocoObject("android.view.View", text="清空").click()


@allure.step("断言搜索按钮存在")
def assert_search_button_exist():
    assert poco_assert_exists(pocoObject("android.view.View", text="搜索"))


@allure.step("断言界面有内容")
def assert_search_list_data(input_text):
    assert poco_assert_exists(pocoObject("android.widget.ImageView", textMatches=r'.*%s(.|\n)*' % input_text))


@allure.step("断言界面没有数据")
def assert_search_list_no_data():
    assert_exists(NODATA_V, "断言界面没有数据")


@allure.step("断言历史记录有记录")
def assert_histrory_have_recorded():
    assert_exists(DUMP_V, "清空回收站按钮存在")


@allure.step("断言历史记录无记录")
def assert_histrory_unrecorded():
    assert_not_exists(DUMP_V, "清空回收站按钮不存在")
