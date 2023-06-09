from os import *
from sys import *
from collections import *
from math import *

def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    string1 = sorted(string1)
    string2 = sorted(string2)

    i = 0
    j = 0

    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            return False
        i = i + 1
        j = j + 1

    return True
string1 = input()
string2 = input()

ans = isPermutation(string1, string2)

if ans:
    print('True')

else:
    print('False')



