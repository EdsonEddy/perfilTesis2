def isPalindrome(arr):
    for i in range(0, int(len(arr) / 2)):
        if arr[i] != arr[len(arr) - 1 - i]:
            return print('NO')

    return print('SI')

n= int(input())
g= []
s= input().split()
for i in s:
    g.append(i)
isPalindrome(g)