import turtle

change = 1.76
thickness = 5

r = 0
g = 120
b = 240

sr = change
gr = change
br = change

turtle.bgcolor("black")
turtle.width(3)
turtle.speed(100)
turtle.showturtle()

rotations=0
turn = 0

def colorcicle(value,steigung):
    if value >= 253.4:
        steigung = -change
    elif value <= 1.6:
        steigung = change
    value += steigung
    return value,steigung




while thickness > 1:
    thickness -= 1
    leaves = 0
    while leaves < 8:
        r,sr = colorcicle(r,sr)
        g,gr = colorcicle(g,gr)
        b,br = colorcicle(b,br)
        turtle.color(r/thickness/255,g/thickness/255,b/thickness/255)

        rotations+=5
        turtle.forward(3+thickness)
        turtle.left(5)
        if rotations >= 90:
            rotations=0
            turtle.left(90)
            turn += 1
            if turn >= 2:
                turtle.left(45)
                leaves += 1
                turn = 0

turtle.color(0,0,0)
turtle.hideturtle()




turtle.done()