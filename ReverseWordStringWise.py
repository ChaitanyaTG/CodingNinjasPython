def reverseStringWordWise(string):
    string = string.split()
    i = 0
    j = len(string) - 1

    while i < j:
        string[i],string[j] = string[j],string[i]
        i = i + 1
        j = j -1
    answer = ""

    for i in string:
        answer = answer + 1
        answer = answer + " "
    return answer

string = input()
ans = reverseStringWordWise(string)
print(ans)