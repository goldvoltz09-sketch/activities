def convertnum(num):
    binary=bin(num)
    octal=oct(num)
    hexadecimal=hex(num)  
    print("The binary value is:",binary)
    print("The octal value is:",octal)
    print("The hexadecimal value is:",hexadecimal)
number=int(input("Enter a number: "))
convertnum(number)