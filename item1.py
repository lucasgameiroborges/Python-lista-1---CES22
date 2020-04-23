import turtle

def draw_square(t, sz):
    # """Make turtle t draw a square of sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes

wn.bgcolor("lightgreen")

tartaruga = turtle.Turtle()
tartaruga.color("red")

tamanhoInicial = 20
numQuadrados = 5
l = tamanhoInicial

for i in range(numQuadrados):
    tartaruga.color("lightgreen")
    tartaruga.setposition(i*(-1)*(tamanhoInicial/2)+tamanhoInicial/2, i*(-1)*(tamanhoInicial/2)+tamanhoInicial/2)
    tartaruga.color("red")
    draw_square(tartaruga, l)
    l = l + 20
