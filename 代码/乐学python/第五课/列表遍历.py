guests = ['张三丰', '萧峰', '杨过', '令狐冲', '张无忌', '段誉']

for item in guests:
    print('九月初九，华山论剑，诚邀各位大侠:', item)

snackes = ['松饼', '提拉米苏', '芝士蛋糕', '三明治']
drinks = ['红茶', '咖啡', '橙汁']
meuns = []
for snacke in snackes:
    for drink in drinks:
        meun = (snacke, drink)
        meuns.append(meun)
        print(meun)

# 算多少个选择
lvyous = ['登山', '看海', '攀岩', '游泳', '滑翔']
chuxings = ['徒步', '自行车', '汽车', '火车']

cishus = []
for lvyou in lvyous:
    for chuxing in chuxings:
        cishu = (lvyou, chuxing)
        cishus.append(cishu)
        # print(cishus.count(cishu))
        print(cishu)


# 搭配营养早餐
hedes = ['牛奶','豆浆','小米粥','八宝粥']
chides = ['鸡蛋','油条','包子','咸菜']
fangshis = ['打包','在这吃']

counts = []
for hede in hedes:
    for chide in chides:
        for fangshi in fangshis:
            count = (hede,chide,fangshi)
            counts.append(count)
            print(count)