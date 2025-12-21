unit=int(input("Enter the number of units consumed: "))
tax=0
bill=0
if unit<50:
    bill=unit*2.6 and tax= bill-25
 if unit>50 and unit<100:
    bill=unit*3.25 and tax= bill-35
    if unit>=100 and unit<200:
     bill=unit*5.26 and tax= bill-45
     if unit>=200:
      bill=unit*8.45 and tax=bill-75
print("The total electricity bill is:",tax)
