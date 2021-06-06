import yaml
import os


class OpenYaml:

    def __init__(self,file_name=None):
        self.file_name = file_name
        if file_name:
            self.file_name = self.file_name
        else:
            self.file_name = '../config/eles.yaml'

        self.data = self.read_yaml()

    def read_yaml(self):
        with open(self.file_name) as f:
            self.data = yaml.load(f,Loader=yaml.CLoader)
            # print(self.data['login']['user']['ele'])
            return self.data


if __name__ == '__main__':
    ya = OpenYaml()
    print(ya.read_yaml()['login']['user']['ele'])