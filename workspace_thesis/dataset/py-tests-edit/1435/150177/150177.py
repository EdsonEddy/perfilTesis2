f = lambda n, k : (len(n), n[int(k)-1])
print(*f(*input().split()))