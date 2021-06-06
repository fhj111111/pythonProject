for i in range(1, 10 + 1):
    if i % 3 == 0:
        break
    print(i, end=',')

for i in range(1, 10 + 1):
    if i % 2 == 0:
        continue
    print(i, end=',')


for i in range(100,1000):
    a = i // 100
    b = i % 100 // 10
    c = i % 10
    if a ** 3+ b**3+c**3 != i:
        continue
    print(i)