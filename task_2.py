import turtle

def inflacja(n):
  for i in range(n):
    turtle.forward(10)
    turtle.left(90)
    turtle.forward((2 * n) + (10 * i))
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward((2 * n) + (10 * i))
    turtle.left(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    
inflacja(n)
#more or less done, haven't used the random library
