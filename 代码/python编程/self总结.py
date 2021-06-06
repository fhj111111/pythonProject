class test1:
    def print1(self):
        print('a+b=', self.a + self.b)


class test2(test1):
    def print2(self, a, b):
        self.a = a
        self.b = b
        self.print1()


leo = test2()
leo.print2(3, 6)



class juxing:

    def rount(self,a,b):
        self.a = a
        self.b = b
        print('rount is ',2*(self.a + self.b))

    def area(self):

        print('area is:',self.a + self.b)

leo = juxing()
leo.rount(3,6)
leo.area()



class juxing:
    def count(self,a,b):
        self.a = a
        self.b = b
        self.area_round()

    def area_round(self):
        print('count is ',self.a + self.b)
        print('area is ',2*(self.a+self.b))

leo = juxing()
leo.count(6,88)

#
#
# while True:
#     a = int(input('请输入第1个数字：'))
#     b = int(input('请输入第2个数字：'))
#     if a == '999' or b == '999':
#         break
#     while True:
#         c = int(input('1 = 加法，2 = 减法，3=乘法，4=除法，5=退出！'))
#         if c == 1:
#             print('a+b=',a+b)
#         elif c == 2:
#             print('a-b=',a-b)
#         elif c == 3:
#             print('a*b=',a*b)
#         elif c == 4:
#             print('a/b=', a / b)
#         else:
#             break
#     break
#
#
#
i = 0
list1 = []
while True:
    a = input('请输入你要添加的数字，如果输入“exit”则退出输入：')
    if a == 'exit':
        break
    else:
        list1.insert(i,int(a))
        i+=1

print('您输入的数字是：%s'%list1)
print('您输入的总和是：%s'%sum(list1))
print('您输入的最大是：%s'%max(list1))
print('您输入的最小是：%s'%min(list1))



import requests

# 模拟请求get测试
