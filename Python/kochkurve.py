"""Draw a Koch curve fractal in a turtle window.

This script recursively draws a Koch snowflake-like pattern by repeatedly
subdividing a line segment. The recursion depth is controlled by the "start"
variable so the segment length stays proportional to the current depth.
"""

import turtle
import tqdm

LINE_LENGTH = 300
start = 0

# Configure the turtle window for fast drawing without animation flicker.
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)


def kochkurve(n):
    """Draw one segment of a Koch curve with recursive depth n.

    The global `start` value tracks the maximum recursion depth reached so far.
    Each level reduces the segment length to one third of the previous length.
    """
    global start
    start = n if n > start else start

    if n == 1:
        turtle.forward(LINE_LENGTH / 3**start)
        return

    kochkurve(n - 1)
    turtle.left(60)
    kochkurve(n - 1)
    turtle.right(120)
    kochkurve(n - 1)
    turtle.left(60)
    kochkurve(n - 1)


def main():
    """Render several Koch curves in a rotated pattern."""
    for i in tqdm.tqdm(range(1, 7)):
        kochkurve(10)
        print(i)
        turtle.right(60)

    turtle.update()
    turtle.mainloop()


if __name__ == "__main__":
    main()