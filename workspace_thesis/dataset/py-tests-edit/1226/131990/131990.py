temperatura = int (input ())
if temperatura > 30:
    if temperatura >= 100:
       print("hace calor")
       print("hierve")
    else:
       print("hace calor")
elif temperatura < 10:
    if temperatura <= 0:
       print("hace frio")
       print("se congela")
    else:
        print("hace frio")
elif temperatura >= 10 and temperatura <=30:
    print("esta bien")
