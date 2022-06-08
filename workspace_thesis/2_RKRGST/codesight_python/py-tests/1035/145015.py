x=input()
while x!='#':
    n=x.replace("%","%25")
    n=n.replace("!","%21")
    n=n.replace("$","%24")
    n=n.replace(" ","%20")
    n=n.replace("(","%28")
    n=n.replace(")","%29")
    n=n.replace("*","%2a")
    print(n)
    x=input()
        