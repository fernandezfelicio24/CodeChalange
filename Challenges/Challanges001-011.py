

def challange001():

    """
    Ask for the user's first name and display the ouput message
    """

    name = input("What's is your first name : ")
    print(f"Hello {name}")


def challange002():

    """

    Ask for the user's first name and then ask for their surname and display the output message
    """

    name = input("What's you first name : ")
    surname = input("What's your surname : ")

    print(f" Hello {name} {surname}")


def challange003():

    """

    Write code that will display the joke "What do you call a bear with no teeth?" and on the next line display the answer
    " A gummy bear !" Try ti create it using only one line of code
    """
    print("What do you call a bear with no teeth ? \nA gummy bear !")


def challange004():

    """
    Ask the user to enter two numbers. Add the together and display the answer as "The total is"

    """
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    sum = num1 + num2

    print(f"The total is {sum}")


def challange005():

    """

    Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third.
    Display the answer as "The answer is "
    """
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    num3 = int(input("Enter the third number : "))

    sum = num1 + num2

    mul = sum * num3

    print(f"The answer is {mul}")



def challange006():

    """
    Ask how many slices of pizza the user started with and ask how many slices they have eaten.
    Work out how many slices they have left and display the answer in a user-friendly format

    """

    num1 = int(input("How many slices of pizza do you started : "))
    num2 = int(input("How many slices of pizza have you eaten : "))
    result = num1 - num2

    print(f"You have only {result} slices of pizza")



def challange007():

    """

    Ask the user for their name and their age. Add 1 to their age and display the output "[Name] next birthday you will be [new age]
    """

    name = input("What is your name : ")
    age  = int(input("What is your age : "))

    nextage = age + 1

    print(f"{name} next birthday you will be {nextage}")




def challange008():

    """

    Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of
    dinners there are. Divide the total bill by the number of dinners and show how much each person must pay
    """
    total = int(input("Total price of the bill : "))

    totaldiner = int(input("Total of the dinner : "))

    divide = total / totaldiner

    print(f"Each person much pay ${divide}")

def challange009():

    """

    Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that
    number of days
    """

    days = int(input("Enter the number of days : "))

    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(f"In, {days} there are ... ")
    print(hours, "hours")
    print(minutes, "minutes")
    print(seconds, "seconds")


def challange010():

    """

    There are 2,204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it to pounds
    """
    kilo = int(input("Enter the number of kilos : "))
    pound = kilo * 2.204

    print("That's", pound, "pounds")



def challange011():

    """

    Task the user to enter a number over 100 an then enter a number under 10 and tell them how many times the smaller
    number goes into the larger number in a user-friendly format.
    """
    larger = int(input("Enter a number over 100 : "))
    smaller = int(input("Enter a number under 10 : "))

    answer = larger//smaller

    print(smaller, "goes into", larger, answer, "times")





def main():

    #challange001
    #challange002()
    #challange003()
    #challange004()
    #challange005()
    #challange006()
    #challange007()
    #challange008()
    #challange009()
    #challange010()
    challange011()
    #paijocalculator()





if __name__ == "__main__":
    main()
