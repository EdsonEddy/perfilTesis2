while(True):
    s = str("")
    cad = input()
    if(cad == "#"):
        break
    for i in range (len (cad)):
        if(cad[i] == " "):
            s=s+("%20")
        elif(cad[i] == "!"):
            s=s+("%21")
        elif(cad[i] == "$"):
            s=s+("%24")
        elif(cad[i] == "%"):
            s=s+("%25")
        elif(cad[i] == "("):
            s=s+("%28")
        elif(cad[i] == ")"):
            s=s+("%29")
        elif(cad[i] == "*"):
            s=s+("%2a")
        else:
            s=s+cad[i]
    print(s)