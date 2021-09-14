while True:
    mon = int(input("请输入充值金额"))
    if mon < 1000:
        print("充值金额太小，请重新充值")
        continue;
    elif 1000 <= mon < 2000:
        mon = mon + mon * 0.1
        print("充值成功，当前余额为：", mon)
        break;
    elif 2000 <= mon < 3000:
        mon = mon + mon * 0.2
        print("充值成功，当前余额为：", mon)
        break;
    elif 3000 <= mon < 4000:
        mon = mon + mon * 0.3
        print("充值成功，当前余额为：", mon)
        break;
    elif 4000 <= mon < 5000:
        mon = mon + mon * 0.4
        print("充值成功，当前余额为：", mon)
        break;
    elif 5000 <= mon:
        mon = mon + mon * 0.5
        print("充值成功，当前余额为：", mon)
        break;
while True:
    play = (input("开始游戏请输入'1',退出游戏请输入'q'"))
    if play == "q":
        print("退出游戏")
        break;
    elif play == "1":
        print("游戏开始")
        break;
    else:
        print("输入错误，请重新输入")


import random
ran = random.randint(0,100)
life = 5
while play == "1":
    a = int(input("请输入一个数"))
    if mon < 500:
        print("余额不足，不能继续游戏")
        break;
    if life == 0:
        print("次数用尽，不能继续游戏")
        break;

    elif ran < a:
        print("输入的数字太大了")
        mon = mon - 500
        print("剩余金额为：",mon)
        life = life - 1
        print("剩余次数为：",life)
        continue;
    elif ran > a:
        print("输入的数字太小了")
        mon = mon - 500
        print("剩余金额为：",mon)
        life = life - 1
        print("剩余次数为：", life)
        continue;
    else:
        print("猜对了")
        mon = mon - 500
        print("剩余金额为：",mon)
    break;
