import random
x=int(input("Izaberi broj: "))
l=[]
i=0
while(i<100):
    l.append(i)
    i+=1
y=random.choice(l)
z=0
br=0
while(x!=y and z<4) :
     if(x>y):
         print("Uneseni broj je veci od trazenog.")
     elif(x<y):
         print("Uneseni broj je manji od trazenog.")
     else:
         print("TACAN BROJ. Pogadjali ste", br, "puta")
     x = int(input("Izaberi novi broj: "))
     br+=1
     z += 1
print("Iskoristili ste sve zivote. Trazeni broj je", y)

