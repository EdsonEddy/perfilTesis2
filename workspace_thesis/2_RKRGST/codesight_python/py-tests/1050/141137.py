while 2>0:
    def resto(f):
        g = str(f)
        rsp = g[::-1]
        return rsp
    b=int(input())
    f=int(bin(b)[2:])
    dd=int(str(resto(f)))
    print(int(str(dd),2))