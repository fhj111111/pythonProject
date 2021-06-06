from cofnfig.excel_config import *
from cofnfig.read_excel import ReadExcel
from cofnfig.method import RunMetdoh
from cofnfig.common import commonUtil
import requests
import json


class RunTest:
    def __init__(self):
        self.config = configs()
        self.reade = ReadExcel()
        self.run = RunMetdoh()
        self.com_util = commonUtil()

    def gou_run(self):
        hang = self.reade.get_hang()
        for i in range(1, hang):
            url = self.reade.get_cell_value(i, get_url())
            methdo = self.reade.get_cell_value(i, get_method())
            headres = eval(self.reade.get_cell_value(i, get_headers()))
            data = eval(self.reade.get_cell_value(i, get_data()))
            asserts = self.reade.get_cell_value(i, get_assert())
            if methdo == 'post':
                res = self.run.run_main(methdo,url,data)
                print(res)
            else:
                res = self.run.run_main(methdo,url,headres,data)
                print(res)
if __name__ == '__main__':
    ru = RunTest()
    ru.gou_run()
