g=int(input("Godina rodjenja: "))
m=int(input("Mjesec rodjenja: "))
d=int(input("Dan rodjenja: "))
print("----------------------")
g1=int(input("Godina trenutna: "))
m1=int(input("Mjesec trenutna: "))
d1=int(input("Dan trenutni: "))
print("----------------------")
g2=g1-g
m2=g2*12
m2=m1-m+m2
d2=30.5*m2
h=d2*24
min=h*60
sek=min*60
print("Ukupan broj mjeseci: ",m2)
print("Ukupan broj dana: ",d2)
print("Sati: ",h,"  \nMinute:",min,"\nSekunde:",sek)

