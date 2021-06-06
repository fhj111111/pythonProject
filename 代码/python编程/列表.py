list1 = [1, 2, 3, 4, 'leo', True]

print(list1)
print(list1[1])
print(list1[5])
list1.append(99)
list1[3] = 'nicy'
print(list1)
list2 = [1, 2, 3]
list3 = ['a', 'b', 'c']
he = list2 + list3
print(he)

print(list1[4]+list3[2])

list1 = [1,2,3,4,5,7]
list1.insert(5,6)
print(list1)

del list1[3]
print(list1)
list1.insert(3,4)
print(list1)
for i in list1:
    print(i)

a = [1, 2, 3, 4, 5, 7]
a.insert(5, 6)
print(a)

a.append(9)
print(a)



del a[7:]
print(a)
