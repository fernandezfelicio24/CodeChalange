"""
Challange 12 until 19 is about if statement



"""



def challange012():

    """
            Ask for two numbers. If
        the first one is larger
        than the second, display
        the second number first
        and then the first
        number, otherwise show
        the first number first and
        then the second.

    """

    firstnumber = int(input("Enter the first number :"))
    secondnumber = int(input("Enter the second number : "))

    if firstnumber > secondnumber:
        print(secondnumber, " ", firstnumber)

    else:
        print(firstnumber, " ", secondnumber)


def challange013():

    """
        Ask the user to enter a
        number that is under
        20. If they enter a
        number that is 20 or
        more, display the
        message “Too high”,
        otherwise display
        “Thank you”.


    """
    firstnumber = int(input("Enter the first number :"))

    if firstnumber <= 20:
        print("Thank you, Arigato ")

    else:
        print("To High")

def challange014():

    """
        Ask the user to enter a
    number between 10 and 20
    (inclusive). If they enter a
    number within this range,
    display the message “Thank
    you”, otherwise display the
    message “Incorrect
    answer”.

    """
    firstnumber = int(input("Enter the first number :"))

    if firstnumber >= 10 and firstnumber <= 20:
        print("Thank you")
    else:
        print("Incorrect Answer")


def challange015():

    """

            Ask the user to enter their favourite colour. If they enter “red”, “RED” or
    “Red” display the message “I like red too”, otherwise display the message
    “I don’t like [colour], I prefer red”.

    """

    favcal = input("Enter your favourite Calor :")

    if favcal == "Red" or favcal == "RED" or favcal == "red":
        print("I like red too")
    else:
        print("I don't like ", favcal)


def challange016():

    """
        Ask the user if it is raining and convert their answer to lower case
    so it doesn’t matter what case they type it in. If they answer “yes”,
    ask if it is windy. If they answer “yes” to this second question,
    display the answer “It is too windy for an umbrella”, otherwise
    display the message “Take an umbrella”. If they did not answer yes
    to the first question, display the answer “Enjoy your day”.

    """

    raining = input("Is it Raining :")


    rainlower = raining.lower()

    if rainlower == "yes":

        ifwindy = input("Is it Windy : ")
        lowerwindy = ifwindy.lower()

        if lowerwindy == "yes":

            print("It is windy for an umbrella")
        else:
            print("Take an umbrella")
    else:
        print("Enjoy your day ")



def challange017():

    """
        Ask the user’s age. If they
    are 18 or over, display the
    message “You can vote”, if
    they are aged 17, display the
    message “You can learn to
    drive”, if they are 16, display
    the message “You can buy a
    lottery ticket”, if they are
    under 16, display the
    message “You can go Trickor-Treating”


    """

    age = int(input("How old are you : "))

    if age >= 18:

        print("You can vote")
    elif age == 17:
        print("You can learn to Drive")

    elif age == 16:
        print("You can by lottery ticket ")

    else:
        print("You can go Trick or Treating")


def challange018():

    """
        Ask the user to enter a number. If it is under 10,
    display the message “Too low”, if their number is
    between 10 and 20, display “Correct”, otherwise
    display “Too high”.
    """

    number = int(input("Please enter the number : "))

    if number < 10:
        print("Too low")
    elif number >= 10 and number <= 20:
        print("Correct")
    else:
        print("To high")

def challange019():

    """
        Ask the user to enter 1, 2 or 3. If they enter a 1, display
    the message “Thank you”, if they enter a 2, display
    “Well done”, if they enter a 3, display “Correct”. If
    they enter anything else, display “Error message”.


    """
    number = int(input("Please enter the number 1 or 2 or 3 : "))

    if number == 1 :
        print("Thank you")
    elif number == 2 :
        print("Well done")
    elif number == 3 :
        print("Correct")
    else:
        print("Error message")

def main():


    #challange012()
    #challange013()
    #challange014()
    #challange015()
    #challange016()
    #challange017()
    #challange018()
    challange019()







if __name__ == "__main__":
    main()
