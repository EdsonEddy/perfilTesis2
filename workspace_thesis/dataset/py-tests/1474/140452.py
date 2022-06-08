from sys import stdin, stdout
a=input()
v1=a.split(" ")
n=int(v1[0])
cad1=stdin.readline()
cad2=stdin.readline()
c1=cad1.split(" ")
c2=cad2.split(" ")
for i in range (n):
    c1[i]=int(c1[i])
    c2[i]=int(c2[i])
for i in range (n):
    a=stdin.readline()
    v1=a.split("\n")
    if(v1[0]=="+"):
        print(str(c1[i]+c2[i]))
    elif(v1[0]=="*"):
        print(str(c1[i]*c2[i]))
    elif(v1[0]==">"):
        print(str(max(c1[i],c2[i])))
    elif(v1[0]=="<"):
        print(str(min(c1[i],c2[i])))