ls = [2,4,8,7,5,1]
casos = int(input())
for j in range(casos):
    x = int(input())
    print(ls[x%6])