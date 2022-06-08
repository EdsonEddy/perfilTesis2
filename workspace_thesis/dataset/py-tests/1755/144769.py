t = int(input())
for _  in range(t):
    n, f = list(map(int, input().split()))
    sol = [1] * f
    for i in range(f, n+1):
        c = sum(sol[i-f: i])
        sol.append(c)
        
    print(sol[n])