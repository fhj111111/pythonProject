# from cofnfig.read_excel import ReadExcel
# from main  import RunMetdoh
# from cofnfig.excel_config import *
#
#
# class DependData:
#     def __init__(self,case_id=None):
#         self.case_id = case_id
#         self.opera_elcel = ReadExcel()
#     """
#     通过case_id 获取整行数据
#     """
#
#     def get_case_line_data(self):
#         rows_data = self.opera_elcel.get_rows_data(self.case_id)
#         return rows_data
#
#     # 执行依赖测试，获取结果
#     def run_dependenlt(self):
#         run_method = RunMetdoh()
#         # row_num = self.opera_elcel.get_row_num(self.case_id)
#         self.opera_elcel.get_row_num(self.case_id)
#         requset_data = get_data()
#         headers = get_headers()
#         method = get_method()
#         url = get_url()
#         res = run_method.run_main(method,url,requset_data,headers)
#         return res
#
#
#     # 根据依赖的key 去获取依赖测试case的响应，然后返回
#     def get_data_foe_key(self):
#         pass
# if __name__ == '__main__':
#     ddd = DependData()
#     ddd.run_dependenlt()