a, b, c = map(int,input().split())
men = min(a, b, c)
may = max(a, b, c)
med = (a+b+c)-may-men
print(men, med, may)