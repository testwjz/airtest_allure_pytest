from case import *
from case.page_object.page_common import click_go_back
from case.page_object.page_goods.page_goods_details import assert_goods_details_open

from case.page_object.page_home.page_home import *


@allure.feature("首页测试")
@allure.story("热销产品测试")
@allure.title("首页热销产品列表商品点击流程")
@allure.description("对首页限时抢购进行断言，滑动限时抢购到顶部，对热销产品进行断言，滑动热销产品到顶部，依次点击所有商品")
@allure.link("test_home_hot_sale_goods_click.html", name="用例详情页")
@copy_result_html("test_home_hot_sale_goods_click.html")
def test_home_hot_sale_goods_click():
    assert_home_flash_sale_exist()
    swipe_home_flash_sale_to_top()
    assert_home_hot_sale_exist()
    swipe_home_hot_sale_to_top()
    sleep(0.5)
    for i in [0, 1, 2, 3]:
        click_home_hot_sale_goods(i)
        assert_goods_details_open()
        click_go_back()
