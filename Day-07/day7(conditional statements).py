#voting eligibility
age=10
if age>=18:
    print("You are eligible to vote.")
elif age<18:
    print("You are not eligible to vote.")


#negavtive or positive
n=4
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")


#marks
marks=65
if marks>=90:
    print("A")
elif marks >= 75 and marks<=90:
    print("B")
elif marks>=50 and marks<=75:
    print("C")
elif marks<=50 and marks>=35:
    print("D")
else:
    print("fail")

#even or odd
num=5
if num % 2==0:
    print("even")
elif num % 2!=0:
    print("odd")

#FizzBuzz
num=963
if num % 3 == 0 and num % 5 ==0:
    print("FizzBuzz")
elif num % 3==0:
    print("Fizz")
elif num % 5==0:
    print("Buzz")
else:
    print("not divisible by 3 and 5")

num=int(input("Enter a number: "))
if num % 3 == 0:
    print("Fizz")

elif num % 5==0:
    print("Buzz")
elif num % 3==0  and num % 5 ==0:
    print("FizzBuzz")