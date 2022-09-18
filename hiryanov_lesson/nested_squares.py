import turtle as t
N = 10


def square(N):
    for i in range(4):
        t.forward(N)
        t.left(90)


for i in range(1, 11):
    square(N*i)
    t.penup()
    t.goto(-i*5, -i*5)
    t.pendown()



