#factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
# n natural numbers sum
def natural(n):
    if n==1:
        return 1
    return n+natural(n-1)
print(natural(10))
#even 
def even(n):
    if n==2:
        return 2
    return n+even(n-2)
print(even(10))