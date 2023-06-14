from os import *
from sys import *
from collections import *
from math import *

def printFun(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
n = int(input())
printFun(n)