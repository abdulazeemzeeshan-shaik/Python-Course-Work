
#normal function
def add(x,y):
    return x+y
print(add(10,20))

#lambda
from functools import reduce
nums=[10,30]
addition=reduce(lambda x,y: x+y,nums)
print(addition)


#FILTER
nums=[1,2,3,4,5,6,7,8]
even=filter(lambda x: x%2==0,nums)
print(even)
print(list(even))

#MAP
nums=[1,2,3,4,5]
add_10=map(lambda x:x+10,nums)
print(list(add_10))

#REDUCE
from functools import reduce
nums=[1,2,3,4,5]
reduce_data=reduce(lambda x,y: x+y,nums)
print(reduce_data)
