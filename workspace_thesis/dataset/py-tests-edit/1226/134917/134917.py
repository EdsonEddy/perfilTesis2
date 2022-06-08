n=int(input())
if(n>=30 and n<100):
    print("hace calor")
elif (n > 30 or n >= 100):
    print("hace calor")
    print("hierve")
elif(n<10):
    print("hace frio")
    print("se congela")
elif(n>10 and n<30):
    print("esta bien")