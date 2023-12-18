from random import randint
import turtle


class Point:


    def __init__(self,x,y):
        """ intiating the point """
        self.x=x
        self.y=y

    def falls_in_triangle(self,rectangle):
        if (rectangle.lowerbound.x <= self.x <= rectangle.upperbound.x \
            and rectangle.lowerbound.y <= self.y <= rectangle.upperbound.y )\
            or (rectangle.upperbound.x <= self.x <= rectangle.lowerbound.x \
            and rectangle.upperbound.y <= self.y <= rectangle.lowerbound.y ):
            print(True)
        else:
            print(False)
    
    def distance_from_x(self,x=0,y=0) :
        return ((x-self.x)**2+(y-self.y)**2)**0.5


class Rectangle:

    def __init__(self,lowerbound,upperbound):
        self.lowerbound=lowerbound
        self.upperbound=upperbound



class GUiRectangle(Rectangle):

    def draw(self,canvas):
        # it moves the pointer up so no sketching
        canvas.penup()
        # go to a certain point 
        canvas.goto(self.lowerbound.x,self.lowerbound.y)
        canvas.pendown()
        # start sketching
        canvas.forward(self.upperbound.x - self.lowerbound.x)
        canvas.left(90)
        canvas.forward(self.upperbound.y - self.lowerbound.y)
        canvas.left(90)
        canvas.forward(self.upperbound.x - self.lowerbound.x)
        canvas.left(90)
        canvas.forward(self.upperbound.y - self.lowerbound.y)

class GuiPoint(Point):

    def draw(self,canvas,size=5,color='red'):

        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size,color)



#creating a dynamically rectangle 

rec=GUiRectangle(Point(randint(0,400),randint(0,400)),Point(randint(0,400),randint(0,400)))

print ("Rectangle co-ordinates are :", 
        "(", str(rec.lowerbound.x),",",str(rec.lowerbound.y) , ") ,", "and",
                    "(", str(rec.upperbound.x),",",str(rec.upperbound.y) , ")")

rec.draw(turtle.Turtle())
user_point=GuiPoint(int(input("Enter the x co-ordinate : ")),int(input("Enter the y co-ordinate : ")))

user_point.falls_in_triangle(rec)

user_point.draw(turtle.Turtle())
turtle.done()
