cd=0
cn=0
may=0
while True:
      n=float(input())
      cd=cd+1
      if(n<0):
        cn=cn+1
      else:
        if(n>may):
            may=n
      if(n==0):
        break
po= int(cn*100)/(cd-1)
po= int (po)
print(po)
may=int(may)
print(may)