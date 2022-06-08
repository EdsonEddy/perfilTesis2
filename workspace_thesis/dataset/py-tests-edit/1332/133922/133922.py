a=input()
a=a.lower()
v='aeiouy'
for i in a:
        if i not in v:
                print(".",end="")
                print(i,end="")