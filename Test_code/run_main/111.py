from cofnfig.excel_config import *
from cofnfig.read_excel import ReadExcel
from cofnfig.method import RunMetdoh
from cofnfig.common import commonUtil


class RunTest():
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
            xie_ru_data = self.reade.get_cell_value(i, get_assert_suss())
            if methdo == 'post':
                res = self.run.run_main(methdo, url, data)
                # print(res)
                if self.com_util.is_contain(asserts, res):
                    self.reade.write_value(i,get_assert_suss(),'pass')
                else:
                    self.reade.write_value(i,get_assert_suss(),res)
            else:
                res = self.run.run_main(methdo, url, headres)
                # print(res)
                if self.com_util.is_contain(asserts, res):
                    self.reade.write_value(i, get_assert_suss(), 'pass')
                else:
                    self.reade.write_value(i, get_assert_suss(), res)


if __name__ == '__main__':
    ru = RunTest()
    ru.gou_run()
