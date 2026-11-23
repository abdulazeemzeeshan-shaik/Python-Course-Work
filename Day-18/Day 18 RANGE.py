#random password generation
import random
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters += "abcdefghijklmnopqrstuvwxyz"
characters += "0123456789"
characters += "@!#$%^&*?"
password = ""
password_length= 8
for ch in range(password_length):
    password += random.choice(characters)
print(password)

print()

#UPPER CASE &LOWER CASE
import random
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
special_characters="@#$%&*?"
all_characters= upper_case+lower_case+digits + special_characters
password=[]
password.append(random.choice(upper_case)) # OR password+=random.choice(upper_case)
password.append(random.choice(lower_case)) # OR password+=random.choice(lower_case)
password.append(random.choice(digits))   # OR password+=random.choice(digits)
password.append(random.choice(special_characters))   # OR password+=random.choice(special_characters)
length=10
for i in range(length - 4):
    password.append(random.choice(all_characters))
#random.shuffle(password) shuffles the order if not shuffled upper_case will come first then lower then digits,etc
random_password="".join(password)
print(random_password)


#find the frequency and occurence of each character in string
string="codegnan a" # for list it counts numbers [1,2,3,1,2,4,5,7,4,9]
dictionary={}
for ch in string:
    if ch in dictionary:
        dictionary[ch] +=1 
    else:
        dictionary[ch]=1
print(dictionary)
print(dictionary.get("z"))

from collections import Counter
f=Counter("codegnan a")
print(f)
print(f["z"])  # there is no Z in string so if we print z it will give as 0