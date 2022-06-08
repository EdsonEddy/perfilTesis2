def factorial(x):
    f=1
    for i in  range(1,x+1):
        f=f*i
    return f
for i in range(1,(int(input()))+1):
    if i%2==1:
        print(factorial(i)*-1)
    else:
        print(factorial(i))