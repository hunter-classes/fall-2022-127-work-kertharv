import turtle

wn = turtle.Screen()

crush = turtle.Turtle()

#draw a square
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)
crush.forward(50)
crush.right(90)

#create a second turtle
squirt = turtle.Turtle()
#into the variable
#and make squirt draw a triangle
squirt.up()
squirt.goto(100, 100)
squirt.down()
squirt.color("red")
squirt.left(120)
squirt.forward(80)
squirt.left(120)
squirt.forward(80)
squirt.left(120)   
squirt.forward(80)

wn.exitonclick()
wn.mainloop()

a = 10 + 30