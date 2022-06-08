import sys
a=0
b=1
v = []
for i in range(50):
   v.append(a*a + b*b)
   c = a + b
   a = b
   b = c
if __name__=='__main__':
    for x in sys.stdin:      
      n = int(x)
      for i in range(n):
         print(v[int(input())])
