#BREAK
for i in range(10):
    if i == 5:
        break #To Stop the iterations after 5
    print(i,end="\t")
    
#CONTINUE
for i in range(5):
    if i==3:
        continue #To skip the i value we assign 
    
    print(i,end="")

#PASS

if 10 % 2==0:
    pass #incase if we want to write a code in future pass is used

#ASSERT used in testing
assert 10%2==0
print("even")