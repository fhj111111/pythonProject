import random

number = random.randint(0, 2)
print('随机数字值', number)

if number == 0:
    print('红灯，停')
else:
    if number == 1:
        print('绿灯，行')
    else:
        print('黄灯，请注意！')

sex = int(input('请输入你的年龄：'))
if sex <= 10:
    print('你还是小孩')
else:
    if sex <= 30 and sex >= 10:
        print('你是成年人了')
    elif sex <= 50 and sex >= 31:
        print('你是中年人了')
    else:
        print('你是老人了')
