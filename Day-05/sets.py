#sets
s={1,2,3,4,5}
s1=set()
s2={}
print(s)
print(type(s1))
print(type(s2))  #it is dictionary

#remove
s.remove(2)
print(s)

#add
s.add(6)
print(s)

s.remove(6)
print(s)
#s.remove(6)
#print(s)  #gives error because 6 is not present in the set

#discard
s.discard(6)
print(s)  #does not give error even if 6 is not present in the set


#SET OPERATIONS
s3={1,2,3,4,5}
s4={4,5,6,7,8}
#union
s1.union(s2)
print(s3 | s4)

#print(s3[0])  #gives error because set is unordered
s3.intersection(s4)
print(s3 & s4) #intersection

s3.difference(s4)
print(s3 - s4) #difference
print(s4 - s3)

s3.symmetric_difference(s4)
print(s3^s4)  #symmetric difference

#issuperset()
s5={23,57,1,56}
s6={23}
print(s5.issuperset(s6))
print(s6.issuperset(s5))
print(s5.issubset(s6))


#counter
from collections import Counter
str1="zeeshannn"
cc=Counter(str1)
print(cc)