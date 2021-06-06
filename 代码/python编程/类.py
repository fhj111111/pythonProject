# class shengwu:
#     pass
#
#
# class dongwu(shengwu):
#     pass
#
#
# class jizhui(dongwu):

class dome():
    def print1():
        print('hello ')

    def print2():
        print('word')


dome.print1()
dome.print2()


class dongwu:
    def xingzou(self):
        print('行走')

    def huxi(self):
        print('呼吸')

    def chifan(self):
        print('吃饭')


class jizhuidongwu(dongwu):
    def youjizhui(self):
        print('有脊椎动物')

    def wujizui(self):
        print('无脊椎动物')


class purudongwu(jizhuidongwu):
    def weinai(self):
        print('喂奶')


class heixingxing(purudongwu):
    def zhilixingzou(self):
        print('直立行走')

    def shiyonggongju(self):
        print('使用工具')
        self.youjizhui()
        self.weinai()

    def test(self,name,age):
        print('%s is %s year old'%(name,age))

leo = heixingxing()
nancy = heixingxing()
print('_____________________________')
leo.shiyonggongju()
print('______________________________')
leo.zhilixingzou()
nancy.weinai()
leo.chifan()
nancy.xingzou()
leo.test('loe',22)



class test1:
    def print1(self,name):
        print(name)


class test2:
    def peint2(self,age):
        print(age)

leo1 = test1()
leo2 = test2()
leo1.print1('wang')
leo2.peint2(32)




class self_test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print('a+b=',self.a+self.b)

    def chengfa(self):
        print('a*b=')
        return self.a * self.b

if __name__ == '__main__':
    leo = self_test(3,5)
    print(leo)
    print(leo.chengfa())


class SelfTest:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def count(self):
        print('a+b=', self.a + self.b)

    def minus(self):
        print('a-b=', self.a - self.b)

    def show(self):
        self.minus()
        self.count()


leo = SelfTest(3, 5)
leo.count()
leo.minus()
leo.show()



class test1:
    def move(self):
        print('move!')

class test2(test1):
    def dance(self):
        print('dance')

class test3(test2):
    def sing(self):
        self.move()
        self.dance()
        print('大家嗨起来！！！')


leo = test3()
print(leo.sing())



class a1:
    def jiafa(self):
        print('wo甲A')

    def jianfa(self):
        print('jianfa')

    def changfa(self):
        print('chengfa')
    def show(self):
        self.jiafa()
        self.jianfa()
        self.changfa()
        print('______________________')
leo= a1()
leo.show()



class a1:
    def jiafa(self):
        print('wo甲A')


class a2(a1):
    def jianfa(self):
        print('jianfa')

class a3(a2):
    def changfa(self):
        print('chengfa')

class a4(a3):
    def show(self):
        self.jiafa()
        self.jianfa()
        self.changfa()
        print('______________________')

leo = a4()
leo.show()