import allure

from case import templateDir
from case.page_object import *

BUYTP = os.path.join(templateDir, r"tpl1589885191551.png")
BUY_V = Template(BUYTP, record_pos=(-0.379, 0.274), resolution=(1080, 2280))

@allure.step("断言商品详情页打开")
def assert_goods_details_open():
    assert_exists(BUY_V)