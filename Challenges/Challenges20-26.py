"""
Challange 20 until 26 is about String


"""


def challange020():

    """
    Ask the user to enter
    their first name and
    then display the
    length of their name.

    """

    firstname = input("Enter the first name : ")

    lenfirstname = len(firstname)

    print(f"The length of your first name is : {lenfirstname}")


def challange021():

    """
    Ask the user to enter their first name and then ask them to
    enter their surname. Join them together with a space between
    and display the name and the length of whole name.

    """


    firstname = input("Enter the first name  : ")

    surname = input("Enter the surname  : ")

    name = firstname + " " + surname

    length = len(name)
    print("Length of your complete name is ", length)

def challange022():

    """
        Ask the user to enter their first name and surname in lower
    case. Change the case to title case and join them together.
    Display the finished result.

    """



    firstname = input("Enter the first name : ")

    surname = input("Enter the surname : ")

    firstname = firstname.title()
    surname = surname.title()
    name = firstname + " " + surname
    print(name)



def challange023():

    """
                    Ask the user to type in the first
            line of a nursery rhyme and
            display the length of the string.
            Ask for a starting number and an
            ending number and then display
            just that section of the text
            (remember Python starts
            counting from 0 and not 1).

    """

    pharase = input("Enter the first line of a nursery rhyme : ")
    lenght = len(pharase)
    print("This has", lenght, "letters in it ")
    start = int(input("Enter a starting number : "))
    end = int(input("Enter an end number : "))
    part = (pharase[start:end])
    print(part)


def challange024():

    """
        Ask the user to enter their first name and surname in lower
    case. Change the case to title case and join them together.
    Display the finished result.
    """
    words = input("Enter any word : ")

    upperword = words.upper()

    print(upperword)



def challange025():

    """
                Ask the user to enter their first name. If the length
        of their first name is under five characters, ask
        them to enter their surname and join them
        together (without a space) and display the name
        in upper case. If the length of the first name is five
        or more characters, display their first name in
        lower case.


    """


    firstname = input("Enter the first name my friend : ")

    lenfirstname = len(firstname)

    if lenfirstname < 5:
        surname = input("Enter the surname my dear friend")

        completename = firstname + surname

        upercomplete = completename.upper()

        print(upercomplete)


    else:

        lowerfirstname = firstname.lower()

        print(lowerfirstname)

def challange026():

    """
            Pig Latin takes the first consonant of a word,
        moves it to the end of the word and adds on an
        “ay”. If a word begins with a vowel you just add
        “way” to the end. For example, pig becomes igpay,
        banana becomes ananabay, and aadvark becomes
        aadvarkway. Create a program that will ask the
        user to enter a word and change it into Pig Latin.
        Make sure the new word is displayed in lower case.
    """


    word = input("Enter any word that you like most : ")

    first = word[0]
    length = len(word)
    rest = word[1:length]
    print(rest)
    if first != "a" and first != "e" and first != "i" and first != "o" and  first != "u":
        neword = rest + first + "ay"
    else:
        neword = word + "way"
    print(neword.lower())



def main():


    #challange020()
    #challange021()
    #challange022()
    #challange023()
    #challange024()
    #challange025()
    challange026()








if __name__ == "__main__":
    main()
