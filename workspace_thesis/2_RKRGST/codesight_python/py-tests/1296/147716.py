while True:
   a=int(input())
   lista=[]
   for i in range (a):
      n=input()
      n=n[::-1]
      lista.insert(0,n)
   for i in range(len(lista)):
      print(lista[i])
