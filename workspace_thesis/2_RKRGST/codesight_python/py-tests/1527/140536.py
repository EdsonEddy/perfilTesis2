x=int(input())
for i in range(x):
    n=int(input())
    sw=0
    while n>0:
       t=n%100
       n=n//10
       if t==96:
           sw=1
           break
    if sw==1:
        print("APLAZADO!")
    else:
        print("TE SALVAS :D")