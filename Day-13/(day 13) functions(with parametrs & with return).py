
#WITH PARAMETRS  and WITH RETURN type
def add1(x,y):
    return x+y
z=add1(10,20)
print(z)

#WITH parameters & WITHOUT return type
def add2(x,y):                       #       we cann assign funtion name if there is return 
    print(x+y)                       #       ex:z=add3() if there is no return we cannot assign
add2(5,10)                           #        or else we will get none value

#WITHOUT parameters & WITH return type
def add3():
    x=20
    y=40
    return x + y
z=add3()
print(z)

#WITHOUT  parameters & WITHOUT  return type
def add4():
    x=1
    y=2
    print(x+y)
add4()
print()
print()

def div1(a,b):
    if b==0:
        print("division with zero is not possible")
    else:
        return [a/b, a//b,a%b]
c=div1(5,2)
print(c)

def div2(a,b):
    print(a/b,a//b,a%b)
div2(10,3)

def div3():
    a=17
    b=7
    return [a/b,a//b,a%b]
print(div3())

def div4():
    a=8
    b=3
    print(a/b,a//b,a%b)
div4()