foods_list = ['nike', 'mango', 'beer']
sports_list = ['football', 'swimming']
print('my favorite foods:\n', foods_list)

print(100 * 4 + 45 * 2 + 50 * 4 + 100 * 4)

str_name = 'leo'
str_hello = 'hello %s'
print(str_hello % str_name)

shop = {'kele': 4, 'hanbao': 6.5, 'regou': 3.5, 'pisa': 16}
a = int(input('kele:'))
b = int(input('hanbao:'))
c = int(input('regou:'))
d = int(input('pisa:'))
total_price = a * shop['kele'] + b * shop['hanbao'] + c * shop['regou'] + d * shop['pisa']
hint = '总金额是 %s 园'
print(hint % total_price)

s = {'ping': 3.2, 'ju': 5, 'xi': 4}
a = int(input('ping:'))
b = int(input('ju:'))
c = int(input('xi:'))

sum1 = a*s['ping']+b*s['ju']+c*s['xi']
f = '您的总金额是%s 元'
print(f%sum1)


list1 = [1, 2, 3, 4, 5, 7]
list1.append(9)
print(list1)
list1.insert(5, 6)
print(list1)
del list1[-1]
print(list1)

tuple1 = 1, 2, 3, 4, 6, 8
print(tuple1)
print(tuple1[:4]+(5,)+tuple1[4:5]+(7,)+tuple1[5:])
print(tuple1[:5]+(7,)+tuple1[6:])

dicet1 = {'zhang':177,'wang':170,'liu':168}
print(dicet1)
dicet1['zhang']=166
print(dicet1)
dicet1['liu']=122
print(dicet1)
del dicet1['wang']
print(dicet1)