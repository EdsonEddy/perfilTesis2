import sys

for m in sys.stdin:
    flag=False
    if (m[0].isspace()):
        break
    else:    
        cad=m[0]+m[1]
        for i in range (2,len(m)-2):
            es=m[i]+m[i+1]
           
            if (cad==es and i<(len(m)-2)):
                print ("si")
                flag=True
        if (flag != True):
            print ("no")