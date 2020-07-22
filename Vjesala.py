import random
r=["mia","jagoda","gumica","miletic"]
x=random.choice(r)
y=len(x)
p=[]
m=[]
s=[]
for i in range(0,len(x)):
    p.append('_')
    m.append(x[i])
print(p)
z=7
while(z>0 and m!=p):
    slovo=input("Pogodi slovo: ")
    for i in range(0,len(x)):
        if(slovo==x[i]):
            p[i]=slovo
    if slovo in s:
        z+=1
    else:
        s.append(slovo)
    z -= 1
    print("Ostalo je",z,"zivota")
    print("Pogadjana slova: ",s)
    print(p)

if(m==p):
    print("Pogodili ste!")
else:
    print("Izgubili ste zivote, trazena rijec je: ",x)