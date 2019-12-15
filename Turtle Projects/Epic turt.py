import turtle 

t = turtle.Turtle()

t.pencolor("black")

t.speed(10)

for i in range(180):
    t.forward(90)
    t.right(i)
    t.forward(90)
    t.pencolor("green")
    t.left(i)
    t.forward(100)
    t.right(75)
    
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    
    t.right(2)
    
turtle.done()
