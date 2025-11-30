age=int(input("enter your age"))
nid=input("do you have a national id card?")
if age>=18 and nid.lower()=="yes":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")