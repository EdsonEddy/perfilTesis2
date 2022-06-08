import sys
num = ['0','1','2','3','4','5','6','7','8','9']
for i in sys.stdin:
   x = i
   cN = []
   cL = []
   for c in x:
      if c=='\n':break 
      if(c in num):
         cN.append(int(c))      
      elif (c=='+' or c=='*'):
         a=b=0
         if(len(cN)):a = cN.pop()
         if(len(cN)):b = cN.pop()
         if(c=='+'):cN.append(a+b)
         else:cN.append(a*b)
      else:cL.append(c)
   while(len(cL)):
      print(cL.pop(),end='')
   print(': habilidad '+str(cN.pop()))   
