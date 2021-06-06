print ('Hello world Python!')


message = 'hello world pyThon!'
print(message)


"""
方法：
title（）——首字母大写
upper（）——全大写
lower（）——全小写
变量的后面使用方法，每个方法后面接着圆括号
"""

print(message.title())
print(message.upper())
print(message.lower())


# 在字符串中使用变量

first_name = 'ada'
last_name = 'lovelace'

print(first_name,last_name)
print(first_name+last_name)
full_name = f'{first_name} {last_name}'
print(full_name)



# x = int(input('请输入鱼香茄子的价格：'))
# y = int(input('请输入宫保鸡丁的价格：'))
# s = (x + y) / 2
# print('两个菜的相差金额是：',x-y)
# print('两个菜品平均值是：%s' %s)


s = int(5*2+(10/3)*2)
m5 = s//5
m1 = s%5
print('水果总金额是%s 元,5元人民币%s 张,1元人民币%s 张'%(s,m5,m1))




dict_menu = {'汉堡':15,'鸡翅':21,'薯条':6,'骨肉相连':15,'披萨':20,}

print(dict_menu)

for i in dict_menu.keys():
    print(i)

for i in dict_menu.values():
    print(i)

x = 0
for p in dict_menu.values():
    # x+=p
    x = x + p
print('平均价格：',x/len(dict_menu))

for k,v in dict_menu.items():
    if v > 20:
        print(k,v)


dict_tity = {
    '张三丰':['北京','上海'],
    '李四':['广州','兰州','深圳','西安'],
    '莫容夫':['上海','兰州','河南']
}

for k,v in dict_tity.items():
    print(k,v)
    if '上海' in v:
        print(k)
