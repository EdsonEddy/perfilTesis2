def Farey(k):
    for i in range (1,k+1):
        for j in range (1,k+1):
            print(str(i)+'/'+str(j))
n=int(input())
if 1 <= n <= 100 :
    Farey(n)
