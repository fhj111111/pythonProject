# 温度转换程序
for i in range(3):
    var = input('请输入待温度表示符号的温度值（例如：32C）：')

    if var[-1] in ['C', 'c']:
        f = 1.8 * float(var[0:-1]) + 32
        print('转换后的温度为：%.2fF' % f)
    elif var[-1] in ['F', 'f']:
        c = (float(var[0:-1]) - 32) / 1.8
        print('转换后的温度为：%.2fC' % c)

    else:
        print('输入 有误')
#
# for i in range(3):
#     lst = input('请输入温度表符号温度值（如：32c)：')
#     if lst [-1] in ['C','c']:
#         f = 1.8 * float(lst[0:-1]) + 32
#         print('转换后的温度为：%.2fF'%f)
#     elif lst [-1] in ['F','f']:
#         c = (float(lst[0:-1]) - 32)/1.8
#         print('转换后的温度为%.2Fc'%c)
#     else:
#         print('输入错误')
# print(1.8*33.2+32)
#
# num1 = input('The first number is:')
# num2 = input('The second number is:')
# avg_num = (float(num1)+float(num2)) / 2
# print('平均数是%s'%avg_num)