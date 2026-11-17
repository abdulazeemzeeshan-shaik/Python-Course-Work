#immutable........address changes
def f(x):
    print(id(x))
    x=x+10
    print(id(x))
    return x
a=100
print(id(a))
f(a)
print()
#Mutable...........address doesnt change
def f(x):
    print(id(x))
    x.append(10)
    print(id(x))
b=[10,20,30]
print(id(b))
print(b)
f(b)
print()
#id changes after RE-ASSIGNING
def z(x):
    print(id(x),"x1")
    x=[10,20,30]
    print(id(x),"x2")
y=[10,20,30]
print(id(y),"y")
z(y)
print()
#doesnt change
def f(x):
    x=110
    print(id(x))
a=110
print(id(a))
f(a)