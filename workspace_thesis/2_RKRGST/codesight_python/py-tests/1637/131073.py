while True :
    try:
        a,b,c=map(int,input().split())
        x,y,z= map(int, input().split())
        if a>=0 and a<=5:
          if b >= 0 and b <= 5:
            if c>= 0 and c <= 5:
                if x >= 0 and x <= 5:
                    if y >= 0 and y <= 5:
                        if z >= 0 and z <= 5:
                            if a+x==5 and b+y==5 and c+z==5:
                                    print("Esta es la llave")
                            else:
                                print("Intenta con otra")
    except ValueError:
        break