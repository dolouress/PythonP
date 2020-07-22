par=[2,4,6,8,10]
nepar=[1,3,5,7,9]
s=par+nepar
s.sort(reverse=True)
zbir=sum(s)
duz=len(s)
min=min(s)
max=max(s)
avg=zbir/duz
print("parni =",par,"neparni =",nepar,"\n","svi =",s)
print(zbir,duz,min,max,avg)

