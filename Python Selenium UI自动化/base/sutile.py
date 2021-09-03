import unittest,time
from data import HTMLTestrunner

def run_all():
    case_path = "./case"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(case_path, "test_*.py")
    now = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
    test = "./report/" + now + "_report.html"
    with open(test, "wb") as report_file:
        runner = HTMLTestrunner.HTMLTestRunner(stream=report_file,
                                               title="UI 自动化测试报告",
                                               description="web-flash后台管理",
                                               )
        runner.run(discover)
if __name__ == '__main__':

    run_all()
