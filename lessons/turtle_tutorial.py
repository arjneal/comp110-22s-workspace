from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.pencolor("pink")

leo.begin_fill()
leo.fillcolor(32, 67, 93)
leo.end_fill()

leo.color("green", "yellow")

leo.color(99, 204, 250)
leo.penup()
leo.goto(45, 60)
leo.pendown()


i = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

bob: Turtle = Turtle()
bob.color("black")
bob.penup()
bob.goto(45, 60)
bob.pendown()


idx: int = 0
side_length: int = 300
while(idx < 3):
    bob.forward(side_length)
    bob.left(120)
    idx += 1
while(idx < 3):
    bob.forward(side_length)
    side_length * .96
    bob.left(120)
    idx += 1
done()
