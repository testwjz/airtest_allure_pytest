import shutil
import sys
import traceback
from functools import wraps

import six
from airtest.core.api import auto_setup
from airtest.core.helper import G, log
from airtest.report.report import LogToHtml, HTML_TPL, STATIC_DIR
from airtest.utils.compat import script_dir_name

from config import *

caseFileName = __file__

templateDir = os.path.join(os.path.dirname(caseFileName), "template")


def copy_result_html(caseName: str):
    """
    该装饰器应用于case中，将allure与airtest报告集成
    用法：
    @allure.link("test_home_search_not_exist.html", name="用例详情页")
    @copy_result_html("test_home_search_not_exist.html")
    def test_home_search_not_exist():
        pass

    :param caseName 传入用例英文case名称以.html结尾，如login.html
    :return None
    """
    if not caseName or caseName.split('.')[-1] != 'html':
        G.LOGGING.error("copy_result_html装饰器参数不能为空，需要填入用例case英文名称且以.html结尾")

    def deco(fun):
        @wraps(fun)
        def report_html(*args, **kwargs):
            init_reportdir()
            # fun执行失败将写入日志，并标记用例执行失败
            try:
                fun(*args, **kwargs)
            except Exception as err:
                tb = traceback.format_exc()
                log("异常错误", tb)
                six.reraise(*sys.exc_info())
            finally:
                pass
                post_action(caseName)

        return report_html

    return deco


def copy_dir(source, target):
    """
    :param target: 目标目录
    :param source: 源目录
    将一个目录下的全部文件和目录,完整地<拷贝并覆盖>到另一个目录
    """

    if not os.path.isdir(source):
        return

    if not os.path.isdir(target):
        os.makedirs(target)

    for a in os.walk(source):
        # 递归创建目录
        for d in a[1]:
            dir_path = os.path.join(a[0].replace(source, target), d)
            if not os.path.isdir(dir_path):
                os.makedirs(dir_path)
        # 递归拷贝文件
        for f in a[2]:
            dep_path = os.path.join(a[0], f)
            arr_path = os.path.join(a[0].replace(source, target), f)
            if not os.path.isfile(arr_path):
                shutil.copyfile(dep_path, arr_path)


def rmdir(dirPath):
    if os.path.exists(dirPath):
        shutil.rmtree(dirPath)


def truncateFile(filePath):
    if os.path.exists(filePath):
        with open(filePath, 'w') as f:
            f.truncate()


def init_setup(device=None):
    """
    初始化airtest, 尝试连接安卓device

    :param device:
        * ``android:///`` # 本地adb device
        * ``android://adbhost:adbport/1234566?cap_method=javacap&touch_method=adb`` #远程adb device
    :return: None
    """
    if device is None:
        device = ["android:///"]
    auto_setup(basedir=caseFileName, devices=device, logdir=reportLogDir)


def init_reportdir():
    """
    初始化report文件夹，每次测试执行前清空log.txt文件内容，这样才能保证每条用例结果不重复
    :return:
    """
    truncateFile(reportLogFile)
    if not os.path.exists(reportLogDir):
        os.makedirs(reportLogDir)
    init_setup()


def modify_file(filePath, template=templateDir,log=reportLogDir):
    """
    修改html文件内容

    :param filePath: .html
    :return: None
    """
    if sys.platform == 'win32':
        template=template.replace('\\', '\\\\').replace('/','\\\\')
        log=log.replace('\\', '\\\\').replace('/','\\\\')

    with open(filePath, 'r', encoding='utf-8') as fr, open('%s.bak' % filePath, 'w', encoding='utf-8') as fw:
        for line in fr:
            line = line.lstrip()
            if line:
                line = line.replace(template, 'template')
                line = line.replace(log, 'log')
                fw.write(line)
    os.remove(filePath)
    os.rename('%s.bak' % filePath, filePath)

def _airtest_report(htmlName):
    """
    自定义airtest报告输出，需要传入报告html文件名称

    :param htmlName: airtest报告输出的html文件
    :return: None
    """
    htmlName = os.path.join(tempDir, htmlName)
    path, name = script_dir_name(caseFileName)
    rpt = LogToHtml(path, reportLogDir, static_root="static/", logfile=LOGFILE, script_name=name, )
    rpt.report(HTML_TPL, output_file=htmlName)


def _copy_static():
    for subdir in ["css", "fonts", "image", "js"]:
        copy_dir(os.path.join(STATIC_DIR, subdir), os.path.join(tempStaticDir, subdir))


def post_action(html_name):
    """
    将report 目录下的log文件生成 file.html 并复制log、static、template文件夹到temp目录下

    :param html_name: 由用例传入html名称
    :return: None
    """
    if not os.path.isdir(tempDir):
        os.makedirs(tempDir)
    _airtest_report(html_name)
    copy_dir(reportLogDir, tempLogDir)
    _copy_static()
    copy_dir(templateDir, tempTemplateDir)
    modify_file(os.path.join(tempDir, html_name))