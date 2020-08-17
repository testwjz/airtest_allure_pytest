# -*- coding: utf-8 -*-
from case import *
from case.page_object.page_home.page_home import click_home_search_box
from case.page_object.page_home.page_home_search import *


@allure.feature("首页测试")
@allure.story("搜索功能测试")
@allure.title("首页正常搜索流程")
@allure.description("对首页搜索框进行搜索，搜索页面有结果，并对结果进行断言，最终将搜索内容清空")
@allure.link("test_home_search_exist.html", name="用例详情页")
@copy_result_html("test_home_search_exist.html")
def test_home_search_exist():
    click_home_search_box()
    assert_search_button_exist()
    enter_content_into_search_box("公司注册")
    assert_search_list_data("公司注册")
    click_cancel_button()
    assert_histrory_have_recorded()
    clear_history()
    assert_histrory_unrecorded()


@allure.feature("首页测试")
@allure.story("搜索功能测试")
@allure.title("首页异常搜索流程")
@allure.description("对首页搜索框进行搜索，搜索页面无结果，并对结果进行断言，最终将搜索内容清空")
@allure.link("test_home_search_not_exist.html", name="用例详情页")
@copy_result_html("test_home_search_not_exist.html")
def test_home_search_not_exist():
    click_home_search_box()
    assert_search_button_exist()
    enter_content_into_search_box("不存在的内容")
    assert_search_list_no_data()
    click_delete_button()
    assert_histrory_have_recorded()
    clear_history()
    assert_histrory_unrecorded()