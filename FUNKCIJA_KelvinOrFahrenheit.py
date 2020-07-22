temp=int(input("Unesi temperaturu: "))
x=input("Unesi K(kelvin) ili F(farenhajt):  ")
def f(x):
    x=x*1.8+32
    print(x,"F")
def k(x):
    x = 273.2+x
    print(x,"K")
if(x=='k' or x=='K'):
    k(temp)
elif(x=='f' or x=='F'):
    f(temp)
else:
    print("Pogresan unos!")
    quit()