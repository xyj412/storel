# 水杯
# class Cap:
#     __height = 0
#     __volume = 0
#     __color = ""
#     __material = ""
#
#     def setHeight(self,height):
#         if height <= 0:
#             print("高度输入非法")
#         else:
#             self.__height = height
#     def getHeight(self):
#         return self.__height
#
#     def setVolume(self,volume):
#         if volume <= 0:
#             print("容积输入非法")
#         else:
#             self.__volume = volume
#     def getVolume(self):
#         return self.__volume
#
#     def setColor(self,color):
#         self.__color = color
#     def getColor(self):
#         return self.__color
#
#     def setMaterial(self,material):
#         self.__material = material
#     def getMaterial(self):
#         return self.__material
#
#     def store(self,ml):
#         print("存放了",ml,"毫升水")
#
#     def showCap(self):
#         print("该杯子高度为",self.__height,"厘米，容积为",self.__volume,"毫升，颜色是",self.__color,"，材质是",self.__material)
#
#
# p = Cap()
# # p.height = 20
# p.setHeight(20)
# # p.volume = 500
# p.setVolume(500)
# # p.color = "白色"
# p.setColor("白色")
# # p.material = "玻璃"
# p.setMaterial("玻璃")
#
# p.store(200)
# p.showCap()



# 笔记本电脑
# class Computer:
#     __screen = 0
#     __price = 0
#     __cpu = ""
#     __memory = 0
#     __standby = 0
#
#     def setScreen(self,screen):
#         if screen <= 0:
#             print("屏幕大小输入非法")
#         else:
#             self.__screen = screen
#     def getScreen(self):
#         return self.__screen
#
#     def setPrice(self,price):
#         if price <= 0:
#             print("价格输入非法")
#         else:
#             self.__price = price
#     def getPrice(self):
#         return self.__price
#
#     def setCpu(self,cpu):
#         self.__cpu = cpu
#     def getCpu(self):
#         return self.__cpu
#
#     def setMemory(self,memory):
#         if memory <= 0:
#             print("内存大小输入非法")
#         else:
#             self.__memory = memory
#     def getMemory(self):
#         return self.__memory
#
#     def setStandy(self,standy):
#         if standy < 0:
#             print("待机时长输入非法")
#         else:
#             self.__standby = standy
#     def getStandy(self):
#         return self.__standby
#
#     def showComputer(self):
#         print("这台电脑屏幕大小为",self.__screen,"英寸，价格为",self.__price,"元，cup型号是",self.__cpu,
#               "，内存大小为",self.__memory,"TB，待机时长为",self.__standby,"小时")
#
#     def typing(self,number):
#         print("使用该电脑打了",number,"个字!")
#
#     def game(self,hours):
#         print("使用该电脑玩了",hours,"个小时游戏!")
#
#     def video(self,hours):
#         print("使用该电脑看了",hours,"个小时视频!")
#
# a = Computer()
# a.setScreen(40)
# a.setPrice(6000)
# a.setCpu("1234ti")
# a.setMemory(2)
# a.setStandy(10)
#
# a.typing(50000)
# a.game(4)
# a.video(6)
#
# a.showComputer()



# 学生类
# class student:
#     __id = 0  # 学号
#     __name = ""  # 姓名
#     __age = 0  # 年龄
#     __gender = ""  # 性别
#     __high = 0  # 身高
#     __weight = 0  # 体重
#     __results = 0  # 成绩
#     __home = ""  # 家庭地址
#     __phone = 0  # 电话号码
#
#     def setid(self,id):
#         self.__id = id
#     def getid(self):
#         return self.__id
#
#     def setname(self,name):
#         self.__name = name
#     def getname(self):
#         return self.__name
#
#     def setage(self,age):
#         if age < 0:
#             print("年龄不能为负数")
#         else:
#             self.__age = age
#     def getage(self):
#         return self.__age
#
#     def setgender(self,gender):
#         self.__gender = gender
#     def getgender(self):
#         return self.__gender
#
#     def sethigh(self,high):
#         if 30 > high or high > 230:
#             print("身高输入非法")
#         else:
#             self.__high = high
#     def gethigh(self):
#         return self.__high
#
#     def setweight(self,weight):
#         if weight < 0:
#             print("体重不能为0")
#         else:
#             self.__weight = weight
#     def getweight(self):
#         return self.__weight
#
#     def setresults(self,results):
#         if results < 0:
#             print("成绩不能为负数")
#         else:
#             self.__results = results
#     def getresults(self):
#         return self.__results
#
#     def sethome(self,home):
#         self.__home = home
#     def gethome(self):
#         return self.__home
#
#     def setphone(self,phone):
#         self.__phone = phone
#     def getphone(self):
#         return self.__phone
#
#     def learning(self,hours):
#         print(self.__name,"学习了",hours,"小时!")
#
#     def playgame(self,gamename):
#         print(self.__name,"正在玩",gamename,"!")
#
#     def programming(self,number):
#         print(self.__name,"写了",number,"行代码!")
#
#     def showstudent(self):
#         info = '''
#                     ------------学生信息------------
#                     学号:%s
#                     姓名：%s
#                     年龄：%s
#                     性别：%s
#                     身高：%s cm
#                     体重：%s kg
#                     成绩：%s
#                     家庭地址：%s
#                     电话号码：%s
#                 '''
#         print(info % (self.__id, self.__name, self.__age, self. __gender, self.__high, self.__weight,
#                       self.__results, self.__home, self.__phone))
#
#
# a = student()
#
# a.setid(12345689)
# a.setname("张三")
# a.setage(18)
# a.setgender("男")
# a.sethigh(150)
# a.setweight(50)
# a.setresults(80)
# a.sethome("aa省bb市")
# a.setphone(12345678910)
#
#
# a.learning(5)
# a.playgame("炸弹人")
# a.programming(100)
#
# a.showstudent()



# 车类
# class car:
#     __model = ""  # 车型号
#     __wheel = 0  # 车轮数
#     __color = ""  # 车身颜色
#     __weight = 0  # 车重量
#     __tank = 0  # 油箱存储大小
#
#     def setmodel(self,model):
#         self.__model = model
#     def getmodel(self):
#         return self.__model
#
#     def setwheel(self,wheel):
#         if wheel < 0:
#             print("车轮数不能为负数!")
#         else:
#             self.__wheel = wheel
#     def getwheel(self):
#         return self.__wheel
#
#     def setcolor(self,color):
#         self.__color = color
#     def getcolor(self):
#         return self.__color
#
#     def setweight(self,weight):
#         if weight < 0:
#             print("车重量不能为0!")
#         else:
#             self.__weight = weight
#     def getweight(self):
#         return self.__weight
#
#     def settank(self,tank):
#         if tank < 10:
#             print("车油箱储存大小不合法!")
#         else:
#             self.__tank = tank
#     def gettank(self):
#         return self.__tank
#
#     def run(self,function):
#         print(self.__model,"品牌的车正在进行",function,"比赛!")
#
#     def showcar(self):
#         print("这辆车型号为",self.__model,"，有",self.__wheel,"个车轮，颜色是",self.__color,
#               "，重量为",self.__weight,"kg，油箱存储大小为",self.__tank,"L!")
#
# a = car()
#
# a.setmodel("法拉利")
# a.setwheel(4)
# a.setcolor("红色")
# a.setweight(200)
# a.settank(20)
#
# a.run("赛车")
#
# a.showcar()



# 猴子类
class monkey:
    __category = ""  # 类别
    __gender = ""   # 性别
    __color = ""  # 颜色
    __weight = 0  # 体重

    def setcategory(self,category):
        self.__category = category
    def getcategory(self):
        return self.__category

    def setgender(self,gender):
        self.__gender = gender
    def getgender(self):
        return self.__gender

    def setcolor(self,color):
        self.__color = color
    def getcolor(self):
        return self.__color

    def setweight(self,weight):
        if weight <= 0:
            print("猴子的重量不能为0!")
        else:
            self.__weight = weight
    def getweight(self):
        return self.__weight

    def fire(self,material):
        print("这只猴子正在用",material,"造火!")

    def learning(self,things):
        print("这只猴子正在学习",things)

    def showmonkey(self):
        print("这是一只",self.__category,"，",self.__gender,"性，",self.__color,"，体重为",self.__weight,"kg")

a = monkey()

a.setcategory("金丝猴")
a.setgender("雄")
a.setcolor("金色")
a.setweight(20)

a.fire("石头")
a.learning("搬东西")

a.showmonkey()


















