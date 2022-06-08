x=input()
x=x.lower()
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="y" or i=="o" or i=="u":
        print(end="")
    else:
        print("."+i,end="")