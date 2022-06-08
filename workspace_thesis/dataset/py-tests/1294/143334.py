t = int(input())
while(t):
    t -= 1
    n, a, b = map(int,input().split())
    A = []  
    while(len(A)<n):
        A += [int(i) for i in input().split()]          
    print(sum(A[a:b+1]))