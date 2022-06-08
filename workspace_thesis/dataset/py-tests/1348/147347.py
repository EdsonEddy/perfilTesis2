unid=["unu","du","tri","kvar","Kvin","ses", "Sep","OK","Nau"] 
dec=["dek","dudek","tridek","kvardek","Kvindek","sesdek","Sepdek","OKdek","Naudek"]
while True:
    s=""
    n=int(input())
    if n>=1 and n<=9:
        h=n-1
        print(unid[h])
    else:
        if 10<=n and n<=99:
            f=n%10
            n=n//10
            f=f-1
            n=n-1
            if f==(-1):
                s=s+dec[n]
                print(s)
            else:
                s=s+dec[n]+" "+unid[f]
                print(s)
            s=""
                
        