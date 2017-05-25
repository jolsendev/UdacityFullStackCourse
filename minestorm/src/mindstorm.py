import turtle

def draw_flower(some_turtle):
    rhombus = 45;
    for i in list(range(4)):
        some_turtle.forward(50)
        if i % 2 == 0:
            some_turtle.right(90-rhombus)
        else:
            some_turtle.right(90+rhombus)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    t = turtle.Turtle()
    t.color("yellow")
    t.speed(10)
    for i in list(range(36)):
        draw_square(t)
        t.right(10)
    t.color("green")
    t.speed(1)
    t.right(90)
    t.forward(250)
    window.exitonclick()

draw_art()











def draw_circle(some_turtle):
    some_turtle.circle(50)
    some_turtle.right(90)


def draw_triangle(some_turtle):
    some_turtle.right(60)
    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(100)

