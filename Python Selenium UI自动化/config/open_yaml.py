import yaml


class open_yaml:
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = '../data/login.yaml'
        self.data = self.open_data()

    def open_data(self):
        with open("../data/login.yaml", "r", encoding='UTF-8') as yaml_file:
            self.data = yaml.load(yaml_file.read(),Loader=yaml.FullLoader)
            return self.data

if __name__ == '__main__':
    tt = open_yaml()
    print(tt.open_data()['login']['username']['type'])