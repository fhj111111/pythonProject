n = int(input('请输入一个整数：'))
for i in  range(2,n):
    if n % i == 0:
        print(str(n)+'不是一个素数')
        break
else:
    print(str(n)+'是一个素数')