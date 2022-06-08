
def mayor(a,b,c):
      may=0
      if a>=b and a>=c:
            may=a
      else:
            if b>=a and b>=c:
                  may=b
            else:
                  may=c
      return may

n=int(input())
b=input()
A='ABC'
E='BABC'
G='CCAABB'
f=0
d=0
y=0
for i in range(n):
      c=i%3
      if b[i]==A[c]:
            f=f+1
for j in range(n):
      c=j%4
      if b[j]==E[c]:
            d=d+1
for g in  range(n):
      c=g%6
      if b[g]==G[c]:
            y=y+1
l=mayor(f,d,y)
if l==d and d==f and f==y:
      print(l)
      print('Alvaro')
      print('Edwin')
      print('Gabriel')
else:
      if l==f and f==d:
            print(l)
            print('Alvaro')
            print('Edwin')
      else:
            if l==f and f==y:
                  print(l)
                  print('Alvaro')
                  print('Gabriel')
            else:
                  if l==d and d==y:
                        print(l)
                        print('Edwin')
                        print('Gabriel')
                  else:
                        if l==f:
                              print(l)
                              print('Alvaro')
                        else:
                              if l==d:
                                    print(l)
                                    print('Edwin')
                              else:
                                    print(l)
                                    print('Gabriel')