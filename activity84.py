try:
    num1,num2=eval(input("enter two numbers seperated by comma"))
    result=num1/num2
    print("result is",result)
except ZeroDivisionError as ex:
    print("division by zero is not allowed",ex)
except SyntaxError:
    print("Please enter numbers separated by comma")
except:
    print("wrong input")
else:
    print("no exception occurred")
finally:
    print("this will execute no matter what")