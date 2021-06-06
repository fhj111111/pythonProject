def func(a):
    '''
    实现a/的平方
    :return:
    '''
    return a * a


print(func(6))

# 匿名函数

a = lambda a: a * a

print(a(4))


def asd(a, *args):
    pass


def printinfo(arge, *arge2):
    print(arge)
    print(arge2)


if __name__ == '__main__':
    printinfo(5, 23, 5, 6, 5, 6, 5, 8)


def add(a,b):
    '''

    :param a: int或者str
    :param b: int或者str
    :return: c
    '''
    c = a+b
    return c
if __name__ == '__main__':

    print(add(55,45))

l = [1,2,3,4,5,6]
print(len(l))

list1 = list(range(1,101))
print(sum(l))
print(sum(list1))
print(len(list1))
