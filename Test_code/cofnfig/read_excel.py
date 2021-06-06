import xlrd
from xlutils.copy import copy
import json
import openpyxl


class ReadExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../data/test_case .xls'
            self.sheet_id = 0
        self.data = self.read()

    def read(self):
        workbook = xlrd.open_workbook(self.file_name)
        data = workbook.sheets()[self.sheet_id]
        return data

    def get_hang(self):  # 获取行数

        return self.data.nrows

    def get_lie(self):
        # 获取列数

        return self.data.ncols

    def get_cell_value(self, cc, oo):
        # 获取某个单元格
        data = self.data.cell_value(cc, oo)
        return data

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)
    #
    # # 根据对于case_id 找到对应行内容
    # def get_rows_data(self, case_id):
    #     row_num = self.get_row_num(case_id)
    #     rows_data = self.get_row_values(row_num)
    #     return rows_data
    #
    # #  根据对于case_id 找到对应行号
    # def get_row_num(self, case_id):
    #     num = 0
    #     cols_data = self.get_cols_data()
    #     for col_data in cols_data:
    #         if case_id in col_data:
    #             return num
    #         num += 1
    #
    # # 根据行号，找到该行内容
    # def get_row_values(self, row):
    #     tables = self.data
    #     row_data = tables.row_values(row)
    #     return row_data
    #
    # # 获取莫一列的内容
    # def get_cols_data(self, col_id=None):
    #     if col_id != None:
    #         cols = self.data.col_values(col_id)
    #     else:
    #         cols = self.data.col_values(0)
    #     return cols


if __name__ == '__main__':
    op = ReadExcel()
    print(op.get_lie())
    print(op.get_hang())
    print(op.get_cell_value(2, 4))
    # print(op.write_value(12, 3, 'test_data'))
    print(op.get_cell_value(12, 3))
