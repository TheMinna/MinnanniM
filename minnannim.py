import turtle

minna = turtle.Turtle()

minna.speed(10)
turtle.Screen().bgcolor("salmon")

minna.pensize(15)
minna.pencolor("white")

minna.penup()
minna.goto(0, 40)
minna.pendown()

minna.left(90)
minna.forward(10)
minna.circle(40,180)
minna.forward(50)
minna.right(180)
minna.forward(90)
minna.right(180)
minna.forward(50)

minna.circle(-40,180) # start of curv until rightway i
minna.forward(50)

minna.penup()  # dot starting
minna.forward(30)
minna.dot(25)

minna.goto(-200, 0) # go to location before M/A
minna.pendown() # M/a starting
minna.right(225)
minna.circle(-75,135)
minna.forward(80)

minna.right(125) # top of M starts
minna.forward(80)
minna.left(70)
minna.forward(80)
minna.right(125)
minna.forward(50)
minna.circle(-55,100)

# mirrored begins

minna.penup()
minna.goto(0, 40) #  moves close to starting point
minna.setheading(-90)
minna.pendown()

#minna.forward(20)
minna.circle(40,180)
minna.forward(50)
minna.right(180)
minna.forward(90)
minna.right(180)
minna.forward(50)

minna.circle(-40,180) # start of curv until rightway i
minna.forward(50)

minna.penup()  # dot starting
minna.forward(30)
minna.dot(25)

minna.goto(200, 95) # go to location before M/A
minna.pendown() # M/a starting
minna.right(225)
minna.circle(-75,135)
minna.forward(80)

minna.right(125) # top of M starts
minna.forward(80)
minna.left(70)
minna.forward(80)
minna.right(125)
minna.forward(50)
minna.circle(-55,100)

minna.hideturtle()
# minna.done()
