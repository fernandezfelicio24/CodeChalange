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




def challange065():

    """
    Write the numbers as shown below,
    starting at the bottom of the number
    one.
    """






def challange066():

    """
    Write the numbers as shown below,
    starting at the bottom of the number
    one.

    """





def challange067():

    """
    Create the following pattern:

    """


def challange068():

    """
    Draw a pattern that will change each time the
    program is run. Use the random function to pick
    the number of lines, the length of each line and
    the angle of each turn.

    """


def main():


    #challange060()
    challange061()
    #challange062()
    #challange063()
    #challange064()
    #challange065()
    #challange066()
    #challange067()








if __name__ == "__main__":
    main()
