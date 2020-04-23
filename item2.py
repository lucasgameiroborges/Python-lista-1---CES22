import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tartaruga = turtle.Turtle()
tartaruga.color("red")

draw_poly(tartaruga, 90, 5)