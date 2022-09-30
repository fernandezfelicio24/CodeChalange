"""

Challange 69 until 79 is about TURTLE GRAPHICS


"""
import turtle

def challange069():

    """
        Create a tuple containing the names of five countries and display the whole tuple. Ask
    the user to enter one of the countries that have been shown to them and then display
    the index number (i.e. position in the list) of that item in the tuple.

    """

    countries = ("Timor Leste", "Indonesia", "Australia", "Japan", "Korea")

    for i in range(len(countries)):
        print(countries[i])

    country = input("Enter a one of the countries that you have seen : ")

    for i in range(len(countries)):

        if countries[i] == country:

            print(f"The index of country is {i}")

        else:

            print(f"The country you have enter {country} is not on tuple")
            break

def challange070():

    """
            Add to program 069 to ask the
    user to enter a number and
    display the country in that
    position.

    """
    countries = ("Timor Leste", "Indonesia", "Australia", "Japan", "Korea")

    for i in range(len(countries)):
        print(countries[i])

    country_pos = int(input("Enter a number between 0 until 4 : \n"))

    for i in range(len(countries)):

        if i == country_pos:
            print(f"The position {country_pos} is the country of {countries[i]}  ")



def challange071():

    """
        Create a list of two sports. Ask the
    user what their favourite sport is and
    add this to the end of the list. Sort the
    list and display it.

    """





    list_sport = ["soccer", "jiu-jitsu"]

    list_sport.append(input("What is your favourite sports : "))
    list_sport.sort()
    print(list_sport)

def challange072():



    """
            Create a list of six school subjects. Ask the user which of these
    subjects they don’t like. Delete the subject they have chosen from the
    list before you display the list again.
    """

    subjects = ["Math", "Art", "Biology", "Geology", "History", "Chemistry"]

    print(subjects)

    dislike = input("Which subject do hate the most : ")

    getrid = subjects.index(dislike)

    del subjects[getrid]

    print(subjects)

def challange073():



    """
    Ask the user to  enter four of their  favourite foods
    and store them in a dictionary so that they are indexed with
    numbers starting from 1. Display the dictionary in full, showing the
    index number and the item. Ask them which they want to get rid of
    and remove it from the list. Sort the remaining data and display
    the dictionary.

    """

    food_dictionary = {}

    food1 = input("Enter a food you like : ")

    food_dictionary[1] = food1

    food2 = input('Enter another food you like : ')

    food_dictionary[2] = food2

    food3 = input('Enter a third food you like : ')

    food_dictionary[3] = food3

    food4 = input('Enter one last food you like : ')

    food_dictionary[4] = food4

    print(food_dictionary)

    dislike = int(input("Which of these do you want to get rid of, enter the index of food"))

    del food_dictionary[dislike]

    print(sorted(food_dictionary.values()))



def challange074():

    """
            Enter a list of ten colours.
        Ask the user for a starting
        number between 0 and 4
        and an end number
        between 5 and 9. Display
        the list for those colours
        between the start and end
        numbers the user input.
    """

    colours = ["red", "blue", "green", "black", "white", "pink", "grey", "purple", "yellow", "brown"]

    print(colours)

    start = int(input("Enter a starting number (0 -4 ) : "))

    end = int(input("Enter an end number ( 5-9) : "))

    print(colours[start:end])






def challange075():

    """
            Create a list of four three-digit
    numbers. Display the list to the
    user, showing each item from
    the list on a separate line. Ask
    the user to enter a three-digit
    number. If the number they
    have typed in matches one in
    the list, display the position of
    that number in the list,
    otherwise display the message
    “That is not in the list”.

    """

    list_digit = [492, 260, 358]


    for i in list_digit:
        print(i)

    selection = int(input("Enter a number from the list : "))

    if selection in list_digit:
        print(selection,"is in position", list_digit.index(selection))

    else:
        print("That is not in the list")

def challange076():

    """
        Ask the user to enter the names of three people they want to
    invite to a party and store them in a list. After they have entered
    all three names, ask them if they want to add another. If they do,
    allow them to add more names until they answer “no”. When
    they answer “no”, display how many people they have invited to
    the party.

    """


def challange077():

    """
            Change program 076 so that once the user has completed their list of names, display the
    full list and ask them to type in one of the names on the list. Display the position of that
    name in the list. Ask the user if they still want that person to come to the party. If they
    answer “no”, delete that entry from the list and display the list again.

    """


def challange078():

    """
        Create a list containing the titles of
    four TV programmes and display
    them on separate lines. Ask the
    user to enter another show and a
    position they want it inserted into
    the list. Display the list again,
    showing all five TV programmes in
    their new positions.

    """


def challange079():

    """
            Create an empty list called “nums”.
    Ask the user to enter numbers.
    After each number is entered, add
    it to the end of the nums list and
    display the list. Once they have
    entered three numbers, ask them if
    they still want the last number they
    entered saved. If they say “no”,
    remove the last item from the list.
    Display the list of numbers.

    """



def main():

    #challange069()
    #challange070()
    #challange071()
    #challange072()
    #challange073()
    #challange074()
    challange075()
    #challange076()
    #challange077()
    #challange078()
    #challange079()





if __name__ == "__main__":
    main()
