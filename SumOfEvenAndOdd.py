n = int(input())

evensum = 0
oddsum = 0

while n > 0:
    last = n % 10

    if n % 2 == 0:
        evensum += last

    else:
        oddsum += last

    n = n // 10

print(evensum, oddsum)