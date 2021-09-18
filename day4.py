# 添加列表
# list = ["北京", "上海", "广东"]
# list2 = ["天津", "重庆", "黑龙江", "吉林", "辽宁", "内蒙古", "河北", "新疆", "甘肃", "青海"]
# list.extend(list2)
# print(list)
# # 换位置
# list[1],list[2] = list[2],list[1]
# print(list)

# 计算
# A=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# print("GDP总和为:",sum(A))
# print("平均GDP为:",sum(A)/8)



# 求5的倍数的和
a = [1,5,21,30,15,9,30,24]
b = []
while len(a) > 0:
    m = a.pop()
    if m%5 == 0:
        b.append(m)
print("是5的倍数的和为",sum(b))



# 翻转
# list = [1,2,3,4,5,6,7,8,9]
# list.reverse()
# print(list)



# 统计出现的次数
# a = int(input("输入一个数"))
# list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# print(a,"出现了",list.count(a),"次")