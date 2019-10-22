# coding=utf-8
# ############################################################################################################# #                                                       #
# Lingzhi Zhang, Humboldt-Universität zu Berlin, 21/10/2019                                               #
# ####################################### LOAD REQUIRED LIBRARIES ############################################# #
import math
import time
# ####################################### SET TIME-COUNT ###################################################### #
from builtins import list, map

starttime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print("--------------------------------------------------------")
print("Starting process, time: " + starttime)
print("")
# ####################################### FOLDER PATHS & global variables ##################################### #
## none
# ####################################### FUNCTIONS ########################################################### #
def square(x):

    Parameters
    ----------
    txtPath: number
    """ Function to calculate square of number

    Returns
    -------
    squared number
    :param x:
    """
    return x**2
def squareroot(x):
    """ Function to calculate square root of single number, if this number is not negative
    0 also has 0 as its square root

    Parameters
    ----------
    txtPath: number

    Returns
    -------
    square root of the number
    :param x:
    """
    if x<0:
        print("Error: negative number doesn't have square root!")
    else:
        return math.sqrt(x)
# ####################################### PROCESSING ########################################################## #
## task 1
List= [1,2,3,4,5]
print(list(map(square, List) ))
## map()function returns a list of results after applying the given function to each item of a given iterable, like list.
## return type of map()function in python 3 is iterator instead of list.

## task 2
squareroot(-2)
print(squareroot(8))
# ####################################### END TIME-COUNT AND PRINT TIME STATS################################## #
print("")
endtime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
print("--------------------------------------------------------")
print("start: " + starttime)
print("end: " + endtime)
print("")

