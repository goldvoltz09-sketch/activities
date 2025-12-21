mcause=input("Do you have a medical cause?")
attendance=int(input("Enter your attendance percentage: "))
if mcause.lower()=="yes:":
   if attendance>=75:
    print("You are allowed to sit in the exam.")
   else:
    print("You are not allowed to sit in the exam.")
else:
    print("You are not allowed to sit in the exam.")
