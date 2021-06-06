import turtle
import math


# class test1:
#     def zuo(self):
#         draw = turtle.Pen()
#         draw.forward(100)
#         draw.left(120)
#         draw.forward(200)
#
#     def zuo1(self):
#         draw2 = turtle.Pen()
#         draw2.backward(100)
#         draw2.left(60)
#         draw2.forward(200)
#
#     def zuo2(self):
#         draw3 = turtle.Pen()
#         draw3.left(90)
#         draw3.forward(round(math.sqrt(200*200-100*100),2))
#
#     def zuo4(self):
#         self.zuo()
#         self.zuo1()
#         self.zuo2()
#         self.zuo4()
#
# leo = test1()
# leo.zuo4()



class juxing:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def round(self):
        print('round is:',2*(self.a + self.b))

    def area(self):
        print('area is:',self.a + self.b)

    def show(self):
        self.area()
        self.round()


leo = juxing(3, 5)
leo.round()
leo.area()
print('________________')
leo.show()
print('_________________')


class juxing1:
    def round(self, a, b):
        print('round is', 2 * (a + b))

    def area(self, a, b):
        print('area is ', a + b)

    def show(self):
        self.round(6, 5)
        self.area(2, 6)


leo = juxing1()
leo.round(3, 5)
leo.area(4, 2)
print('_______________')
leo.show()
print('_________________')



class juxing3:
    def round(self,a,b):
        print('round is:',2*(a+b))

class juxing4(juxing3):
    def area(self,a,b):
        print('area is ',a+b)

class juxing5(juxing4):
    def show(self):
        self.area(6,6)
        self.round(6,6)
        print('完美结束~')

leo = juxing5()
leo.show()



draw1 = turtle.Pen()
draw2 = turtle.Pen()
draw3 = turtle.Pen()
draw1.forward(200)
draw1.forward(150)
draw2.left(90)
draw2.forward(100)
draw2.right(90)
draw2.forward(50)
draw3.forward(150)
draw3.left(90)
draw3.forward(100)
draw3.left(90)
draw3.forward(50)


