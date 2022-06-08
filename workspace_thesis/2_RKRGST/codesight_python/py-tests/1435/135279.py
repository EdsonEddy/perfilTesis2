import math
n, k = map(int, input().split(" "))
tam = int(math.log10(n)) + 1
ind = tam - k + 1
cd = 1
print(tam, end = " ")
while(n > 0):
    if(cd == ind):
        print(n % 10)
        break
    n//=10
    cd+=1
