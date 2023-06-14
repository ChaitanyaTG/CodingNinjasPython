from os import *
from sys import *
from collections import *
from math import *


def printSubstrings(string):
    n = len(string)
    for i in range(n):
        for j in range(i, n):
            for k in range(i, (j + 1)):
                print(string[k], end=" ")
            print()


string = input()
printSubstrings(string)
