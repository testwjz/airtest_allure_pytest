import os

import allure
from airtest.core.cv import Template

from case import templateDir
from case.common import airtest_touch_wait_tv

GOBACKTP = os.path.join(templateDir, "tpl1588752941545.png")
GOBACK_V = Template(GOBACKTP, record_pos=(-0.437, -0.897), resolution=(1080, 2280))


@allure.step("点击返回上一页图标：<")
def click_go_back():
    airtest_touch_wait_tv(GOBACK_V)
