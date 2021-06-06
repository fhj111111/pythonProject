import xlrd

book = xlrd.open_workbook('income.xlsx')
# print(f'包含表单数量,{book.nsheets}') # 获取多少个表单数
# print(f'表单的名字分别为：,{book.sheet_names()}') # 获取表单名字
#
#
# # book1 = xlrd.open_workbook('接口用例.xlsx')
# # print(book1.nsheets)
# # print(book1.sheet_names())
#
# # 索引获取第一个表单
# sheet = book.sheet_by_index(0)
#
# print(sheet.nrows)   #获取多少行数
# print(f'表单索引：{sheet.number}') #
# print(f'表单索引：{sheet.nrows}') #行数
# print(f'表单索引：{sheet.ncols}') #列数
#
#
# print(f'单元个A1的内容是：{int(sheet.cell_value(rowx=4,colx=1))}')
#
# print(f'第一行内容是：{(sheet.row_values(rowx=2))}')



sheet1 = book.sheet_by_name('2017')

incomes = sheet1.col_values(colx=1,start_rowx=1)

# print(f'2017年收入为：{int(incomes)}')
print(f"2017年收入为: {sum(incomes)}")
