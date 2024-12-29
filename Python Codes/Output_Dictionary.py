#Find the Output of the following:

'''D={1:"one",2:"two",3:"three"}
L=[]
for K,V in D.items():
    if V[0]=="t":
        L.append(K)

print(L)'''

D={}
T=("ZEESHAN","NISHANT","GURMEET","LISA")

for i in range(1,5):
    D[i]=T[i-1]
print(D)
