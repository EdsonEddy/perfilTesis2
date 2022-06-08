n = int(input())
v = list(map(int, input().split()))
a = [v[i] for i in range(len(v))]
a.reverse()
if(a == v):
    print("SI")
else:
    print("NO")
