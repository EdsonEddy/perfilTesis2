n=input()
while n!=""\
    "":
    sp,si=0,0
    for i in range(len(n)):
        if(i+1)%2!=0:
            si=si+int(n[i])
        else:
            sp=sp+int(n[i])
    if si==sp:
        print("SI")
    else:
        print("NO")
    n=input()