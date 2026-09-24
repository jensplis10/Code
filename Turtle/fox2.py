import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
t.speed(0)
t.pensize(3)

# Fuchsfarbe
t.color("orange", "orange")

# Kopf
t.begin_fill()
t.penup()
t.goto(0, -80)
t.pendown()

for _ in range(3):
    t.forward(160)
    t.left(120)

t.end_fill()

# Linkes Ohr
t.begin_fill()
t.penup()
t.goto(-50, 10)
t.pendown()

for _ in range(3):
    t.forward(60)
    t.left(120)

t.end_fill()

# Rechtes Ohr
t.begin_fill()
t.penup()
t.goto(50, 10)
t.pendown()

for _ in range(3):
    t.forward(60)
    t.left(120)

t.end_fill()

# Augen
t.penup()
t.goto(-25, -20)
t.dot(12, "white")

t.goto(25, -20)
t.dot(12, "white")

# Pupillen
t.goto(-25, -20)
t.dot(5, "black")

t.goto(25, -20)
t.dot(5, "black")

# Nase
t.goto(0, -60)
t.dot(12, "black")

t.hideturtle()
turtle.done()