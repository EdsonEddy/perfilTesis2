x=input()
x=x.lower()
x=x.replace("a","")
x=x.replace("e","")
x=x.replace("i","")
x=x.replace("o","")
x=x.replace("u","")
x=x.replace("y","")
x=x.replace("",".")
x=x[:len(x)-1]
print(x)