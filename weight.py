#Jack Savini
#CS 102 Spring 2020
#February 13 2020
#Program: Weights

'''
Asks the user to input two people's weights in pounds. Translates them
to kg and 'stone
'''


#Tutorial Print
print("This Program Asks the user to input two people's weights in pounds and translates them to kg and stone")
print("")

#Get the subject's name and weight in pounds
person_1 = input("Input the name of person #1: ")
weight_1 = int(input("Input " + person_1 + "'s weight in pounds: "))

print("")

#Convert pounds to kilograms for later
kilograms_1 = weight_1 / 2.2046

#Give the results of my scientific/mathematical analysis
print(person_1 + "'s weight is", int(weight_1//14), "stone and", weight_1%14, "pound, or %.2f kg." %(kilograms_1))

print("")

#Repeat for person #2, I don't feel I need to explain a second time
person_2 = input("Input the name of person #2: ")
weight_2 = int(input("Input " + person_2 + "'s weight in pounds: "))

print("")

kilograms_2 = weight_2 / 2.2046

print(person_2 + "'s weight is", int(weight_2//14), "stone and", weight_2%14, "pound, or %.2f kg." %(kilograms_2))

print("")

#Now give the average of the two peoples weights in pounds
print("The average weight in pounds of " + person_1 + " and " + person_2 + " is %.2f lbs." %((weight_1+weight_2)/2))

#Now in Stone
print("The average weight in stone of " + person_1 + " and " + person_2 + " is", int((((weight_1+weight_2)/2)//14)), "stone and %.2f lbs." %(((weight_1+weight_2)/2)%14))

#Now in kg
print("The average weight in kilograms of " + person_1 + " and " + person_2 + " is %.2f kgs." %(((weight_1+weight_2)/2)/2.2046))

print("")
print("Thanks for playing!")
