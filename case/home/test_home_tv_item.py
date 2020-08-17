# -*- coding: utf-8 -*-
import allure

from case import *
from case.page_object.page_common import click_go_back
from case.page_object.page_home.page_home import click_home_tv_item
from case.page_object.page_tv_item.page_account import assert_account_open
from case.page_object.page_tv_item.page_articles import assert_articles_open
from case.page_object.page_tv_item.page_case import assert_case_open
from case.page_object.page_tv_item.page_company import assert_company_open
from case.page_object.page_tv_item.page_deal import assert_deal_open
from case.page_object.page_tv_item.page_law import assert_law_open
from case.page_object.page_tv_item.page_loan import assert_loan_open
from case.page_object.page_tv_item.page_patent import assert_patent_open
from case.page_object.page_tv_item.page_trademark import assert_trademark_open
from case.page_object.page_tv_item.page_website import assert_website_open


@allure.feature("首页测试")
@allure.story("tv_item点击测试")
@allure.title("首页tv_item点击测试")
@allure.description("对首页tv_item进行点击测试，并分别进行断言")
@allure.link("test_home_tv_item.html", name="用例详情页")
@copy_result_html("test_home_tv_item.html")
def test_home_tv_item():
    click_home_tv_item("公司注册")
    assert_company_open()
    click_go_back()
    click_home_tv_item("会计财税")
    assert_account_open()
    click_go_back()
    click_home_tv_item("贷款服务")
    assert_loan_open()
    click_go_back()
    click_home_tv_item("网站营销")
    assert_website_open()
    click_go_back()
    click_home_tv_item("商标注册")
    assert_trademark_open()
    click_go_back()
    click_home_tv_item("专利服务")
    assert_patent_open()
    click_go_back()
    click_home_tv_item("法律服务")
    assert_law_open()
    click_go_back()
    click_home_tv_item("交易平台")
    assert_deal_open()
    click_go_back()
    click_home_tv_item("精选文章")
    assert_articles_open()
    click_go_back()
    click_home_tv_item("精选案例")
    assert_case_open()
    click_go_back()
