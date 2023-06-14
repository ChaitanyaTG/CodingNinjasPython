from os import *
from sys import *
from collections import *
from math import *

from sys import stdin


def countWords(string):
    if len(string) == 0:
        return 0
    count = 0

    for i in string:
        if i == " ":
            count = count + 1
    return count + 1


string = stdin.readline().strip()
count = countWords(string)

print(count)