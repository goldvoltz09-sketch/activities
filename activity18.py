bank=20,000
withdraw=int(input("enter the withdrawal amount"))
if withdraw>bank:
    print("insufficient balance")
else:
    bank=bank-withdraw
    print("succesful transaction")
    print("you have",bank,"remaining in your account")