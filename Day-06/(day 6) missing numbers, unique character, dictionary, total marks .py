s1={10,45,62,75,43}
s2={45,10,1}
s1.symmetric_difference(s2)
print(s1.symmetric_difference(s2))

#find unique characters

word="Innovation"
unique=set(word)
print(unique)

#dictionary from 2 lists

lst1=['name', 'age', 'gender']
lst2 =['zeeshan', 22, 'male']
a=dict(zip(lst1,lst2))
print(a)

#total marks
marks={'python':85,
       'aptitude':78,
       'softskills':65}
d=sum(marks.values())
print(d)