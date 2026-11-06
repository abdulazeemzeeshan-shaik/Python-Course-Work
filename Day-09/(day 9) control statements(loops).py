#FOR LOOP
name="zeeshan"
for i in range(0,len(name)):
    print(name[i],end=" ")
print()
n=[10,20,30,40,50]
for index in range(len(n)):
    print(n[index],end=" ")
print()

even_list=[]
odd_list=[]
for i in range(1,11):
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
print()
#WHILE LOOP
i=1
while i <=5:
    print(i)
    i+=1
print()
print(i)
i=5
while i >=1:
    print(i,end=" ")
    i-=1
print()
print(i)
print()
#FOR WITH ELSE
for i in range(10):
    if i==50: #if i exceeds for then else executes
        break
    print(i,end=" ")
else:
    print("loop completed")
 #while with else
i=1
while i <=10:
    if i==7:
        break
    print(i)
    i=i+1
print()
print()

i=1
while i <=10:
    if i==4:
        continue
    print(i)
    i=i+1