name="codegnan"
characters=[ch for ch in name]
print(characters)

character_upper=[ch.upper() for ch in name]
print(character_upper)

vowel=[ch for ch in name if ch not in "aeiouAEIOU"]
print(vowel)



#list comprehension
l=[1,2,3,4]
res=[]
for num in l:
    if num%2==0:
        res.append(num)
print(res)
#even positions
l=[10,23,4,5,6,7,56,98,65]
even=[i for i in l if i %2==0]
print(even)

#normal position printing 
t=[10,23,4,5,6,7,56,98,65]
for i in range(len(t)):
    if i %2!=0:
        print(t[i],end=" ")
print()

# list comprehension printing of  even positions
tup=[10,23,4,5,6,7,56,98,65]
even_position=[tup[i]  for i in range(len(tup)) if i %2!=0 ] #tuple position t[i]
print(even_position)


#even or odd
l=[1,2,3,4,5,6,7]
print(['even' if num%2==0  else 'odd' for num  in l])
