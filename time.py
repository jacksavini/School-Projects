#Jack Savini
#time class project
#Prof. Sauerberg
#3-10-20

#This is a class which represents time on a standard base 60 interval. It has methods
#which allow two different times to be added together, or simply one Time variable
#and one float or int which represents hours. 

#This class represents amounts of time in hours and minutes, rounded down by the
#closest minute. 
class Time:

    #This sets the default hours and minutes to 0, but accepts variables for both
    #arguments
    def __init__(self, hour = 0, minute = 0):
        self.hour = hour
        self.minute = minute//1

    #this causes the Time class to print in the form of
    #
    #"<hours> hours and <minutes> minutes"
    def __str__(self):

        #I converted all the hours and minutes into a single variable which tracks
        #the number of minutes only. This makes it easier to print later.
        num_minutes = self.minute + (self.hour * 60)
        
        #This makes the class print what I want when used within a print statement.
        return str(int(num_minutes//60)) + " hours and " +\
               str(int(num_minutes % 60)) + " minutes"

    #This add method adds either two time classes or one time class and one float/int.
    #It returns a new time data type.
    def __add__(self, other):

        #If the second variable is not a Time data type, it converts it to one.
        if type(other) != Time:
            other = Time(other)

        #These add the minutes and hours together
        new_hour = self.hour + other.hour
        new_minute = self.minute + other.minute

        #returns the correct output
        return Time(new_hour, new_minute)

    #This right here is in case the first argument is not a Time variable. If so, it
    #reverses self and other and then does the add method.
    def __radd__(self, other):
        return self.__add__(other)

time0 = Time()
time1 = Time(6)
time2 = Time(3,30)
time3 = Time(30,75)
time4 = Time(3.5)
