from os import *
from sys import *
from collections import *
from math import *

S = int(input())
E = int(input())
W = int(input())

for CurrentFarhenheitValue in range(S, E + 1, W):
    celsius = int((CurrentFarhenheitValue - 32) * 5 / 9)
    print(CurrentFarhenheitValue, celsius, sep = '\t')