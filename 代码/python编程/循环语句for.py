# import random as shuzi
#
# ste = 1
# while True:
#     suiji = shuzi.randint(1,100)
#     a = '请输入你的数字%s 次：'
#     gu = int(input(a%ste))
#     ste += 1
#     if gu == suiji:
#         print('真棒~')
#         break
#     elif gu > suiji:
#         print('dale,')
#     elif gu < suiji:
#         print('xiaole')
#     else:
#         print('1-20zhijian')
#
#
# suiji = shuzi.randint(1, 20)
#
# list1 = ['hello', True, 12, 3.1]
# tuple1 = 1, 2, 3, 4, 5, 6
# a = 1
# for i in list1:
#     print('打印第%s次' % a, i)
#     a += 1
#
# for i in range(1, 2):
#     print('hello')
#
# tuple1 = 1, 2, 3, 4, 5, 6
# s = 1
# for i in tuple1:
#     print('第%s 次打印' % s, i)
#     s += 1
#
# dict1 = {'zhang': 32, 'liu': 22, 'li': 18}
# d = 1
# for i in dict1:
#     print('这是第%s次打印' % d, dict1)
#     # print(dict1['li'])
#     d += 1

# for i in range(1, 11):
#     print('第%s轮输出：' % i)
#     for s in range(1, 4):
#         print(s)
#
# list1 = ['hello', True, 12, 3.1]
# for i in list1:
#     print(i)
#     for s in list1:
#         print(s)

a = 0
for i in range(1, 101):
    a = a + i
print('the result :%s' % a)

s = 0
for i in range(1, 101):
    s = s + i
print('you %s' % s)



a = 1
for i in range(1,101):
    if i % 3 == 0:
        print('第%s个能被3整除的数字是：'%a,i)
        a+=1

t = 1
for i in range(1,101):
    if i % 9 == 0:
        print('第%s个能被9整除的数字是：' % t, i)
        t+=1

import random as shuzi
q = 1
while True:
    shuzi1 = shuzi.randint(1,10)
    title = '请输入你要猜的数字吧~这是你第%s次输入：'
    st = int(input(title%q))
    q+=1
    if st == shuzi1:
        print('你真棒~')
        break
    elif st > shuzi1:
        print('大了。往小了猜测')
    elif st < shuzi1:
        print('小了。往大了猜测')
