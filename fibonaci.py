n=int(input("Unesi zeljeni broj clanova fibonacijevog niza: "))
l=[0,1]
i=0
if(n==1):
    print(l[0])
elif(n==2):
    print(l[0],l[1])
else:
    while(i<n):
        l.append(l[-1]+l[-2])
        print(l[i])
        i += 1