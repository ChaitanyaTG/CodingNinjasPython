def firstIndex(arr, n, target):
    index = -1

    for i in range(n):
        if arr[i] == target:
            return i
    return -1

length = int(input())
target = int(input())

arr = [int(i) for i in input().split()]

print(firstIndex(arr,length, target))
