import turtle

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
  for i in range (numsides):
    t.forward(sidelen)
    t.left(45)

wn = turtle.Screen()

hexxy = turtle.Turtle()
hexagon(hexxy, 50, 50, 5, "aqua", 90)

indeed = turtle.Turtle()
ngon(indeed, 8, -65, -50, "black", 5, 40)

wn.exitonclick()
wn.mainloop()