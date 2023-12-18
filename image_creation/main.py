from canvas import Canvas
from shapes import Rectangle, Square

colors={'white':(255,255,255),'black':(0,0,0)}
canvas_width=int(input("Enter the width of canvas"))
canvas_length=int(input("Enter the length of canvas"))
canvas_color=input("Enter the canvas color ")
canvas= Canvas(canvas_length, canvas_width,colors[canvas_color])

while True:
    shape_type=input("what(Rectangle/Square) do you like to draw, Enter 'quit if want to quit: ")
    if shape_type.upper()== 'RECTANGLE':
        x_co=int(input("Enter the x co-ordinate :"))
        y_co = int(input("Enter the y co-ordinate :"))
        length=int(input("Enter the length (should be lesser than canvas length): "))
        width = int(input("Enter the width (should be lesser than canvas width): "))
        rcolor=int(input("enter the red prop: "))
        gcolor = int(input("enter the green prop: "))
        bcolor = int(input("enter the blue prop: "))
        r1= Rectangle(x_co, y_co, length, width, (rcolor, bcolor, gcolor))
        r1.draw(canvas)
    elif shape_type.upper()== 'SQUARE':
        x_co = int(input("Enter the x co-ordinate :"))
        y_co = int(input("Enter the y co-ordinate :"))
        side = int(input("Enter the side (should be lesser than canvas side): "))
        rcolor = int(input("enter the red prop: "))
        gcolor = int(input("enter the green prop: "))
        bcolor = int(input("enter the blue prop: "))
        s1= Square(x_co, y_co,side, (rcolor, bcolor, gcolor))
        s1.draw(canvas)
    else:
        break
canvas.make()