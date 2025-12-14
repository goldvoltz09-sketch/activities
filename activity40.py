principal=int(input("enter principal amount"))
rate=int(input("enter rate of interest"))
time=int(input("enter time in years"))
compoundinterest=principal*(1+rate/100)**time
print("The compound interest is:",compoundinterest)