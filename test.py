n=11
count=0 
for a1 in range(1,n+1,1):
    for a2 in range(1,n+1,1):
        for a3 in range(1,n+1,1):
            for a4 in range(1,n+1,1):
                if a1+a2-a3-a4>0:
                    print( a1,a2,a3,a4)
                    count +=1 

print('count:', count)

