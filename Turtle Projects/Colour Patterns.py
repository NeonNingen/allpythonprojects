import turtle 

t = turtle.Turtle()

t.pencolor("blue")

for i in range(200):
    t.forward(100)
    t.backward(i)
    t.left(260) 
    
    
turtle.done()
