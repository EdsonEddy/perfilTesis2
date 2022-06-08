while 2>0:
    a=int(input())
    l=["unu","du","tri","kvar","Kvin","ses","Sep","OK","Nau"]
    l2=["dek","dudek","tridek","kvardek","Kvindek","sesdek","Sepdek","OKdek","Naudek"]
    if a>10 and a%10>0:
        print(l2[a//10-1]+" "+l[a%10-1])
    elif a<10:
        print(l[a-1])
    else:
        print(l2[a//10-1])