"""
Challange 27 until 34 is about MATHS


"""


def challange027():

    """
        Ask the user to enter a
    number with lots of
    decimal places. Multiply
    this number by two and
    display the answer.

    """

    decimal = float(input("Enter a number with lots of decimal places : "))
    result = decimal * 2

    print(f"The result is {result}")


def challange028():

    """
           Update program 027 so that it will display the answer to
    two decimal places.

    """

    decimal = float(input("Enter a number with lots of decimal places : "))
    result = decimal * 2

    resulttwodecimal = round(result, 2)
    print(result)
    print(f"The result is {resulttwodecimal}")

def challange029():

    import math
    """
        Ask the user to enter an integer that is over 500. Work
    out the square root of that number and display it to two decimal places

    """

    number = int(input("Enter a number over 500 : "))

    result = math.sqrt(number)

    resulttwodecimal = round(result,2)
    print(f"The result is {resulttwodecimal}")





def challange030():

    import math

    """
    Display pi (π) to five
    decimal places.

    """
    print(round(math.pi, 5))


def challange031():

    import math

    """
           Ask the user to enter the radius of a circle
    (measurement from the centre point to the edge). Work
    out the area of the circle (π*radius2).
    """
    radius = int(input("Enter the radius of a circle : "))

    result = (math.pi * radius**2)

    print(f"The result of radius is : {result}")


def challange032():

    import math

    """
                   Ask for the radius and the depth of a cylinder
        and work out the total volume (circle
        area*depth) rounded to three decimal
        places.

    """
    radius = int(input("Enter the radius of a circle : "))
    depth = int(input("Enter the depth : "))
    area = (math.pi * radius**2)

    volume = area * depth

    print(round(volume))

def challange033():

    """
        Ask the user to enter two numbers.
    Use whole number division to divide
    the first number by the second and
    also work out the remainder and
    display the answer in a user-friendly
    way (e.g. if they enter 7 and 2 display
    “7 divided by 2 is 3 with 1
    remaining”).

    """
    number = int(input("Enter the first number : "))
    othernumber = int(input("Enter another number : "))

    result = number//othernumber
    result1 = number%othernumber
    print(result)
    print(number, "divided by", othernumber, " is ", result, "with ", result1, "remaining")


def challange034():

    """


        Display the following message:
        1. Square
        2. Triangle
        Enter a number :
    If the user enters 1, then it should ask them for
    the length of one of its sides and display the
    area. If they select 2, it should ask for the base
    and height of the triangle and display the area. If
    they type in anything else, it should give them a
    suitable error message.
    """
    print("1) Square ")
    print("2) Triangle")

    choice = int(input("Enter your choice 1 or 2 : "))

    if choice == 1 :
        side = int(input("Enter the lenght of one side : "))
        area = side * side
        print(f"The area of your chosen shape is ", area)

    elif choice == 2 :
        base = int(input("Enter the lenght of base : "))
        height = int(input("Enter the height of the triangle : "))
        area = (base*height)/2
        print(f"The area of your chosen shape is {area}")
    else:
        print("Incorect option selected")


def main():


    #challange027()
    #challange028()
    #challange029()
    #challange030()
    #challange031()
    #challange032()
    #challange033()
    challange034()








if __name__ == "__main__":
    main()
