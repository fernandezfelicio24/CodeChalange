"""
Challange 35 until 44 is about FOR LOOP


"""


def challange035():

    """
        Ask the user to enter
    their name and then
    display their name
    three times.
    """

    name = input("Enter your nama buddy : ")

    for i in range(0,3):
        print(name)


def challange036():

    """
    Alter program 035 so that it will ask the user to enter their
    name and a number and then display their name that
    number of times.

    """
    name = input("Enter your name buddy : ")
    number = int(input("Enter the number : "))

    for i in range(0,number):
        print(name)


def challange037():

    import math
    """
      Ask the user to enter their name and display each letter in 
    their name on a separate line.

    """

    name = input("Enter your name buddy : ")


    for i in range(0, len(name)):
        print(name[i])





def challange038():

    import math

    """
        Change program 
    037 to also ask for a 
    number. Display 
    their name (one 
    letter at a time on 
    each line) and 
    repeat this for the 
    number of times 
    they entered. 

    """

    name = input("Enter your name buddy :")

    number = int(input("Enter the number : "))

    for i in range (0, number):
        for x in name:
            print(x)


def challange039():

    import math

    """
        Ask the user to enter a number between 1 
    and 12 and then display the times table for 
    that number. 
    """
    number = int(input("Enter the number between 1 and 12\n"))

    for i in range(1,13):
        answer = i * number
        print(i, "x", number, "=", answer)


def challange040():

    import math

    """
          Ask for a number below 50 and then count down from 
    50 to that number, making sure you show the number 
    they entered in the output.

    """
    num = int(input("Enter a number below 50 : "))

    for i in range(50, num-1, -1):

        print(i)


def challange041():

    """
                Ask the user to enter their
        name and a number. If the
        number is less than 10, then
        display their name that
        number of times; otherwise
        display the message “Too
        high” three times.

    """

    name = input("Enter your name : ")
    number = int(input("Enter the number : "))

    if number < 10:
        for i in range(0, number):
            print(name)
    else:
        print("Too high")



def challange042():

    """

       Set a variable called total to 0. Ask the user to enter
    five numbers and after each input ask them if they
    want that number included. If they do, then add the
    number to the total. If they do not want it included,
    don’t add it to the total. After they have entered all five
    numbers, display the total.


    """

    total = 0

    for i in range(0, 5):
        num = int(input("Enter a number : "))
        ans = input("Do you want this number to be included ? (y/n) ")

        if ans == 'y':
            total += num

    print(total)


def challange043():

    """

        Ask which direction the user wants to count (up or down). If they select up, then ask
    them for the top number and then count from 1 to that number. If they select down, ask
    them to enter a number below 20 and then count down from 20 to that number. If they
    entered something other than up or down, display the message “I don’t understand”.


    """

    direction = input("Do you want to count up or down ? (u/d) : ")

    if direction == 'u':
        num = int(input("What is the top number ? "))
        for i in  range(1, num+1):
            print(i)
    elif direction == 'd':
        num = int(input("Enter a number below 20 : ? "))
        for i in range(20, num-1, -1):
            print(i)

    else:
        print("I don't understand ")


def challange044():

    """
            Ask how many people the user wants to invite to a party. If they enter a number below
    10, ask for the names and after each name display “[name] has been invited”. If they
    enter a number which is 10 or higher, display the message “Too many people”.



    """

    people = int(input("How many people do you want to invite : "))

    if people < 10:
        for i in range(0, people):
            name = input("Enter the name you want to invite : ")

            print(name, "has been invited")
    else:
        print("Too many people. ")


def main():


    #challange035()
    #challange036()
    #challange037()
    #challange038()
    #challange039()
    #challange040()
    #challange041()
    #challange042()
    #challange043()
    challange044()







if __name__ == "__main__":
    main()
