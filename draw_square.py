import turtle

def draw_square():
    window = turtle.Screen()

    window.bgcolor("green")
    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    
    brad.forward(100)
    
    
    window.exitonclick()
    
def draw_rectangle():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(10)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(10)
    brad.right(90)
    window.exitonclick()    
    
draw_square()
draw_rectangle()
