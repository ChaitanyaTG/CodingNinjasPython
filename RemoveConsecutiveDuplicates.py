from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def removeConsecutiveDuplicates(string):
    n = len(string)

    if n == 0:
        return string

    answer = string[0]
    i = 1

    while i < len(string):
        if string[i] != string[i - 1]:
            answer = answer + string[i]

        i = i + 1

    return answer

string = stdin.readline().strip()
ans = removeConsecutiveDuplicates(string)
print(ans)

