lst=""
while lst !="#":
    lst=input()
    x=lst
    if lst=="#":
        break
    x=x.replace("%","%25")
    x=x.replace(" ","%20")
    x=x.replace("!","%21")
    x=x.replace("$","%24")
    x=x.replace("(","%28")
    x=x.replace(")","%29")
    x=x.replace("*","%2a")
    print(x)
    x=""