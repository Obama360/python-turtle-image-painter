import turtle
import numpy as np
from PIL import Image

t = turtle.Turtle()
t.speed("fastest")
t.screen.colormode(255)

def PaintImage(image, scale, turtle):
    img = Image.open(image)
    arr = np.array(img)
    progressrn = 0
    turtle.pensize(4)
    
    print("Image size: {}, {}".format(len(arr), len(arr[0])))
    
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            turtle.pencolor(arr[x,y][0],arr[x,y][1],arr[x,y][2])
            turtle.forward(scale)
            
        t.penup()
        turtle.backward(len(arr[0])*scale)
        turtle.right(90)
        turtle.forward(scale)
        turtle.left(90)
        turtle.pendown()
        progress = int((100/len(arr)*x))
        if progress != progressrn:
            progressrn = progress
            print("painting {}, {}%".format(image, progressrn))
            
PaintImage("test.png", 3, t)
PaintImage("cat5.png", 4, t)