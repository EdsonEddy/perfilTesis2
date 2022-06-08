def esP(palabra):
    if palabra==palabra[::-1]:
         return True
    else:
         return False

while True:
    try:
       t=int(input())
       c=0
       while t > 0:
          t-=1
          n=int(input())
          if esP(str(n)):
              c+=1
       print(c)
    except ValueError:
        break