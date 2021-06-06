# 评委打分，去掉最高和最低分，求剩下综合

def fun1(lst):
    lst.remove(max(lst))
    lst.remove(min(lst))
    return sum(lst)

score = [[6,7,8,9,2],[4,9,2,5,4],[9,2,6,5,1,8]]
for x in score:
    print('总分：{}'.format(fun1(x))) 


def fun2(lst):
    lst.remove(max(lst))
    lst.remove(min(lst))
    return sum(lst)

score1 = [[6,7,8,9,2],[4,9,2,5,4],[9,2,6,5,1,8]]
sum_score = 0
for i in score1:
    s = fun2(i)
    print('总分：{}'.format((s)))
    sum_score+=s
print(sum_score)