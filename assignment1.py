# Lina Lange
# ####################################### LOAD REQUIRED LIBRARIES ############################################# #
import time
import os
import math
# ####################################### SET TIME-COUNT ###################################################### #
starttime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print("--------------------------------------------------------")
print("Starting process, time: " + starttime)
print("Author: Lina Lange")
# ####################################### FUNCTIONS ########################################################### #
def square(x):

    ### Function calculates the square of any given number

    ### Parameter
    ### txtPath: number

    ### Returns squared number

    return x**2

def square_root(x):

    ### Function calculates the square root of any given number, unless this number is negative
    ### The square root of 0 is 0

    ### Parameter
    ### txtPath: number

    ### Returns square root of the number

    if x<0:
        print("Error: negative number does not have a square root!")
    else:
        return math.sqrt(x)

# ####################################### PROCESSING ########################################################## #

### calculate square ###
List= [1,2,3,4]
print(list(map(square, List) ))   #map() applies given function to all items in a list

#### calculate square root using math.sqrt####
square_root(-7)
print(square_root(18))

# ####################################### END TIME-COUNT AND PRINT TIME STATS################################## #
endtime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print("--------------------------------------------------------")
print("start: " + starttime)
print("end: " + endtime)
print("I am sorry for handing the assignment in late!")