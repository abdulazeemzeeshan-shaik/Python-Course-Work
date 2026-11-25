#if code has error it goes to except
#try->except->finally
# if code doesnt have any error it goes to else block
# try->else->finally   " finally will be executed whether error is present or not"

# try:
#     a = int(input("enter value "))
#     b = int(input("enter value "))
#     print(a/b)

# except ValueError as v:
#     print("Please enter valid integers:", v)

# except ZeroDivisionError as z:
#     print("Cannot divide by zero:", z)

# else:
#     print("code doesnt have any error")

# finally:
#     print("code has executed")


#raise Keyword
def div(x,y):
    if y==0:
        raise ZeroDivisionError()
    return x/y 
try:
    div(10,0)
except:
    print("division with zero")

#custom Exception
#if user want to create an exception, we can call it as custom exception
class NegativeBalanceError(Exception):
    pass
def withdraw(amount):
    balance=1000
    if amount < 0:
        raise NegativeBalanceError()
    balamce=balance - amount
    return f'{amount} withdrawn,current balance is {balance}'

try:
    a=withdraw(-500)
    print(a)
except:
    print("amount is negative")
# try:
#     password=input("enter password")
#     up_case="QWERTYUIOPLKJHGFDSAZXCVBNM"
#     sp_characters="!@#$%^&*"
#     numbers="0123456789"
#     if  password not in up_case :
#         raise ValueError("uppercase letters arer missing")
#     if len(password)<=8:
#         raise ValueError("password length is small")

#     if  password not in sp_characters:
#         raise ValueError("special characters are misssing")
#     if password not in numbers:
#         raise ValueError("numbers are missing in the password")

try:
    password=input("enter password")
    up_case="QWERTYUIOPLKJHGFDSAZXCVBNM"
    sp_characters="!@#$%^&*"
    numbers="0123456789"
    if not any(char in up_case for char in password):
        raise ValueError("Uppercase letters are missing")

    if len(password) < 8:
        raise ValueError("Password length is small")

    if not any(char in sp_characters for char in password):
        raise ValueError("Special characters are missing")

    if not any(char in numbers for char in password):
        raise ValueError("Numbers are missing")
except ValueError as e:
    print("PASSWORD ERROR",e)

else:
    print("password is valid")
finally:
    print("password accepted")