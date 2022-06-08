while True:
   try:
       x=int(input())
       l=['0','unu','du','tri','kvar','Kvin','ses','Sep','OK','Nau']
       if x < 10:
           print(l[x])
       else:
           l1={10:'dek',20:'dudek',30:'tridek',40:'kvardek',50:'Kvindek',60:'sesdek',70:'Sepdek',80:'OKdek',90:'Naudek'}
           d=x//10
           d1=d*10
           d2=x%10
           for e in l1:
               if d1==e:
                   s=l1[e]
                   break
           if x in l1:
               print(s)
           else:
              print(s,l[d2])
   except ValueError:
      break