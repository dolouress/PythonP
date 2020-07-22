s=input("Unesi string: ")
s=s.lower()
a=s[::-1]
if(s==a):
    print("String je palindrom.")
else:
    print("String nije palindrom.")