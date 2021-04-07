import turtle

tortuguinha = turtle.Turtle()
tortuguinha.shape('turtle')
tortuguinha.color('red')

def make_shape(t, sides):
    angle = 360/sides
    for i in range(0,sides):
        t.forward(100)
        t.right(angle)

make_shape(tortuguinha, 1)
make_shape(tortuguinha, 2)
make_shape(tortuguinha, 10)
make_shape(tortuguinha, 20)