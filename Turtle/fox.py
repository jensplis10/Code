import turtle

change = 1.76

r = 0
g = 120
b = 240

sr = change
gr = change
br = change

turtle.bgcolor("black")
turtle.width(3)
turtle.speed(100)


def colorcicle(value,steigung):
    if value >= 253.4:
        steigung = -change
    elif value <= 1.6:
        steigung = change
    value += steigung
    return value,steigung

def changecolor():
    global r,sr,g,gr,b,br
    r,sr = colorcicle(r,sr)
    g,gr = colorcicle(g,gr)
    b,br = colorcicle(b,br)
    turtle.color(r/255,g/255,b/255)

while True:
    changecolor()





turtle.done()