while True: 	
    n=input().split() 
    w=n[1:] 	
    if int(n[0])==0: 	
        print("") 	
    else: 		
        e=w[::-1] 	
        for i in range(len(e)-1): 		
            r=e[i] 		
            print(r,end=" ") 	
        print(e[len(e)-1])