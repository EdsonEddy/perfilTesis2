var = int(input())
n = 1
d = 1
barra = "/"
while n <= var and d<=var:
    print(str(n) + barra +str(d))
    d+=1
    #print(str(n) + barra +str(d))
    if d == var:
        print(str(n) + barra + str(d))
        n+=1
        d-=(var-1)
        #print(str(n) + barra + str(d))
        if n > var:
            break