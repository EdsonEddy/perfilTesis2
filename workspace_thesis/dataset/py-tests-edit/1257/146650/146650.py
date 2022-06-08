casos=int(input())
for i in range(casos):
    a=input()
    b=input()
    k=list(a)
    while " " in k:
        k.remove(" ")
    kk=list(b)
    while " " in kk:
        kk.remove(" ")
    k.sort()
    kk.sort()
    if k==kk:
        print("Si")
    else:
        print("No")