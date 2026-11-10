n=10
for factor in range(1,n+1):
    if n %factor==0:
        print(factor)


num=10
for n in range(1,n+1):
    if n%2!=0:
        print(n,end= " ")
print()

num=10
count=0
for n in range(1,num+1):
    if n%2!=0:
        count=count+1
print(count)

#prime number
n=int(input("enter a number"))
if n % 1==0 and n % n ==0:
    print("prime")
else:
    print("not")
