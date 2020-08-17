# -*- coding：utf-8 -*-
import os
import sys


from case import copy_dir, rmdir
from config import tempDir, allureResult, allureReport, listDeleteDir

base_dir = os.path.dirname(__file__)


def init_main():
    for dirName in listDeleteDir:
        rmdir(dirName)


def post_main():
    # 执行完成后生成allure报告
    os.system('allure generate -c {0}'.format(allureResult))
    copy_dir(tempDir, allureReport)


def main(case):
    init_main()
    try:
        os.system(r'pytest --alluredir={} {}'.format(allureResult, case))
    except Exception as e:
        sys.exit(1)
    post_main()


if __name__ == '__main__':
    casepath = os.path.join(base_dir, 'case', 'home')
    main(casepath)
