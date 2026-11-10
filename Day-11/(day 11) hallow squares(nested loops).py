#hallow square
# #prin          * * * *
#                *     *
#                *     *
#                * * * *


for i in range(10):
    for j in range(10):
        if i ==0 or i ==9 or j==0 or j==9:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()


r=5
c=5
for i in range(r):
    for j in range(c):
        if (i+j)==(r-1) or i==j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print( )
print( )
r=5
c=5
for i in range(r):
    for j in range(c):
        if (i+j)==2 or (i + j) ==6 :
            print("*", end = " ")
        else:
            print(" ",end= " ")
    print()