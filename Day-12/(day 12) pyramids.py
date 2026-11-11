#        * 
#      * * * 
#    * * * * *
#    2*i+1 
n=3
for i in range(n):
    #spaces
    for j in range(n-i-1):
        print(" ",end=" ")
    #stars
    for j in range(2*i + 1):
        print("*",end=" ")
    print()
print()
# n=5
# for i in range(5):
#     #spaces
#     for j in range(i):
#         print(" *",end=" ")
#     print()
n=5
for i in range(n):
    #spaces
    for j in range(n-i-1):
        print(" ",end=" ")
    #stars
    for j in range(2*i + 1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
        
    for j in range(2*n-(2*i+1)):
        print("*",end=" ")
    print()
print()





        





n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
n=n-1
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(2*n -(2*i+1)):
        print('*',end=" ")
    print()
    











