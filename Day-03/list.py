lst=[10,20,30,40,50]
print(lst[0])
print(lst[0:3]) 
                #print(lst.append(55)) gives error
lst.append(55)  #we to call the list before printing
print(lst)
lst.append([5,10,15])
print(lst)
lst.extend([60,70,80])  #lst.extend(60,70,80) it gives error
print(lst)
lst.insert(0,5)
print(lst)
#new list [5,10,20,30,40,50,55,[5,10,15],60,70,80]
element = 100
if element in lst:
    lst.remove(element)
print("no element")
print(lst)
l=[4,6,2,67,85,2,6,8,3]
print(l)
#l.sort()
#print(l)
l2=sorted(l)

print(l2)




#shallow and deep copy
import copy
l1=[1,2,3,4,5,[6,7,8]]
l2=copy.copy(l1)
print(l1)
print(l2)