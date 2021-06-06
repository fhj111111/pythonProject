from 第七课.函数返回值 import fun2

score1 = [[6, 7, 8, 9, 2], [4, 9, 2, 5, 4], [9, 2, 6, 5, 1, 8]]
sum_sorent = 0
for x in score1:
    s = fun2(x)
    print('分数是{}'.format(s))
    sum_sorent += s
print('总数是：', sum_sorent)

