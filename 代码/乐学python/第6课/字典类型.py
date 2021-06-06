native = {'江苏':2,'山东':6,'南京':7,'广州':1}

print(native) # 查询
native['上海']=102 # 添加
print(native)
native['上海']=1 # 修改
print(native)
del native['上海']   # 删除
print(native)

print('上海' in native) # 有显示True 否则 False
print(native.get('上海','没有这个地方的人'))

for k in native.keys(): # 遍历键
    print(k)

for k in native.values(): # 遍历值
    print(k)

for i in native.items(): # 遍历键值对
    print(i)



# for item in native.items():
#     if item[1]>5:
#         print('5个以上人员有：',item[0])


for k,v in native.items():
    if v>5:
        print('5个以上人员有：', k[0:2])


dict_city = {'张三丰':['北京','上海'],
             '李莫愁':['广州','成都','兰州'],
             '慕容复':['太原','西安','济南','上海']}

# 统计去过上海的人
for k,v in dict_city.items():
    if '上海' in v:
        print('去过上海的人有：%s'%k)

for k,v in dict_city.items():
    if '济南' in v:
        print(k)