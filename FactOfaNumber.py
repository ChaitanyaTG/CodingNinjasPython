n = int(input())

if n < 0:
    print('error')

else:
    fact = 1

    for i in range(2, n + 1):
        fact = fact * i

    print(fact)