#numeric data types
number = 100
percentage = 9.4
complex = 2+3j
print(number,type(number))
print(percentage,type(percentage))
print(complex,type(complex))



#sequence data types
string = "zeeshan"
list = [1,2,3,4,5]
tuple = (10,20,30,40,50)
print(string,type(string))
print(list,type(list))
print(tuple,type(tuple))


#boolean data types
#true or false
boolean1 = True
boolean2 = False
print(type(boolean1))
print(boolean1 + boolean2)

#mapping data types - dictionary
dictionary={"name":"zeeshan",
            "location":"hyderabad",
            "branch":4}
print(dictionary)
print(type(dictionary))

#sets
s={10}
print(s)
print(type(s))

lst1=[]
print(lst1,type(lst1))

tup=()
print(tup,type(tup))
str=""
print(str,type(str))

dict={}
print(dict,type(dict))
set=set()
print(set,type(set))
#type casting implicit
a=10
b=20.5
print(a+b,type(a+b))
num=int(input())
str1=input()
list1=list(map(int,input().split(",")))
tuple1=tuple(map(int,input().split()))
set1=set(map(int,input().split()))
print(num,type(num))
print(str1,type(str1))
print(list1,type(list1))
print(tuple1,type(tuple1))
print(set1,type(set1))