def reverseArray(arr, start, end, length):
    while start > end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1

length = int(input())
arr = [int(i) for i in input().split()]

reverseArray(arr, 0, length - 1,length)
print(*arr)