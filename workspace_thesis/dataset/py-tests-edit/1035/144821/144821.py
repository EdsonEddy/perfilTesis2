while(True):
    a=input("")
    if(a=="#"):
        break
    a=a.replace("%","%25")
    a=a.replace(" ","%20")
    a=a.replace("!","%21")
    a=a.replace("$","%24")
    a=a.replace("(","%28")
    a=a.replace(")","%29")
    a=a.replace("*","%2"+"a")
    print(a)