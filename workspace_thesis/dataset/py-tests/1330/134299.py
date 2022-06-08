x,y=map(str,input().split())
y=int(y)
aux = x[0:len(x)-y]
x = x[len(x)-y:]
print(x+aux)
