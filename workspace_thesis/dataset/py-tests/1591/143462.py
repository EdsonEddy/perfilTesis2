d= int(input())
for x in range (d):  
    a=input()
    c=""
    for b in a:
        if b=="2" or b=="3" or  b=="5" or b=="7":
            c=c+b
    if len(c)==0:
        print("-1")
    else:
        print(c)