sa=['a','e','i','o','e','A','E','I','O','U']
sam=0
sug=0
praz=0
s=input('Unesi string: ')
for x in s:
    if(x in sa):
        sam=sam+1
    elif (x == ' '):
        praz = praz + 1
    else:
        sug = sug + 1
print("Samoglasnika:",sam)
print("Suglasnika:",sug)
print("Praznina:",praz)