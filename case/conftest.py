import allure
import pytest
from airtest.core.api import stop_app, start_app

from case.common import package_opened
from case.page_object.page_home.page_home import assert_home_open


@allure.step("开启应用")
def init_app(package: str):
    if package_opened(package):
        stop_app(package)
    start_app(package)


@allure.step("初始化应用")
@pytest.fixture(scope="function", autouse=True)
def pre_test():
    init_app('net.dgg.fitax')
    assert_home_open()
