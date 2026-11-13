#POSITIVE NEGATIVE OR ZERO
n=5
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")

print()
#even or odd
n=41
if n%2==0:
    print("even")
else:
    print("odd")

print()

#vote eligibility
name="zeeshan"
age=22
country="india"
if age>=18:
    print(f"{name} {country} eligibe to vote")
else:
    print(f"{name} {country} not eligible")

print()

#grade
name="zeeshan"
s1=75
s2=80
s3=85
s4=90
s5=80
total=(s1+s2+s3+s4+s5)
p=(total/500)*100
if p>90:
    print(f"{name} {total} {p} Grade A")
elif p>80 and p<90:
    print(f"{name} {total} {p} Grade B")
elif p>70 and p<80:
    print("Grade C")
elif p>60 and p<70:
    print("Grade D")
elif p>40 and p<60:
    print("Grade E")
else:
    print("Fail")

#electricity
c_name="zeeshan"
c_id="pfs-71"
units=250
if units<100:
    bill=2*units
elif units > 100 and units <= 200:
    bill=3*units
elif units >200 and units <= 300:
    bill=5*units
elif units > 300:
    bill=7*units

print(f"{c_name} {c_id} {units} {bill}")


print()

"""Employee name
• Employee salary
• Years of experience
• Performance rating (1 to 5)
"""
E_name="Azeem"
salary=30000
exp=5
rating=4
if exp>=5 and rating>=4 and rating <=5:
    print(salary + (salary * 0.2))
elif exp>=3 and exp<5 and rating>=3:
    print(salary + (salary * 0.1))
else:
    print(salary + (salary*0.05))


print()

"""7. ATM Withdrawal Validation System
Question: Develop an ATM withdrawal validation application.
Accept the following details:
• Account holder name
• Account balance
• Withdrawal amount
• ATM PIN
Assume the correct ATM PIN is 1234.
Apply the following conditions:
1. If the entered PIN is incorrect, display an invalid PIN message.
2. If the withdrawal amount is less than or equal to zero, display an invalid amount message.
3. If the withdrawal amount exceeds the account balance, display insufficient balance.
4. If the withdrawal amount is a multiple of ₹100 and all other conditions are satisfied, process the
withdrawal.
5. Otherwise, display an appropriate withdrawal amount error.
Display the transaction status and remaining account balance"""

name="zeeshan"
pin=1234
# p=int(input("enter pin"))
p=1234
if p!=pin:
    print("invalid pin ")
# balance=int(input("balance"))
# withdraw=int(input("withdraw"))
balance=30000
withdraw=10000

acc_balance=balance-withdraw

if withdraw<=0:
    print("invalid amount ")
elif withdraw > balance:
    print("insufficient balance")
elif withdraw %100==0:
    print(f"{name} amount received{withdraw} and account balance is {acc_balance}")
else:
    print("appropriate withdrawal amount error")

#8th question shopping discount and delivery system
# name="azeem"
# product="furniture"
# price=4000
# quantity=1
# membership=input("enter membership type")
# location=input("local or other city")
# if membership=="regular" and price>=5000: 
#     discount=price*0.05   
#     final_price=price-discount

# elif membership=="silver":
#     discount=price*0.05
#     final_price=price-discount
# elif membership=="gold":
#     discount=price * 0.1
#     final_price=price-discount
# else:
#     discount=0
#     final_price=price

# if location=="local":
#     total_amount=final_price+50
# else:
#     total_amount=final_price+100
   
# print(f"the amount of {product} is {price} ")
# print(f"the discount is {discount}")
# print(f"the final amount is {total_amount}")
# print()

#9. Hospital Patient Billing and Consultation System 
patient_name="john"
patient_age=42
consultation=input("general or specialist")
lab_test=int(input("number of tests"))
test_cost=int(input("cost of test"))
hospital_room=int(input("no of days in the hospital"))
room_type=input("general,semi-private or private")

if consultation == "general":
    consultation_bill=300
else:
    consultation_bill==700
if  room_type == "general":
    room_bill=500
elif room_type == "semi-private":
    room_bill=1000
else:
    room_bill=2000
if age>=60:
    discount=consultation_bill * 0.1
    age_discount=discount
elif lab_test>=2 and test_cost>=1000:
    discount=test_cost*0.1
    laboratory_bill=discount
elif hospital_room >=2:
    discount=room_bill*0.1
    room_charge=discount
total_bill=(consultation_bill + room_bill) -(age_discount +laboratory_bill+ room_charge) 

print(f"consultation bill is {consultation_bill} and laboratory_bill is {laboratory_bill} and room charge is {room_charge}")
print(f"total bill is {total_bill}")