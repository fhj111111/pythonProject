import yaml

class OpenYaml:

    def __init__(self,file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = './data/page_data.yaml'
        self.data = self.getdata()

    def getdata(self):
        # 读取yaml的值
        with open(self.file_name,'r',encoding='utf-8') as f:
            self.data = yaml.load(f,Loader=yaml.FullLoader)
            return self.data
        # self.yamlindex = open(self.file_name,'r',encoding='utf-8')
        # # 把文件内容读取出来
        # self.data = yaml.load()
        # # print(self.data['login']['username']['type'])
        # return self.data
if __name__ == '__main__':

    tt  = OpenYaml()
    print(tt.getdata()['login']['username']['type'])