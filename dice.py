#Jack Savini
#CS 102
#dice game python project

from random import *

#Introduction to the game
def intro():

    #Setting up the initial score board numbers
    score = 0
    turns = 0

    name = input("Enter your name: ")
    print("")

    #tutorial

    
    return score, name, turns

def turn(name, score, turns):

    turns += 1

    #This is used as a parameter for the while loop below
    stop = 'Y'

    #new_score is the score added to the players intial score input
    #into the turn function
    new_score = 0

    print("ROUND " + str(turns) + "!!!!!!")
    print("")
    
    while stop != 'N':

        #Quick update on the person's score
        print(name + ", your score is", score + new_score)
        print("")

        stop = input("Would you like to continue this turn? [Y/N]:")

        #In case the person chooses to lock in their score
        if stop == 'N':
            print("____________________________________________________")
            print("")
            return score + new_score, turns
        
        print("")

        
        if stop != 'N':

            #I do two dice rolls and find the sum
            rand_num_a = randint(1,6)
            rand_num_b = randint(1,6)
            fin_num = rand_num_a + rand_num_b

            print("The dice rolled a", rand_num_a, "and a", rand_num_b, ".")
            print("")

            #In the person doesn't bust, they get the number added to their score
            if fin_num != 2 and fin_num != 7 and fin_num != 12:
                new_score += fin_num

            else:
                #If the person busts, they lose their new points and start over.
                print("Oh no!", name + ", you rolled a", (fin_num), "! Your score"
                " is now", score, ", and you must start a new round.")
                print("____________________________________________________")
                print("")
                return score, turns

    print("")

#This function takes in data and spits out print statements announcing the winner.
def final_score(name, turns):
    print("Congratulations " + name + "! You won in", turns, "rounds!")
    
#The main function puts all the other functions together and runs them in order.
def main():
    score, name, turns = intro()

    while score < 100:
        score, turns = turn(name, score, turns)


    final_score(name, turns)
        
main()
