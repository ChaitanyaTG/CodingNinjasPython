from os import *
from sys import *
from collections import *
from math import *

def firstIndex(arr, n, target):
    index = -1
    for i in range(n -1,-1,-1):
        if arr(i) == target:
            index = i
            break
    return index

length = int(input())
arr = [int(i) for i in input().split()]
target = int(input())

print(firstIndex(length, arr, target))