while True:
    pa = input()
    s = ["oro","Oro","ORo","OrO","oRO","oRo","orO","ORO"]
    for x in s:
        if x in pa:
            d = pa.find(x)
            print (d, d+2)
            break
    else:
        print("-1")