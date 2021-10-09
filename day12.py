from threading import Thread
import time

tart = 0
class cook(Thread):
    def run(self) -> None:
        global tart
        while True:
            if tart < 50:
                tart = tart + 1
                print("cook造了一个蛋挞,现有",tart,"个蛋挞")
            else:
                time.sleep(3)

class user(Thread):
    money = 300
    count = 0
    def run(self) -> None:
        global tart
        while True:
            if tart > 0 and self.money - 2 > 0:
                tart = tart - 1
                self.money = self.money - 2
                self.count = self.count + 1
                print(self.name,"购买了一个蛋挞，还有",self.money,"元")
            elif tart == 0:
                time.sleep(3)
            elif self.money - 2 == 0:
                print("没钱了，买了",self.count,"个蛋挞")
                break



c1 = cook()
c2 = cook()
c3 = cook()

u1 = user()
u2 = user()
u3 = user()
u4 = user()
u5 = user()
u6 = user()

u1.name = "a"
u2.name = "b"
u3.name = "c"
u4.name = "d"
u5.name = "e"
u6.name = "f"

c1.start()
c2.start()
c3.start()

u1.start()
u2.start()
u3.start()
u4.start()
u5.start()
u6.start()