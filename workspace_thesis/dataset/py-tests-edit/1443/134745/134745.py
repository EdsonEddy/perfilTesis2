i=1
while i==1:
    a=int(input(""))
    s=0
    for j in range(1,a):
        if a%j==0:
            s=s+j
    if s<a:
        print ("Deficiente")
    elif s>a:
        print ("Abundante")
    else: 
        print ("Perfecto")