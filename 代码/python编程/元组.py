tuple1 = (1, 2, 3, 'leo', True)
print(tuple1)

print(tuple1[1])
tuple2 = 4, 5, 6, False
print(tuple2)

print(type(tuple1))

tuple3 = 1, 2, 3, 4, 6
print(tuple3)
t = tuple3[:4] + (5,) + tuple3[4:]
print(t)

"实验"
#
s = 1, 2, 3, 4, 5, 7
print(s)
print(s[:5] + (6,) + s[5:])

a = 1, 2, 3, 4, 4, 5
print(a[:4] + a[5:])

a = 1, 2, 3, 5, 6
print(a[:3] + (4,) + a[3:] + (7,))

s = 1, 2, 3, 4, 4, 5
print(s[0:3] + s[4:])

print(a+s)