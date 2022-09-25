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





def challange072():



    """
        Create a list of two sports. Ask the
    user what their favourite sport is and
    add this to the end of the list. Sort the
    list and display it.
    """




def challange073():



    """
        Create a list of two sports. Ask the
    user what their favourite sport is and
    add this to the end of the list. Sort the
    list and display it.

    """



def challange074():

    """
        Create a list of two sports. Ask the
    user what their favourite sport is and
    add this to the end of the list. Sort the
    list and display it.
    """


def challange075():

    """
        Create a list of two sports. Ask the
    user what their favourite sport is and
    add this to the end of the list. Sort the
    list and display it.

    """



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
        Ask the user to enter the names of three people they want to
    invite to a party and store them in a list. After they have entered
    all three names, ask them if they want to add another. If they do,
    allow them to add more names until they answer “no”. When
    they answer “no”, display how many people they have invited to
    the party.

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
        Create a list containing the titles of
    four TV programmes and display
    them on separate lines. Ask the
    user to enter another show and a
    position they want it inserted into
    the list. Display the list again,
    showing all five TV programmes in
    their new positions.

    """



def main():

    #challange069()
    challange070()
    #challange071()
    #challange072()
    #challange073()
    #challange074()
    #challange075()
    #challange076()
    #challange077()
    #challange078()
    #challange079()





if __name__ == "__main__":
    main()
