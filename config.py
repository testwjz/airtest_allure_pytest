import os

from airtest.report.report import LOGFILE

configFile = __file__
configDir = os.path.dirname(configFile)

# airtest报告中途备份
tempDir = os.path.join(configDir, 'temp')
tempLogDir = os.path.join(tempDir, 'log')
tempStaticDir = os.path.join(tempDir, 'static')
tempTemplateDir = os.path.join(tempDir, 'template')

# airtest日志路径
reportDir = os.path.join(configDir, 'report')
reportLogDir = os.path.join(reportDir, 'log')
reportLogFile=os.path.join(reportLogDir, LOGFILE)

# allure结果路径
allureResult = os.path.join(configDir, 'allureResult')
allureReport = os.path.join(configDir, 'allure-report')

# 执行前需要删除的文件夹
listDeleteDir = [reportDir, tempDir, allureResult, allureReport]
