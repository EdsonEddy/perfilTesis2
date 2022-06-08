a=input()
abc="abcdefghijklmnopqrstuvwxyz"
for i in abc:
    if i not in a:
        print(i)
        break
    elif i=="z" and i in a:
        print(-1)
        break