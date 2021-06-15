#Jack Savini
#CS 102
#Prof. Saurberg
#3-3-20
#heading towards nothing project

#I'll need the randint function to make my list
from random import *

#This function asks for an integer, and then spits out a list with that number
#of random elements from 0 to 99
def initial():

    integer = eval(input("Please input an integer: "))
    print("")

    #This checks to see if the input is positive
    while integer <= 0:
        integer = eval(input("Please input a positive integer: "))
        print("")

    #This checks to see if the input is an int, and if not makes it one
    if type(integer) == float:
        integer //= 1
        integer = int(integer)

    #I made two lists, one which can change and one to maintain the original
    #set of numbers.
    new_list = []
    original_list = []

    #This handy dandy for loop makes my list
    for i in range(integer):
        rand_num = randint(0,99)
        new_list.append(rand_num)
        original_list.append(rand_num)

    return original_list, new_list

#The update function takes a list and spits out a new one made up of the
#difference between adjacent elements
def update(new_list):

    #This helps in making a more semless for loop below
    new_list.append(new_list[0])

    new_new_list = []

    #This loops looks at adjacent elements, and adds their difference to a new
    #list
    for i in range(len(new_list)-1):
        new_num = abs(new_list[i] - new_list[i+1])
        new_new_list.append(new_num)

    return new_new_list

#The round function asks for a new integer, and then continues the program for
#that many more number of steps
def round():

    rounds = eval(input("Input how many more rounds you would like: "))
    print("")

    #this error checks for negatives
    while rounds < 0:
        rounds = eval(input("Please input a positive integer or zero: "))
        print("")

    #this error checks for floats
    if type(rounds) == float:
        rounds //= 1
        rounds = int(rounds)

    return rounds

#The finished function checks to see if the list is all 0s, and if so, returns
#a boolean True
def finished(new_list):

    for i in new_list:
        if i != 0:
            return False

    return True

def main():

    #This makes the original list
    original_list, new_list = initial()

    #rounds must start greater than 0 so the loop knows to not be finished
    #num rounds keeps track of how many rounds have run so far
    #new_rounds checks to see if the program should continue running
    rounds = 1
    num_rounds = 0
    new_rounds = True

    #This loop continues as long as there are rounds left AND as long as the
    #list is not all zeros
    while new_rounds == True and finished(new_list) == False:

        #This prints the list, and asks how many more rounds
        print("After", num_rounds, "rounds, The current list is", new_list)
        print("")
        rounds = round()

        #If the user inputs 0, the loop stops
        if rounds == 0:
            new_rounds = False

        #This updates the list however many times indicated, updating the final
        #tally of rounds as it does so
        while rounds > 0 and finished(new_list) == False:
            new_list = update(new_list)
            rounds -= 1
            num_rounds += 1

    #This reminds of the original list
    print("The original list was", original_list)
    print("")

    #This prints the nunmber of rounds and the final list.
    print("After", num_rounds, "rounds, The final list is", new_list)

main()

#Question 10:

#From what I can tell from running my program a million times with different
#lengths of lists, the numbers only converge on zero when the length is a
#power of 2. So this converging to zero works for squares, octagons,
#hexadecagons, triacontadigons, so on and so forth.
