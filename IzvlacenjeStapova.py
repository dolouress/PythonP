#
l=[]
i=0
while(i<7):
    l.append(i)
    i+=1
ig=0
y=int(input("Izaberi da li zelis 1. ili 2. da izvlacis: "))
if(y==1):
    while(len(l)!=0):
        x=int(input("Izvuci 1, 2 ili 3 stapa: "))
        if(x==1):
            del l[0]
        elif(x==2):
            del l[0]
            del l[0]
        elif(x==3):
            del l[0]
            del l[0]
            del l[0]
        else:
            print("Previse stapova")
        print("Ostalo je",len(l),"stapova")
        ig+=1
else:
    del l[0]
    del l[0]
    print("Ostalo je", len(l), "stapova")
    while(len(l)!=0):
        x=int(input("Izvuci 1, 2 ili 3 stapa: "))
        if(x==1):
            del l[0]
        elif(x==2):
            del l[0]
            del l[0]
        elif(x==3):
            del l[0]
            del l[0]
            del l[0]
        else:
            print("Previse stapova")
        print("Ostalo je", len(l), "stapova")
        ig += 1
if(y==2):
    if(ig%2==0):
        print("Pobijedio je 1. igrac. ")
    else:
        print("Pobijedio je 2. igrac. ")
else:
    if (ig % 2 == 0):
        print("Pobijedio je 2. igrac. ")
    else:
        print("Pobijedio je 1. igrac. ")
