from os import *
from sys import *
from collections import *
from math import *

x, n = map(int,input().split())

ans = 1

while n > 0:
    ans = ans * x

    n = n - 1

print(ans)
