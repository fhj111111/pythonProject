import unittest
from common.HTMLTestrunner import HTMLTestRunner

caseath = "E:\\code\\ZDH\\case"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=caseath, pattern=rule)
print(discover)

repoerPath = 'E:\\code\\ZDH\\case' + 'report.html'
fp = open(repoerPath, 'wb')

runner = HTMLTestRunner(stream=fp,
                                       title='测试报告',
                                       description='Web 自动化')
runner.run(discover)
