list1 = list(range(1, 101))
print(list1)

tuple1 = tuple(range(1, 11))
print(tuple1)


# '''
# 函数有个名字==函数的名字
# 函数有个参数==工具
# 函数体=成品
# '''


def sayhello(yourname):
    print('hello:', yourname)


print(sayhello('you'))


def aa(youname, friename):
    print('hello:%s&%s' % (youname, friename))


print(aa('nacy', 'int(666'))

list1 = list(range(1, 11))
print(list1)


def you(name):
    print('hello_%s' % name)


print(you('li'))


def na(name1, name2):
    print('hello_%s&%s' % (name1, name2))


print(na('nacy', 'zhang'))


#
# def add (a,b):
#     print('how much is %s plus %s'%(a,b),a+b)
#
# a = int(input('请输入加数：'))
# b = int(input('请输入被加数'))
# print(add(a,b))


# def add(a, b):
#     return a + b
#

# while True:
#     a = int(input('请输入加数：'))
#     b = int(input('请输入被加数'))
#     print('第一个数字是%s,第二个数字是%s' % (a, b), add(a, b))


def compare(a, b):
    if a > b:
        return print(a, '>', b)
    elif a < b:
        return print(a, '<', b)
    else:
        return print(a, '=', b)


print(compare(1, 2))
print(compare(3, 3))
print(compare(2, 1))


def chengfa():
    a = 13
    b = 15
    print('%s * %s=' % (a, b), a * b)


chengfa()
print(chengfa())

a = 13
b = 15


def cf(c1, c2):
    return c1 * c2


print('1', cf(a, b))


# def leijia(s):
#     number = 0
#     for i in range(1, s + 1):
#         number += i
#     return print('result is', number)
#
#
# while True:
#     a = input('尾数：')
#     if a == 'exit':
#         break
#     else:
#         leijia(int(a))
# leijia(5)



#
# def shu(a,b):
#     s = 0
#     for i in range(a,b):
#         s+=i
#     print('sum:',s)
#
# shu(int(0),int(101))
#
#
# def leijia(s):
#     number = 0
#     for i in range(1,s+1):
#         number+=i
#     return print('result is',number)
#
# while True:
#     a = input('尾数：')
#     if a == 'exit':
#         break
#     else:
#         leijia(int(a))
# leijia(a)
#



def sum (s):
    number = 0
    for i in range(1,s+1):
        number +=i
    return print('总和是：',number)

while True:
    a = input('请输入数字：')
    if a == 'exit':
        break
    else:
        sum(int(a))

sum(22)