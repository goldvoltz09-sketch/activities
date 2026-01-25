def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiply(P,Q):
    return P * Q
def divide(P,Q):
    return P / Q
print("please select operation -\n")
print("a. Add\n",
      "b. Subtract\n",
      "c. Multiply\n",
      "d. Divide\n")
choice=input("Enter choice(a/b/c/d): ")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input")