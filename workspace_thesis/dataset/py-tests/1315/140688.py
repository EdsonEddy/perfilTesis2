from sys import stdin,stdout
n=input()
n=int(n)
cad= input()
v1=cad.split(" ")
for i in range(n):
  v1[i]=int(v1[i])
print(v1[0],end="")
for i in range(1,n):
    print("",v1[i]-v1[i-1],end="")
