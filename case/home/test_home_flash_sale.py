
from case import *
from case.page_object.page_common import click_go_back
from case.page_object.page_goods.page_goods_details import assert_goods_details_open
from case.page_object.page_home.page_home import *
from case.page_object.page_tv_item.page_account import assert_account_open
from case.page_object.page_tv_item.page_website import assert_website_open

@allure.feature("首页测试")
@allure.story("限时抢购测试")
@allure.title("首页限时抢购列表商品点击流程")
@allure.description("对首页限时抢购进行断言，滑动限时抢购到顶部，依次点击所有商品")
@allure.link("test_home_flash_sale_goods_click.html", name="用例详情页")
@copy_result_html("test_home_flash_sale_goods_click.html")
def test_home_flash_sale_goods_click():
    assert_home_flash_sale_exist()
    swipe_home_flash_sale_to_top()
    sleep(0.5)
    for i in ["one", "two", "three"]:
        click_home_flash_sale_goods(i)
        assert_goods_details_open()
        click_go_back()


@allure.feature("首页测试")
@allure.story("限时抢购测试")
@allure.title("首页限时抢购下im_item:会计服务、网站营销点击流程")
@allure.description("对首页限时抢购进行断言，滑动限时抢购到顶部，依次点击会计服务、网站营销")
@allure.link("test_home_flash_sale_item_click.html", name="用例详情页")
@copy_result_html("test_home_flash_sale_item_click.html")
def test_home_flash_sale_item_click():
    assert_home_flash_sale_exist()
    swipe_home_flash_sale_to_top()
    click_home_flash_sale_item(0)
    assert_account_open()
    click_go_back()
    click_home_flash_sale_item(1)
    assert_website_open()
