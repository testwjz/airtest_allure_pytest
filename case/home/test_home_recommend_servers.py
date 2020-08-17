from case import *
from case.page_object.page_common import click_go_back
from case.page_object.page_goods.page_goods_details import assert_goods_details_open

from case.page_object.page_home.page_home import *


def _commond_goods(title_name):
    assert_home_flash_sale_exist()
    swipe_home_flash_sale_to_top()
    assert_home_hot_sale_exist()
    swipe_home_hot_sale_to_top()
    assert_home_recommend_servers_exist()
    swipe_home_recommend_servers_to_top()
    click_home_recommend_servers_title(title_name)
    for i in [0, 1, 2]:
        click_home_recommend_servers_goods(i)
        assert_goods_details_open()
        click_go_back()


@allure.feature("首页测试")
@allure.story("推荐服务测试")
@allure.title("首页推荐服务-工商服务列表商品点击流程")
@allure.description("对首页限时抢购进行断言，滑动限时抢购到顶部，对热销产品进行断言，滑动热销产品到顶部，对推荐服务进行断"
                    "言，滑动推荐服务到顶部，依次点击前三个商品")
@allure.link("test_home_recommend_servers_gs_goods_click.html", name="用例详情页")
@copy_result_html("test_home_recommend_servers_gs_goods_click.html")
def test_home_recommend_servers_gs_goods_click():
    _commond_goods("工商服务")


@allure.feature("首页测试")
@allure.story("推荐服务测试")
@allure.title("首页推荐服务-会计/税务服务列表商品点击流程")
@allure.description("对首页限时抢购进行断言，滑动限时抢购到顶部，对热销产品进行断言，滑动热销产品到顶部，对推荐服务进行断"
                    "言，滑动推荐服务到顶部，点击会计/税务title，依次点击前三个商品")
@allure.link("test_home_recommend_servers_ki_goods_click.html", name="用例详情页")
@copy_result_html("test_home_recommend_servers_ki_goods_click.html")
def test_home_recommend_servers_ki_goods_click():
    _commond_goods("会计/税务")


# @allure.feature("首页测试")
# @allure.story("推荐服务测试")
# @allure.title("首页推荐服务-财税服务列表商品点击流程")
# @allure.description("对首页限时抢购进行断言，滑动限时抢购到顶部，对热销产品进行断言，滑动热销产品到顶部，对推荐服务进行断"
#                     "言，滑动推荐服务到顶部，点击财税服务title，依次点击前三个商品")
# @allure.link("test_home_recommend_servers_csfw_goods_click.html", name="用例详情页")
# @copy_result_html("test_home_recommend_servers_csfw_goods_click.html")
# def test_home_recommend_servers_csfw_goods_click():
#     _commond_goods("财税服务")

# TOCO待增加更多的title商品点击用例
