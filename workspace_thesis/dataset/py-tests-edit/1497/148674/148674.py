def bina(n):
    binario=''
    while n//2!=0:
        binario=str(n%2)+binario
        n=n//2
    return str(n)+binario

n=input()
k=""
for i in n:
      j=ord(i)
      f=bina(j)
      

      while len(f)!=8:
            f="0"+f
      k=k+f

print(k)