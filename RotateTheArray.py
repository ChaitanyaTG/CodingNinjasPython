from os import *
from sys import *
from collections import *
from math import *

def rotateArray(arr, n, k):
    for arr in range(k):
        temp = arr[0]

        for j in range(n - 1):
            arr[j] = arr[j + 1]

        arr[n - 1] = temp

length = int(input())
arr = [int(i) for i in input().split()]
k = int(input())

rotateArray(arr, n, k)
print(*arr)