x1, y1, x2, y2 = map(int, input().split())
if y2 >= y1 >= x2 >= x1:
    print('['+str(x2)+','+str(y1)+']')
elif y1 >= y2 and x2 >= x1:
    print('['+str(x2)+','+str(y2)+']')
elif y2 >= y1 and x1 >= x2:
    print('['+str(x1)+','+str(y1)+']')
elif y1 >= y2 >= x1 >= x2:
    print('['+str(x1)+','+str(y2)+']')
else:
    print('[]')


