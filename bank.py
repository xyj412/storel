import  random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={}
#bank={'Frank': {'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002', 'ran': 38340677, 'money': 0}}
#{'Frank': {'password': '123456', 'country': '中国', 'province': '山东', 'street': '001', 'door': '002', 'ran': 38340677, 'money': 0}}
bank_name="中国工商银行"#全局变量
def bank_adduser(username,password,country,province,street,door,account,money):
    if account in bank :#如果一个变量在容器内就运行代码
        return 2
    if len(bank)>=100:
        return 3
    bank[account]={
         "username":username,
         "password":password,
         "country":country,
         "province":province,
         "street":street,
         "door":door,
         "money":money,
         "bank_name":bank_name
     }
    return 1

def useradd():
    username=input("请输入您的用户名：")#局部变量
    password = input("请输入密码：")#print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10,99)
    money=0
    bankadd=bank_adduser(username,password,country,province,street,door,account,money)
    if bankadd == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
    elif bankadd ==2:
        print("用户已存在")
    elif bankadd == 3:
        print("数据库已满")

def withdraw():
    account=int(input("请输入你的账号："))
    life = 3  # 密码输入最大次数
    if account in bank:
        while True:
            password=input("请输入您的密码")
            if password == bank[account]["password"]:
                withdraw_money=int(input("请输入你要取款的金额："))
                if withdraw_money > bank[account]["money"]:
                    print("您的余额不足！余额：",bank[account]["money"])
                    break
                else:
                    balance=bank[account]["money"]- withdraw_money
                    print("取钱成功！您的余额为：",balance)
                    bank[account]["money"]=balance
                    break
            else:
                print("很抱歉，密码输入错误，您还有", life - 1, "次机会")
                life -= 1
                if life == 0:
                    print("密码错误，账号已锁定，请到柜台解锁")
                continue
    else:
        print("您输入的账号不存在！")

def saving():
    account=int(input("请输入你的账号："))
    if account in bank:
        money=int(input("请输入你要存入的金额："))
        bank[account]["money"]+=money
        print("存款成功！你的余额为：",bank[account]["money"])
    else:
        print("您输入的账号不存在！")

def transfer():
    account=int(input("请输入您的账号"))
    life = 3  # 密码输入最大次数
    if account in bank:
        account2=int(input("请输入您要转账的账号："))
        if account2 in bank:

            while True:
                password = input("请输入您的密码")
                if password == bank[account]["password"]:
                    money=int(input("请输入您要转账的金额："))
                    bank[account]["money"]-=money
                    bank[account2]["money"]+=money
                    print("转账成功！您的余额为：",bank[account]["money"])
                    break
                else:
                    print("很抱歉，密码输入错误，您还有", life - 1, "次机会")
                    life -= 1
                    if life == 0:
                        print("密码错误，账号已锁定，请到柜台解锁")
                    continue
        else:
            print("您输入的账号不存在")
    else:
        print("您输入的账号不正确！")

def inquire():
    account=int(input("请输入您要查询的账号："))
    life = 3  # 密码输入最大次数
    if account in bank :
        password=input("请输入密码")
        while True:
            if password == bank[account]["password"]:
                print("当前账号：",account,",密码：******","用户居住地：",bank[account]["country"]["province"]["street"]["door"],"，开户行：",bank[account]["bank_name"])
                break
            else:
                print("很抱歉，密码输入错误，您还有", life - 1, "次机会")
                life -= 1
                if life == 0:
                    print("密码错误，账号已锁定，请到柜台解锁")
                continue
    else:
        print("该用户不存在")


while True:#永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        withdraw()
    elif begin == "3":
        saving()
    elif begin == "4":
        transfer()
    elif begin == "5":
        inquire()
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break