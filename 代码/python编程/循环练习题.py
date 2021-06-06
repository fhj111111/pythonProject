for x in range(0, 20):
    print('hello_%s' % x)
    if x > 9:
        break

#
#
# xz = int(input('您现在的体重是多少KG：'))
# plus = int(input('您预计每年增加多少KG'))
# print('您现在在月球的体重是:',xz*0.165)
# for year in range(1,11):
#     print('您第%s年在月球的体重是：'%year,int((xz+plus*year)*0.165))
#


# age = input('请输入你的年龄：')
#
# while age != 'exit':
#     if int(age) % 2 == 0:
#         for a in range(0, int(age)):
#             if a % 2 == 0:
#                 print(a, ',', end='')
#     elif int(age) % 2 != 0:
#         for a in range(0, int(age)):
#             if a % 2 != 0:
#                 print(a, ',', end='')
#
#     age = input('\n请输入你的年龄：')


ast = input('输入你的年龄：')
while ast != 'exit':
    if int(ast) % 2 == 0:
        for a in range(0, int(ast)):
            if a % 2 == 0:
                print(a, ',', end='')
    elif int(ast) % 2 != 0:
        for a in range(0, int(ast)):
            if a % 2 != 0:
                print(a, ',', end='')
    a = input('\n输入你的年龄：')


# age = input('请输入你的年龄：')
#
# while age != 'exit':
#     if int(age) % 2 == 0:
#         for a in range(0, int(age)):
#             if a % 2 == 0:
#                 print(a, ',', end='')
#     elif int(age) % 2 != 0:
#         for a in range(0, int(age)):
#             if a % 2 != 0:
#                 print(a, ',', end='')
#     age = input('\n请输入你的年龄：')
