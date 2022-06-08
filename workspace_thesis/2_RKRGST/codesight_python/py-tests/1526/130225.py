import sys
if __name__=='__main__':
   for x in sys.stdin:      
      v = [int (i) for i in x.split()]
      v.sort()
      print(v[3]-v[0]-v[1]+v[2])