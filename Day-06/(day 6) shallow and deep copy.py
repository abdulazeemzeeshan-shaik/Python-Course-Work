#shallow
l1=[1,2,3,4,[5,6,7]]
l2=l1.copy()
print(l1)
print(l2)
l1.append(8)
print(l1)
print(l2)   

#deep copy
import copy
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l1.append(9)
print(l1)
print(l2)
