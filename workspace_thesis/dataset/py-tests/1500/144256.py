m = int(input())
a = list(map(int, input().split()))
aux = [a[i] for i in range(len(a))]
aux.reverse()
if(aux == a):
    print("SI")
else:
    print("NO")
