from sys import stdin
for n in stdin:
    n = int(n)
    v = list(map(int, input().split()))
    if(n <= 2):
        print(0)
    else:
        cd = 0
        for i in range(1,n-1):
            if(v[i] < v[i - 1] and v[i] < v[i + 1]):
                cd+=1
            if(v[i] > v[i - 1] and v[i] > v[i + 1]):
                cd+=1
        print(cd)
            
