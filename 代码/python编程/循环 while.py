a = 0
while True:
    if a > 10:
        print('that\'s all for today')
        break
    print(a, ',', end='')
    a += 1

a = 1
for i in range(1, 101):
    a = a + i
print('the is sun:%s' % a)

a = 1
for i in range(1, 101):
    if i % 9 == 0:
        print('第%s 次，被9整数的数字是:' % a, i)
        a += 1

a = 0
b = 1
while b <= 100:
    a = a + b
    b += 1
print('the is sum:%s' % a)

suzi = 0
for i in range(1, 101):
    suzi = suzi + i
print(suzi)

import random as cia
# while True:
#     sum = cia.randint(1,100)
#     shuru = int(input('请输入你的数字：'))
#     if shuru == sum:
#         print('你真棒~')
#         break
#     elif shuru > sum:
#         print("大了，请往小的猜")
#     elif shuru < sum:
#         print("小了，王大的猜")
#
#
s = 0
for i in range(1, 101):
    s += i
print(s)

a = 0
for i in range(1, 101):
    if i % 5 == 0:
        print('第%s 个被5整数的数字：' % a, i)
        a += 1

s = 0
for i in range(1, 11):
    s += i
print(s)

#
# import random as rd
# shuzi = rd.randint(1,100)
# while True:
#
#     sr = int(input('请输入你的数字：'))
#     if sr == shuzi:
#         print('你好棒~')
#         break
#     elif sr > shuzi:
#         print('大了，请往小的猜')
#     elif sr < shuzi:
#         print('小了，请往大的猜测')

s = 0
for i in range(1, 101):
    s += i
print(s)

a = 0
for i in range(1, 101):
    if i % 10 == 0:
        print('第%s次打印，能整数10的数字是：' % a, i)
        a += 1

y = 1
x = 1
while y <= 30 and x <= 30:
    a = y + cia.randint(-20, 20)
    b = x + cia.randint(-20, 20)
    print(a, '', b, '', end='')
    y += 1
    x += 1

