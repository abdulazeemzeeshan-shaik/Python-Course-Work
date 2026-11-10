num=7
count=0
for i in range(1,num+1):
    if num % i ==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")


#perfect number example:6 factors of 6(1+2+3)perfect number  8(1,2,4)not perfect
n=6
summ=0
for i in range(1,n):
    if n % i ==0:
       summ= summ+i
      
        

if summ==n:
    print("perfect number")
else:
    print('not a perfet')

print(   )


#minimum element from the list 
l=[10,26,2,-3,4,45]
mini=l[0]
for i in l:
    if i < mini:
        mini=i
print(mini)
print(     )
#maximum element from the list 
l=[12,345,63,865,4,96]
maxi=l[0]
for i in l:
    if i > maxi:
        maxi = i
        print(sum(l))
print(maxi)


#length
lst=[10,20,30,40]
length=0
for num in lst:
    length+=1
print(length)