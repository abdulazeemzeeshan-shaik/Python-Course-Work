#1Q.def calculator function
def calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)
calculator(20,10)


#2Q. Personal Information Generator Using Functions 
#with parameters without return type
def display_profile(name,age,city,qualification,profession):
    print(name)
    print(age)
    print(city)
    print(qualification)
    print(profession)
display_profile("zeeshan",22,"hyd","B.Tech","Student")
print()
#with parameter and with return type
def display_profile(name,age,city,qualification,profession):
    return name,age,city,qualification,profession
profile=display_profile("azeem",22,"guntur","B.tech","student")
print(profile)
print()

#3Q.Area Calculator Using Default Arguments 
def geometric_calculator(l,b,h,s,r):
    area_of_square=s*s
    area_of_rectangle=l*b
    area_of_circle=(3.14)*(r**2)*(h)
    area_of_triangle=0.5*(b*h)
    return (area_of_square,area_of_rectangle,area_of_circle,area_of_triangle)
print(geometric_calculator(10,5,15,3,4))
#4Q. Student Marks and Grade Calculator 
def student_grade(sub1,sub2,sub3,sub4,sub5):
    total=(sub1+sub2+sub3+sub4+sub5)
    average=(sub1+sub2+sub3+sub4+sub5)/5
    percentage=(total/500)*100
    if percentage >=90:
        grade="GRADE A"
        
    elif percentage>=80 and percentage< 90:
        grade="grade B"
        
    elif percentage >=70 and percentage<80:
        grade="GRADE c"
    elif percentage>=60 and percentage<70:
        grade="GRADE D"
    elif percentage>=40 and percentage <60:
        grade="GRADE E"
    else:
        grade="fail"
    return (total,average,percentage,grade)
print(student_grade(80,85,90,70,75))