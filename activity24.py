weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in cm: "))
BMI=weight/(height/100)**2
if BMI<18.5:
    print("Underweight")
elif 18.5<=BMI<24.9:
    print("Normal weight")
elif 25<=BMI<29.9:
    print("Overweight")