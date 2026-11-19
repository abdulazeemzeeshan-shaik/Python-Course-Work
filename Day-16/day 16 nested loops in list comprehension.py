for i in range(3):
    for j in range(3):
        print(i,j,end="")
    print()

print([[i,j] for i in range(3) for j in range(3)])
print()


matrix=[[1,2,3],[4,5,6,],[7,8,9]]
print(matrix[1][2])

print()

print([matrix[i][j] for i in range(3) for j in range(3) if i!=j])

#1Q.squares from 1 to 10
n=10
print([x**2 for x in range(1,11) ])

print()

#2Q.python code programming [6,4,7]
l=['python','code','program']
print([len(x) for x in l])

print()

#3Q.numbers divisible by 5
num=[3,5,15,24,25,35,61,40]
print([x for x in num if x %5 ==0 ])

print()

#4Q.EXTRACT WORDS HAVING MORE THAN 5 CHARACTERS
word=["PFS71","python","full stack","programming","lang"]
print([ch for ch in word if len(ch)>5])

print()

#5Q.vowels from string
s="comprehensIon"
print([v for v in s if v in  "aeiouAEIOU"])

print()

#6Q.prime numbers from 1 to 100
num = 10
print([num for num in range(2,11) for x in range (2,num)   if num % x==0  ])



