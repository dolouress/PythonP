import random

y=int(input("Izaberi broj: "))
l=[]
n=1
while(n<=100):
    l.append(n)
    n+=1
x=random.choice(l)
br=0
while(x!=y):
    if(x>y):
        print("Izabrani broj je nizi od trazenog. ")
    else:
        print("Izabrani broj je visi od trazenog. ")
    y = int(input("Broj nije pogodjen. Izaberi novi broj: "))
    br+=1
print("POGODJEN BROJ. POGADJALI STE",br, "PUTA.")
