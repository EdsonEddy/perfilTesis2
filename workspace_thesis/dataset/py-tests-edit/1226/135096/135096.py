t=int(input())
if(t>=100):
    print("hace calor\nhierve")
elif(t>30):
    print("hace calor")
elif(t>=10 and t<=30):
    print("esta bien")
elif(t<10 and t>0):
    print("hace frio")
elif(t<=0):
    print("hace frio\nse congela")