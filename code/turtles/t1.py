import turtle

def sample_function():
  print("This is a function")
  print("It can be used multiple times")
  
wn = turtle.Screen()

crush = turtle.Turtle()

#draw a square
for i in range (4):
  crush.forward(50)
  crush.right(90)

#create a second turtle
#into the variable
squirt = turtle.Turtle()
#and make squirt draw a triangle
squirt.up()
squirt.goto(100, 100)
squirt.down()
squirt.color("red")

for i in range(3):
  squirt.left(120)
  squirt.forward(80)

sample_function()
sample_function()
sample_function()

wn.exitonclick()
wn.mainloop()

a = 10 + 30