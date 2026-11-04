
#one conditional statement inside another conditional statement is called nested loops

#a=int(input("Enter a number: "))
#b=int(input("Enter a number: "))
#c=int(input("enter a number:"))
            # OR
a,b,c=map(int,input("enter three numbers").split())
if a >b:
    if a>c:
        print("a is largest")
    else:
        print("c is larges")
else:
    if b>c:
        print("b is largest")
    else:
        print("c is larest")
