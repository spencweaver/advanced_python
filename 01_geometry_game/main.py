from random import randint
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x \
            and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * \
            (self.upright.y - self.lowleft.y)

class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()

        canvas.forward()
        canvas.left()
        canvas.forward()
        canvas.left()
        canvas.forward()
        canvas.left()
        canvas.forward()

        turtle.done()

gui_rectangle = GuiRectangle(Point(randint(0, 9), randint(0, 9)),
    Point(randint(10, 19), randint(10, 19)))

myturtle = turtle.Turtle()

gui_rectangle.draw(canvas=myturtle)



# rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
# Point(randint(10, 19), randint(10, 19)))

# print("Rectangle Coordinates: ",
#     rectangle.lowleft.x, ",",
#     rectangle.lowleft.y, "and",
#     rectangle.upright.x, ",",
#     rectangle.upright.y)

# user_point = Point(int(input("Guess X: ")), int(input("Guess Y: ")))

# user_area = float(input("Guess rectangle area: "))


# print("Your point was inside rectangle: ",
#     user_point.falls_in_rectangle(rectangle))

# print("Your are was off by: ",
# rectangle.area() - user_area)
