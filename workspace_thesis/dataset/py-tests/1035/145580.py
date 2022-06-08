import sys
for m in sys.stdin:
    if (ord(m[0])==35):
        break
    else:
        if (m[0]==" " or m[len(m)-2]==" "):
            print (m,end="")
        else:
            cad=""
            for i in range (len(m)-1):
                if (m[i]==" "):
                    cad=cad+"%20"
                elif (m[i]=="!"):
                    cad=cad+"%21"
                elif (m[i]=="$"):
                    cad=cad+"%24"
                elif (m[i]=="%"):
                    cad=cad+"%25"
                elif (m[i]=="("):
                    cad=cad+"%28"
                elif (m[i]==")"):
                    cad=cad+"%29"                    
                elif (m[i]=="*"):
                    cad=cad+"%2a"    
                else:    
                    cad=cad+m[i]    
            print (cad)     
