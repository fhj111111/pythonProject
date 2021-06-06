import unittest, time
from data import HTMLTestRunner


def run_all():
    case_path = "./case"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(case_path, "test_*.py")
    now = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
    test = "./report/" + now + "_report.html"
    with open(test, "wb") as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="自动化测试报告", description="登录功能测试")
        runner.run(discover)
# if __name__ == '__main__':
#
#     run_all()


# import unittest
# if __name__ == '__main__':
#     # 测试用例保存的目录
#     case_dirs = "../case"
#     # 加载测试用例
#     discover = unittest.defaultTestLoader.discover(case_dirs, "test_*.py")
#     # 运行测试用例
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(discover)