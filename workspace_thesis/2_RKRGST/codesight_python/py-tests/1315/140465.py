from sys import stdin, stdout
n=int(input(""))
cad1=stdin.readline()
c1=cad1.split(" ")
c2=[n]
#c1.remove("\n")
#print("--------------------------------")
for i in range(n):
        if(i==0):
            print(c1[0],end="")
        else:
            a=int(c1[i])-int(c1[i-1])
            print("",a,end="")