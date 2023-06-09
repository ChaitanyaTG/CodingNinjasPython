from os import *
from sys import *
from collections import *
from math import *

def totalPrime(S, E):
    count = 0
    for i in range(S, E + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break

        if flag:
            count = count + 1
    return count

S, E = map(int,input().split(' '))
print(totalPrime(S,E))


