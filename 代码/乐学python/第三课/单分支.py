import random

# 0 代表红灯！ 1 代表绿灯！ 2 是黄灯
# 单分支
sig = random.randint(0, 1)
print('现在是：', sig)
if sig == 0:
    print('红灯，停')

# 双分支

number = random.randint(0, 2)
print('现在是：', number)
if number == 0:
    print('红灯，停')
else:
    print('绿灯，行')

# 多分支
deng = random.randint(0, 3)
print('现在是：', deng)
if deng == 0:
    print('红灯，停')
elif deng == 1:
    print('绿灯，行')
else:
    print('黄灯，请注意')

str = int(input('请输入你的数字：'))
print('你的数字是：', str)
if str <= 10:
    print('你还是小屁孩')
elif str >= 10 and str <= 30:
    print('你是成年人了')
elif str >= 30 and str >= 60:
    print('你已经老了')
else:
    print('你是老年人了')
