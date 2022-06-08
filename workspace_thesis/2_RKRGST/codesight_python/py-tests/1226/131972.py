n = int(input())
if n > 30:
    print("hace calor")
    if n >= 100:
        print("hierve")
elif n < 10:
    print("hace frio")
    if n <= 0:
        print("se congela")
else:
    print("esta bien")
