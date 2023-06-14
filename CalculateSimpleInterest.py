from os import *
from sys import *
from collections import *
from math import *

Principal_amount = int(input())
Rate = float(input())
Time = int(input())

SI = ((Principal_amount * Rate * Time) / 100)

print(SI)