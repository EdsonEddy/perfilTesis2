n=input()
n2=n.lower()
n1=n2.find('oro')
if n1==(-1):
    print(-1)
else:
    print(n1,"{:1}".format(n1+2))
