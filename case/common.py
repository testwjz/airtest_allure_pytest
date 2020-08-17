from airtest.core.api import *
from poco.exceptions import PocoTargetTimeout

MAX_TIME_OUT = 6
MIN_TIME_OUT = 3


def airtest_text_wait_poco(obj, arg, timeout=None):
    """
    Input text on the target device use Airtest if pocoObject exist

    :param obj: poco Object
    :param arg: arg to input, unicode is supported
    :param timeout:time interval to wait for the match
    :return: None
    """
    timeout = timeout or MAX_TIME_OUT
    if isinstance(obj, Template):
        wait(obj, timeout)
    else:
        obj.wait_for_appearance(timeout)
    text(arg)


def airtest_text_wait_tv(tv, arg, timeout=None):
    """
    Input text on the target device use Airtest if Template exist

    :param tv: Template instance
    :param arg: arg to input, unicode is supported
    :param timeout:time interval to wait for the match
    :return: None
    """
    timeout = timeout or MAX_TIME_OUT
    wait(tv, timeout)
    text(arg)


def airtest_touch_wait_tv(tv, timeout=None):
    """
    Wait timeout to match the Template on the device screen to Perform the touch action on the device screen

    :param tv: Template instance
    :param timeout: time interval to wait for the match
    :return:
    """
    timeout = timeout or MAX_TIME_OUT
    pos = wait(tv, timeout)
    touch(pos)


def poco_assert_exists(pocoObject, timeout=None):
    """
    Assert poco object exist

    :param pocoObject: poco object
    :param timeout: time interval to wait for the match
    :return: bool
    """
    timeout = timeout or MAX_TIME_OUT
    try:
        pocoObject.wait_for_appearance(timeout)
        return True
    except PocoTargetTimeout as e:
        return False


def poco_assert_not_exists(pocoObject, timeout=None):
    """
    Assert poco object not exist

    :param pocoObject: poco object
    :param timeout: time interval to wait for the match
    :return: bool
    """
    timeout = timeout or MIN_TIME_OUT
    try:
        pocoObject.wait_for_disappearance(timeout)
        return True
    except PocoTargetTimeout as e:
        return False


def package_opened(package):
    """
    Determines whether the package is open

    :param package: name of the package
    :return:bool
    """
    try:
        shell("pidof %s" % package)
        return True
    except Exception as err:
        return False
