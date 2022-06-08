import sys
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def find(x):
   for i in range(26):
      if letras[i]==x:
         return i
   return -1
if __name__=='__main__':
   for x in sys.stdin:
      k, x = x.split(' ')
      x = x.upper()
      k = int(k) % 26
      for i in range(len(x)):
         if x[i] in letras:
            pos = (int(find(x[i])) + k) % 26            
            print(letras[pos],end='')
         elif x[i]=='_':
            print(' ',end='')
         else: print(x[i],end='')
      #print()