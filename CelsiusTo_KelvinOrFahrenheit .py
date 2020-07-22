temp=float(input("Unesi temperaturu: "))
x=input("Unesi K(kelvin) ili F(farenhajt): ")
if(x=='k' or x=='K'):
    temp+= 273.1
elif(x=='f' or x=='F'):
    temp=temp*1.800+32
else:
    print("Pogresan unos!")
    quit()
print("Temperatura u zadanoj jedinici je: ",temp,x)
