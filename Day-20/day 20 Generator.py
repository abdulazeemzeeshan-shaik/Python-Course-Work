def generator(x):
    yield x
    yield x+1
    yield x+2
result = generator(10)
print(result)
# print(next(result))
# print(next(result))
# print(next(result))
for i in result:
    print(i)

print()


lst =[10,20,30]
for i in lst:
    print(i)

lst_iterator = iter(lst)
print(lst_iterator)
print(next(lst_iterator))
for i in lst_iterator:
    print(i)

