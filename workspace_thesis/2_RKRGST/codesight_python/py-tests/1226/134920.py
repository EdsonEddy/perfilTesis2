import math
n=int(input())
if(n>=10 and n<=30):
    print("esta bien")
elif(n>30 and n<100):
    print("hace calor")
elif(n>=100):
    print("hace calor")
    print ("hierve")    
elif(n>0 and n<10):
    print("hace frio")
elif(n<=0):
    print("hace frio")
    print("se congela")