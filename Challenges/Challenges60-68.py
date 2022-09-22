"""

Challange 60 until 68 is about TURTLE GRAPHICS


"""
import turtle

def challange060():

    """
    Draw a square

    """


    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)


def challange061():

    """
    Draw a triangle.

    """

    for i in range(0,3):
        turtle.forward(100)
        turtle.left(120)

    turtle.exitonclick()


def challange062():

    """
    Draw a circle.

    """


    for i in range(0, 360):

        turtle.forward(1)
        turtle.right(1)


    turtle.exitonclick()




def challange063():



    """
    Draw three squares
    in a row with a gap
    between each. Fill
    them using three
    different colours.

    """

    turtle.color("black","red")
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(70)
        turtle.right(90)

    turtle.penup()
    turtle.end_fill()
    turtle.forward(100)

    turtle.pendown()
    turtle.color("black","yellow")
    turtle.begin_fill()

    for i in range (0,4):
        turtle.forward(70)
        turtle.right(90)




def challange064():



    """
    Draw a five-pointed
    star

    """

    for i in range(0, 5):
        turtle.forward(100)
        turtle.right(144)

    turtle.exitonclick()


def challange065():

    """
    Write the numbers as shown below,
    starting at the bottom of the number
    one.
    """


    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(75)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(180)


    turtle.forward(45)
    turtle.left(90)
    turtle.forward(50)

    turtle.left(90)
    turtle.forward(75)

    turtle.hideturtle()
    turtle.exitonclick()

def challange066():

    """
        Draw an octagon that uses a different colour (randomly
    selected from a list of six possible colours) for each line.

    """

    import random

    turtle.pensize(3)

    for i in range (0, 8):
        turtle.color(random.choice(["red", "blue", "yellow", "green", "pink", "orange"]))
        turtle.forward(50)
        turtle.right(45)

    turtle.exitonclick()


def challange067():

    """
    Create the following pattern:

    """
    import random

    for x in range(0, 10):
        for i in range (0, 8):
            turtle.forward(50)
            turtle.right(45)
        turtle.right(36)

    turtle.hideturtle()
    turtle.exitonclick()

def challange068():

    """
    Draw a pattern that will change each time the
    program is run. Use the random function to pick
    the number of lines, the length of each line and
    the angle of each turn.

    """

    import random

    lines = random.randint(5, 20)

    for x in range(0, lines):
        length = random.randint(25, 100)
        rotate = random.randint(1, 365)
        turtle.forward(length)
        turtle.right(rotate)
    turtle.exitonclick()

def main():


    #challange060()
    #challange061()
    #challange062()
    #challange063()
    #challange064()
    #challange065()
    #challange066()
    #challange067()
    challange068()







if __name__ == "__main__":
    main()
