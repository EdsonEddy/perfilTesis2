def primo(x):
    l = int(x/2+1)
    p = True
    for i in range(2,l):
        if x%i==0:
            p = False
            break
    return p
x = int(input())
while x>0:
    if primo(x):
        print('ES PRIMO')
    else:
        print('NO ES PRIMO')
    x = int(input())
