# list  列表[1,2,3,4,5,5]
# tuple 元组(1,2,3,4,5,6)
# dict  字典{'1':'value'}


t3 = 123,456
print(t3)

a = [1,2,3,4,5,6,7,8,9]
print(a)
b = [10,11]
print(a+b)
print(b*2)
print(len(b))
print(a[2:])
a.append(10)
a.pop(5)
print(a)
a.append([5,'6'])
print(a)
a.insert(5,'6')
print(a)
# for i in a:
#     print(i)

# for i in a[1:3]:
#     print(i)
#
# print(2 in a )