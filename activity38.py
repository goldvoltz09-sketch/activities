cycle1=int(input("Enter the speed of the cycle in km/hr: "))
cycle2=int(input("Enter the speed of the second cycle in km/hr: "))
cycle3=int(input("Enter the speed of the third cycle in km/hr: "))
avg=(cycle1+cycle2+cycle3)/3
if avg>cycle1:
    print("The speed of the first cycle is below average.")
if avg>cycle2:
    print("The speed of the second cycle is below average.")
if avg>cycle3:
    print("The speed of the third cycle is below average.")
else:
    print("All cycles are above average speed.")