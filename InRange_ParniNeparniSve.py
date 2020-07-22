par=[]
for broj in range(2,101,2):
    par.append(broj)
print(par)

nepar=[]
for broj in range(1,101,2):
    nepar.append(broj)
print(nepar)

sve=nepar+par
sve.sort(reverse=True)
print(sve)