class people:
    age = 0
    gender = ""
    name = ""

class workers(people):
    work = ""
    def showworkers(self):
        print("一名",a.age,"岁的",a.gender,"工人，名叫",a.name,"，正在努力的",a.work)

class student(people):
    id = 0
    behavior1 = ""
    behavior2 = ""
    def learn(self):
        print("一名",b.age,"岁的",b.gender,"学生，名叫",b.name,"，学号为",b.id,"，正在努力的",b.behavior1)

    def sing(self):
        print("一名", b.age, "岁的", b.gender, "学生，名叫", b.name, "，学号为", b.id, "，正在努力的", b.behavior2)



a = workers()
a.age = 25
a.gender = "男"
a.name = "张三"
a.work = "干活"
a.showworkers()

b = student()
b.age = 15
b.gender = "男"
b.name = "李四"
b.id = 1234565789
b.behavior1 = "学习"
b.behavior2 = "唱歌"
b.learn()
b.sing()