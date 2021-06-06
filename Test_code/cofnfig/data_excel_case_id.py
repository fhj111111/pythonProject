from cofnfig.read_excel import ReadExcel
from cofnfig.excel_config import *

class read_excel_data:

    def __init__(self):
        self.read = ReadExcel()


    def get_hang(self):
        self.read.get_hang()

    def urls(self,row):
        col = get_url()
        self.read.get_cell_value(row,col)

    def is_zhixing(self,row):
        col = get_is_run()
        self.read.get_cell_value(row,col)

if __name__ == '__main__':
    ls =read_excel_data()
    ls.is_zhixing(2)
