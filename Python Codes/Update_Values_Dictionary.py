#WAP to update a dictionary with values from that Dictionary

d={'a':1,'b':2,'c':3,'d':4,'e':5}

print("\nDictionary: ",d)

'''for k,v in d.items():
    d['c']= 10
print(d)'''

'''for k,v in d.items():
    d[k]= 10
print(d)'''


d.update({'b':10,'c':20})   
print("Updated Dictionary: ",d)
