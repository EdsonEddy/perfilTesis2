import sys
for j in sys.stdin:
    num=int(j)
    cont=0
    sumapares=0
    sumaimpares=0
    while(num>0):
        dig=num%10
        cont=cont+1
        num=num//10
        if(cont%2==0):
            sumapares=sumapares+dig
        else:
            sumaimpares=sumaimpares+dig
    if(sumapares==sumaimpares):
        print("SI")
    else:
        print("NO")