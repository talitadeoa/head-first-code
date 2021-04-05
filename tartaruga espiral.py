import turtle 

tortuguinha = turtle.Turtle()
tortuguinha.shape('turtle')
tortuguinha.color('red')
tortugo = turtle.Turtle()
tortugo.shape('turtle')
tortugo.color('blue')

def faz_quadradin(the_turtle):

    for i in range(0,4):
        the_turtle.forward(100)
        the_turtle.right(90)

def faz_espiral(the_turtle):
    for i in range(0,36):
        faz_quadradin(the_turtle)
        the_turtle.right(10)

faz_espiral(tortuguinha)
tortugo.right(5)
faz_espiral(tortugo)
