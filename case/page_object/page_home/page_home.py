import allure
from poco.exceptions import  PocoException

from case.page_object import *

TV_LBS = "net.dgg.fitax:id/tv_lbs"

@allure.step("断言首页打开")
def assert_home_open():
    poco_assert_exists(pocoObject("net.dgg.fitax:id/tv_search_des", text='搜索您想找的服务'))


@allure.step("点击title搜索框")
def click_home_search_box():
    pocoObject("net.dgg.fitax:id/tv_search_des", text='搜索您想找的服务').click()


@allure.step("点击tv列表")
def click_home_tv_item(item_name):
    pocoObject("net.dgg.fitax:id/tv_item_name", text=item_name).click()


@allure.step("断言限时抢购存在")
def assert_home_flash_sale_exist():
    assert poco_assert_exists(pocoObject("net.dgg.fitax:id/tv_title_flash_sale", text="限时抢购"))


@allure.step("滑动限时抢购到顶部")
def swipe_home_flash_sale_to_top():
    pocoObject("net.dgg.fitax:id/tv_title_flash_sale", text="限时抢购").drag_to(pocoObject(TV_LBS))


@allure.step("点击限时抢购下商品")
def click_home_flash_sale_goods(index):
    """
    传入id，对限时抢购商品进行点击

    :param index: one(公司变更)  two（公司注册）   three（商标注册）：版本升级后，内容可能会有变化，主要开运营配置
    :return:None
    """
    pocoObject("net.dgg.fitax:id/iv_flash_sale_%s" % index).click()


@allure.step("点击限时抢购下im_item:会计服务、网站营销")
def click_home_flash_sale_item(index=0):
    """
    传入index，对限时抢购下im_item进行点击

    :param index: 0代表：会计服务   1代表：网站营销  版本升级后，内容可能会有变化，主要开运营配置
    :return:None
    """
    if index not in [0, 1]:
        raise Exception("输入index 范围为【0,1】")
    pocoObject("net.dgg.fitax:id/vp_grid_view_ad").offspring("net.dgg.fitax:id/im_item_icon")[index].click()


@allure.step("断言热销产品存在")
def assert_home_hot_sale_exist():
    assert poco_assert_exists(pocoObject("net.dgg.fitax:id/tv_title_hot_sale", text="热销产品"))


@allure.step("滑动热销产品到顶部")
def swipe_home_hot_sale_to_top():
    pocoObject("net.dgg.fitax:id/tv_title_hot_sale", text="热销产品").drag_to(pocoObject(TV_LBS))


@allure.step("点击热销产品下商品")
def click_home_hot_sale_goods(index=0):
    """
    传入index，对热销产品下im_item（商品）进行点击

    :param index: 0代表：社保代理   1代表：刻章印章  2代表：模板网站  3代表：代理记账  版本升级后，内容可能会有变化，主要开运营配置
    :return:None
    """
    if index not in [0, 1, 2, 3]:
        raise Exception("输入index 范围为【0,1,2,3】")
    pocoObject("net.dgg.fitax:id/pgv_ad_hot_sale_products").offspring("net.dgg.fitax:id/im_item_icon")[index].click()


@allure.step("断言推荐服务存在")
def assert_home_recommend_servers_exist():
    assert poco_assert_exists(pocoObject("android.widget.TextView", text="推荐服务"))


@allure.step("滑动热销产品到顶部")
def swipe_home_recommend_servers_to_top():
    pocoObject("android.widget.TextView", text="推荐服务").drag_to(pocoObject(TV_LBS))


@allure.step("点击推荐服务下title")
def click_home_recommend_servers_title(title_name):
    pocoObject("net.dgg.fitax:id/tv_tab_title", text=title_name).click()


@allure.step("点击推荐服务下商品")
def click_home_recommend_servers_goods(index=0):
    """
    传入index，对推荐服务下（商品）进行点击

    :param index: 0代表：当前可见列表第一个产品 依次类推
    :return:None
    """
    try:
        pocoObject("net.dgg.fitax:id/rl_item_product")[index].click()
    except PocoException as e:
        pocoObject("net.dgg.fitax:id/tv_title")[index].click()