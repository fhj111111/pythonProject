import random
s = int(input('请输入你的数字：'))
i = 1
while i < s:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    print(str(a) + '+' + str(b) + '=')
    i += 1

t = 1
while t < 3:
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(str(a)+'+'+str(b)+'=')
    t += 1

import random
a = int(input('请输入数字，即将随机出题：'))
b = 1
while b < a:
    c = random.randint(1,15)
    d = random.randint(1,15)
    print(str(c)+'+'+str(d)+'=')
    b += 1