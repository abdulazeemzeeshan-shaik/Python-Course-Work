#withdraw and balance
balance=10000
withdraw_amount=int(input("enter"))

if withdraw_amount< balance and withdraw_amount % 100==0 or withdraw_amount % 200==0 or withdraw_amount % 500==0:
    print("Allow it ")
    balance_amount=balance-withdraw_amount
    print(f"balance amount is {balance_amount}")
else:
    print("insufficient balance")



#