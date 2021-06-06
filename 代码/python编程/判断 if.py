# arge = 33
# if arge > 30:
#     print('称为腊肉')
#
# if arge>30:
#     print('称为腊肉呀~')
#     print('too old')
#
# a = int(input('来个数字吧：'))
# print(type(a))

#
# while True:
#     s = int(input('输入我的数字：'))
#     if s == 6:
#         print('is to happy')
#     else:
#         print('No~')
#         break
#
# s = int(input('输入要发送的金额吧：'))
# if s < 200:
#     print('可以发送红包发送成功~')
# if s > 200:
#     print('金额过大，发送金额不超过200！')
# if s == 200:
#     print('yea！,大红包哟~')

#
# while True:
#     a = input('输入你的分数：')
#     if a == 'exit':
#         print('结束查询')
#         break
#     elif int(a) >= 90 and int(a) <= 100:
#         print('优秀哟~')
#     elif int(a) >= 60 and int(a) <= 89:
#         print('良好')
#     elif int(a) < 60 and int(a) >= 0:
#         print('不及格！')
#     else:
#         print('输错了吧')
#
#
# while True:
#     a = input('输入你的分数：')
#     if a == 'exit':
#         print('结束查询')
#         break
#     elif float(a) >= 90 and float(a) <= 100:
#         print('优秀哟~')
#     elif float(a) >= 60 and float(a) <= 89:
#         print('良好')
#     elif float(a) < 60 and float(a) >= 0:
#         print('不及格！')
#     else:
#         print('输错了吧')
#
#
money = 100
if money > 500:
    print('...')
else:
    print('so poor~')
    print('you need to work harder')

# import random as suijishu
#
# result = suijishu.randint(1, 100)
# times = 1
# print('我现在有了1-100的随机数你能猜到是多少吗？ ')
# while True:
#     strl = '你知道这个数字是多少吗？请输入%s 次数猜测:'
#     guwss = int(input(strl % times))
#     times += 1
#     if guwss == result:
#         print('终于猜对了~')
#         break
#     elif guwss > result:
#         print('大了，请往小了猜')
#     elif guwss < result:
#         print('小了，请往大了猜')
#     else:
#         print('1-100 的数字')

import random as suzi
result1 = suzi.randint(1,50)
str1 = 1
while True:
    s = '我们开始猜数字游戏吧，请输入你%s次数字：'
    gus = int(input(s%str1))
    str1+=1
    if gus == result1:
        print('你真棒~')
        break
    elif gus > result1:
        print('猜大了，请往小的猜')
    elif gus < result1:
        print('猜小了，请往大的猜')
    else:
        print('请输入1-50之间的数字')