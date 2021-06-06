import random as suijishu


def sj():
    a = suijishu.randint(1, 100)
    b = suijishu.randint(1, 100)

    if a > b:
        print('%s > %s=' % (a, b), a + b)
    elif a < b:
        print('%s < %s=' % (a, b), a + b)
    elif a == b:
        print('%s = %s=' % (a, b), a + b)


print(sj())
sj()
sj()

import time as t

print(t.asctime())
print(t.asctime())

import sys


# a = sys.stdin.readline()
# print(a)

def compaer():
    age = int(input('请输入你的年龄：'))
    if age >= 30:
        print('腊肉+1')
    else:
        print('小鲜肉+1')


compaer()
compaer()
compaer()


#
# def compaer():
#     age = int(sys.stdin.readline())
#     if age >= 30:
#         print('腊肉')
#     else:
#         print('小鲜肉')
#
#
# compaer()
# compaer()
# compaer()


def list1():
    return list(range(1, 101))


print(list1())


def chujiu():
    a = 0
    for i in range(1, 101):
        if i % 9 == 0:
            print('第%s次被九整除的数字是%s' % (a, i))
            a += 1


chujiu()


def moon_weigth(now_weight, add_weigth,year):
    print('您今年的体重是多少kg:%s' % round(now_weight * 0.165, 2))
    for i in range(1, year):
        print('你第%s年体重是%s kg' % (i + 1, int(0.165 * (now_weight + i * add_weigth))))


while True:
    a = int(input('now_weight:'))
    b = int(input('add_weight:'))
    c = int(input('期待计算的年龄：'))
    if a == -1 or b == -1:
        print('结束测量')
        break
    moon_weigth(a, b,c)


print(round(13.2280,2))




def jiafa(c,d):
    a=1
    for i in range(c,d):
        a = a+i
    print('总和是:%s'%a)

#
#
# while True:
#     a = int(input('请输入第1个数字：'))
#     b = int(input('请输入第2个数字：'))
#     if a == -1 or b == -1:
#         print('游戏结束！')
#     else:
#         jiafa(a,b)




def zhnegchu(a,b,c):
    s=1
    for i in range(a,b):
        if i % c == 0:
            print('第%s次，被%s整除的数字是：'%(s,c),i)
            s+=1


while True:
    a = int(input('请输入开始的数字：'))
    b = int(input('请输入结束的数字：'))
    c = int(input('请输入整除的数字：'))
    if a == -1 or b == -1 or c ==-1:
        print('游戏结束啦~~~~')
        break
    else:
        zhnegchu(a,b,c)