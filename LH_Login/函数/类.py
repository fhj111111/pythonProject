def chiguitou(a = 'Gou'):
    print('%s 在吃骨头'%a)



class Gou(object):

    def chigutou(self):

        print('出骨头')

    def huijiao(self):
        self.chigutou()
        print('会叫')

if __name__ == '__main__':

    gou = Gou() # 实例化
    gou.huijiao()
    gou.chigutou()
    chiguitou()


class Count():

    def __init__(self,a,b):
        self.a = a
        self.b = b