import random
x=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',' ']
m=['m','i','a',' ']
l=[]
br=0
naj=[]
najbr1=0
while(l!=m):
    najbr = 0
    i=0
    l=[]
    while(i<4):
        y=random.choice(x)
        l.append(y)
        if(m[i]==l[i]):
            najbr+=1
        i+=1
    if (najbr > najbr1):
        naj = l
        najbr1=najbr
    br+=1

print("Broj pogadjanja:",br)
print("Najblize pogadjanje:",naj)