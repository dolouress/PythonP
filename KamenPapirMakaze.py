import random
x=["kamen","papir","makaze"]
i=0
k=0
while(i<3 and k<3):
    print("\nKamen/papir/makaze?")
    igrac = input()
    komp = random.choice(x)
    print("Igrac 2:",komp)
    if(igrac=="kamen" and komp=="makaze" or igrac=="papir" and komp=="kamen" or igrac=="makaze" and komp=="papir"):
        i+=1
    elif(igrac=="kamen" and komp=="papir" or igrac=="papir" and komp=="makaze" or igrac=="makaze" and komp=="kamen"):
        k+=1
    print("Igrac 1:",i,"\nIgrac 2:",k)

if(i>k):
    print("\nPOBIJEDIO/LA SI  :D   !!!!!!!!!!!!!!!!!")
else:
    print("\nIZGUBIO/LA SI  :(  !!!!!!!!!!!!!!!!!")