from sys import stdin
for line in stdin:
    lis = list(map(int, input().split()))
    lis.sort()
    c = i = 0
    while i < (int(line)-1):
        if lis[i] == lis[i+1] :
            c += 1
            i += 1
        i += 1
    print(c)
