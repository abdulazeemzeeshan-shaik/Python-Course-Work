# even=2
# odd=1
# for i in range(1,5):
#     for j in range(1,5):
#         if i %2 ==0:
#             print(odd, end=" ")
#             odd+=2
#         else:
#             print(even,end=" ")
#             even+=2
#     print()


# print()


#TWO ways to print this pattern

#1st way
for i in range(1,5):
    for j in range(i): #i=0 , i=1, i=2, i=3
        print("*",end=" ")
    print()



print()



#2nd way
for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#numbers in place of *****'
# s
n=1
for i in range(1,5):
    for j in range(i):
        print(n,end=" ")
        n+=1
    print()


# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(i,end=" ")
#         n+=1
#     print()

# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(j,end=" ")
#         n+=1
#     print()
n=4
for i in range(4):
    for j in range(n-i):
        print("*",end=" ")
    print()
