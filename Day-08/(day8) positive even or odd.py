"""Check whether the number is positive or negative or zero """
#if -elif
n=15
if n > 0 and n % 2 ==0:
    print("positive even")
elif n>0 and n%2 !=0:
    print("positive odd")
elif  n < 0 and n % 2 ==0:
    print("negative even")
elif  n < 0 and n % 2 !=0:
    print("negative odd")
else:
    print("zero")

#nested if

n=50
if n > 0:
    if n % 2 ==0:
        print("positive even")
    else:
        print("positive odd")
elif  n < 0 :
    if n %2 ==0:
        print("negative even")
    else:
        print("negative odd")

else:
    print("zero")