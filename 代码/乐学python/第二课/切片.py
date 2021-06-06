s = '一帆风顺二龙腾飞三羊开泰四季平安五福临门'
print(s[-2:4:1])
print(s[2:8])
print(s[-6::-4])
print(s[-2::4])
print(s[0::4])
print(s[-7::4])
print(s[6:8])
print(s[0:4:1])


y = input("请输入你向说的话：")
s = y[-3::-1]
print(s)
s = '一帆风顺二龙腾飞三羊开泰四季平安五福临门'
print(s[-2:4:1])
print(s[2:8])
print(s[-6::-4])
print(s[-2::4])
print(s[0::4])
print(s[-7::4])

x = '我们是小米'
print(x[-2::2])
print(x[-2:5:4])
print(x[0:5])
print(x[-2:5:2])
print(x[-7::1])


y = '123456787'
s = y[-3::-1]
print(s)

y = input("请输入你向说的话：")
s = y[-3::-1]
print(s)


i = int(input('请输入数字1-7：'))
s = '赤橙黄绿青蓝紫'
c = s[i-1]
print('颜色代表为：',c)



def inputs():
    i = int(input('请输入数字1-7：'))
    s = '赤橙黄绿青蓝紫'[i-1]
    # print('代表的颜色是：',s)
    return s
t = inputs()
print(t)
