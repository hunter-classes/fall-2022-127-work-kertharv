import turtle


def square(t, x, y, w, color, sidelen):
  """
  Draw a square using the turtle passed into t
  
  Parameters:
    t       -  a turtle
    x,y     - location
    w       - width of side
    color   - color to draw in
    sidelen - length of each side
  Returns:
    nothing
  """
  #set the location, color, and width
  t.penup()
  t.goto(x, y)
  t.width(w)
  t.color(color)
  t.pendown()
  #draw a square
  for i in range (4):
    t.forward(sidelen)
    t.right(90)

def triangle(t, x, y, w, color, sidelen):
  #code to draw the triangle
  t.penup()
  t.goto(x, y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range (3):
    t.left(120)
    t.forward(sidelen)

def hexagon(t, x, y, w, color, sidelen):
  #code to draw the hexagon
  t.penup()
  t.goto(x, y)
  t.width(w)
  t.color(color)
  t.pendown()
  for i in range (6):
    t.forward(sidelen)
    t.left(300)


def ngon(t, numsides, x, y, color, width, sidelen):
  #code to draw the ngon
  #numsides- number of sides to draw a polygon
  t.penup()
  t.goto(x, y)
  t.width(width)
  t.color(color)
  t.pendown()
  t.left(30)
  t.forward(sidelen)
  t.left(60)
  t.forward(sidelen)
  t.left(120)
  t.forward(sidelen)
  t.left(60)
  t.forward(sidelen)
  t.left(90)
  

wn = turtle.Screen()

honey = turtle.Turtle()
triangle(honey, 0, 0, 1, "red", 100)

hexxy = turtle.Turtle()
hexagon(hexxy, 50, 50, 5, "aqua", 90)

indeed = turtle.Turtle()
ngon(indeed, 6, 0, 0, "black", 5, 150)

crush = turtle.Turtle()
square(crush, 0, 0, 1, "green", 50)

squirt = turtle.Turtle()
square(squirt, 100, 100, 5, "red", 80)

square(crush, -50, 30, 3, "yellow", 100)

crush.setheading(45)
square(crush, 150, 30, 2, "blue", 60)

wn.exitonclick()
wn.mainloop()