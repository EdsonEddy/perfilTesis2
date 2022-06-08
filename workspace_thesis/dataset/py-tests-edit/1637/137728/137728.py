while True:
    a,b,c = map(int,input().split())
    x,y,z = map(int,input().split())
    pr = a+x==5 and b+y==5 and c+z == 5
    if pr:
        print('Esta es la llave')
    else:print('Intenta con otra')