tc = int(input())
# evaluar la temperatura
if tc>30:
    print("hace calor")
elif tc<10:
    print("hace frio")
else:
    print("esta bien")
# evaluar si el agua hierve o se congela
if tc>=100:
    print("hierve")
elif tc<=0:
    print("se congela")