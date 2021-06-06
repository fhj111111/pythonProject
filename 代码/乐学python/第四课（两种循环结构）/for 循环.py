import random

s = int(input('请输入题数：'))
for i in range(1, s + 1, 1):  # 生成1到s+1步长为1的
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(str(i) + '.' + str(a) + '+' + str(b) + '=')
