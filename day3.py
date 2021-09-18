# 十个数的和
# a = int(input("请输入第一个数"))
# b = int(input("请输入第二个数"))
# c = int(input("请输入第三个数"))
# d = int(input("请输入第四个数"))
# e = int(input("请输入第五个数"))
# f = int(input("请输入第六个数"))
# g = int(input("请输入第七个数"))
# h = int(input("请输入第八个数"))
# i = int(input("请输入第九个数"))
# j = int(input("请输入第十个数"))
#
# print("输入十个数的和为：",a+b+c+d+e+f+g+h+i+j)



# 打印最大数、求和、平均数
# n = 0
# max = 0
# for i in range(0,10):
#     num = int(input("请输入正整数"))
#     n = num + n
#     if num > max:
#         max = num
# print("十个数的最大值为",max)
# print("和为",n)
# print("平均数为",n/10)



# 产生50~150之间的数
# import random
# ran = random.randint(50,150)
# print(ran)



# 构成三角形
# a = int(input("请输入第一条边"))
# b = int(input("请输入第二条边"))
# c = int(input("请输入第三条边"))
# while True:
#     if a < b + c and b < a + c and c < a + b:
#         if a == b == c:
#             print("构成等边三角形")
#             break;
#         elif a == b or b == c or a == c:
#             print("构成等腰三角形")
#             break;
#         elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#             print("构成直角三角形")
#             break;
#         else:
#             print("构成普通三角形")
#         break;
#     else:
#         print("不能构成三角形")
#         break;



# 调换
# print("A=56")
# print("B=78")
# while True:
#     m = input("请输入‘+’号或者‘-’号")
#     if m == '+':
#         print("A=78")
#         print("B=56")
#         break;
#     elif m == '-':
#         print("A=56")
#         print("B=78")
#         break;
#     else:
#         print("输入无效，请重新输入")
#         continue;



# 密码输入错误三次锁定
# left = 3
# while left > 0:
#     name = input("请输入账号")
#     password = input("请输入密码")
#     if name != 'root' and password != 'admin':
#         left = left - 1
#         print("用户名或密码输入错误，还有",left,"次机会")
#         continue;
#     elif name == 'root' and password == 'admin':
#         print("登陆成功")
#         break;
# while left == 0:
#     print("输入错误的次数已达到三次，账号被锁定")
#     break;


# 打印*号
# i = 0
# while i < 9:
#     if i < 7:
#         j = 0
#         while j < 7 - i:
#             print(" ", end="")
#             j += 1
#         j = 0
#         while j < i + 1:
#             print("*", end=" ")
#             j += 1
#     print()
#     i += 1


# 九九乘法表
# a = 1
# while a <= 9:
#     b = 1
#     while b <= a:
#         print("%d*%d=%d\t" % (b, a, a*b), end = " ")
#         b += 1
#     print()
#     a += 1
# print()


# 九九乘法表倒叙打印
i = 9
while i >= 1:
    j = 1
    while j <= i:
        print('%d*%d=%-2d'%(j,i,j*i),end ='  ')
        j += 1
    print()
    i -= 1
