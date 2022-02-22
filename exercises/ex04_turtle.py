"""Creates a turtle function that includes '3-D' windows, a door with a door knob a triangular roof and a square base."""

__author__ = "730484878"

from turtle import Turtle, done


def main() -> None: 
    """The entrypoint of my scene."""
    tracer: Turtle = Turtle()
    draw_triangle(tracer, 0, 150)
    draw_square(tracer, 150, "black", "yellow")
    draw_door(tracer, 65, 0)
    draw_window(tracer, 15, 75)
    # Drew multiple windows near the same spot in order to attempt to create  3-D looking pop-out windows.
    draw_window(tracer, 18, 78)
    draw_window(tracer, 105, 75)
    draw_window(tracer, 108, 78)
    draw_ground(tracer, -1000, 0)
    draw_sun(tracer, -250, 310)
    done()


def draw_triangle(a: Turtle, x: float, y: float) -> None:
    """Draw roof for the house."""
    i: int = 0
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.begin_fill()
    a.fillcolor("black")
    while(i < 3):
        a.forward(150)
        a.left(120)
        i += 1
    a.end_fill()


def draw_square(a: Turtle, width: int, marker_color: str, fill_color: str) -> None:
    """Draws a square base for the house."""
    # Base outlined in brown to represent the color of wood.
    idx: int = 0
    a.penup()
    a.goto(0, 0)
    a.pendown()
    a.color(marker_color)
    a.begin_fill()
    a.fillcolor(fill_color)
    while(idx < 4):
        a.forward(width)
        a.left(90)
        idx += 1
    a.end_fill()
    a.width()


def draw_window(a: Turtle, x: float, y: float) -> None:
    """Draws a window."""
    ctr: int = 0
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.color("black")
    a.pensize(3)
    # pensize imported from python libraries expands the frame of the window to make it look bigger. 
    a.begin_fill()
    a.fillcolor("blue")
    while (ctr < 4):
        if ctr % 2 != 0:
            a.forward(35)
            a.left(90)
        else:
            a.forward(20)
            a.left(90)
        ctr += 1
    a.end_fill()


def draw_door(a: Turtle, x: float, y: float) -> None:
    # Door function is filled with a black circle that signifies a doorknob.
    """Draws a door and doorknob."""
    a.color("brown")
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.begin_fill()
    a.fillcolor("brown")
    dtc: int = 0
    while (dtc < 4):
        if dtc % 2 != 0:
            a.forward(45)
            a.left(90)
        else:
            a.forward(30)
            a.left(90)
        dtc += 1
    a.end_fill()
    a.penup()
    a.goto(70, 22)
    a.pendown()
    a.begin_fill()
    a.fillcolor("black")
    a.circle(3)
    a.end_fill()
# The circle is the door knob it is the color black and it is a function that I learned using the python library directory. 


def draw_sun(a: Turtle, x: float, y: float) -> None:
    """The sun function being drawn out for the house scene."""
    sun_ctr: int = 0
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.color("orange")
    a.begin_fill()
    a.fillcolor("yellow")
    while (sun_ctr < 6):
        a.right(60)
        a.forward(50)
        sun_ctr += 1
    a.end_fill()
    # Filled with orange and outlined with yellow to make a sun like picture. 


def draw_ground(a: Turtle, x: float, y: float) -> None:
    """Draws the ground of the function."""
    ground_ctr: int = 0
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.begin_fill()
    a.fillcolor("dark green")
    while ground_ctr < 4: 
        a.forward(2000)
        a.right(90)
        ground_ctr += 1
    a.end_fill()
# This function needs to be set at y=0 therefore it is right below the house function.


if __name__ == "__main__":
    main()