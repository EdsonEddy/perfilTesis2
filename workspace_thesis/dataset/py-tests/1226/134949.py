g=int(input())
c="hace calor"
f="hace frio"
if g<=0:
    print (f)
    print ("se congela")
else:
    if g > 0 and g < 30:
        print ("esta bien")
    else:
        if g >= 30:
            print (c)
        if g >= 100:
            print ("hierve")
    