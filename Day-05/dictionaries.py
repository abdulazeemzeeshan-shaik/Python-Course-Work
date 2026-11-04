d={}
d1=dict()
d2={'a':1,
    'b':2,
    'c':3}
print(type(d),type(d1),type(d2))

print(d2.values())
print(d2.keys())
print(d2.items())
d2['c']=4
print(d2)
d2['d']=5
print(d2)


d2.update({'e':6}) #updates the dictionary with the new key-value pair
print(d2)

print(d2.get('a')) #same as d2['a'] but if key is not present it will return None instead of giving error
print(d2['a'])

print(d2.get('z')) #gives None because key is not present
print(d2.get('z',0)) #gives 0 because key is not present and we have given default value as 0

d2.pop('b') 
print(d2)

d2.popitem() #removes the last inserted key-value pair
print(d2)

#d2.clear()
#print(d2) #removes all the key-value pairs from the dictionary
a=10
print(id(a)) # address of the variable a (building)
print(hash(a))  # room number of the building (hash value)
print(d2.items())