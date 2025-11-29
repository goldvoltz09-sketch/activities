cost=int(input("enter the cost price"))
sell=int(input("enter the selling price"))
if cost/sell>1:
    print("loss")
elif cost/sell<1:
 print("profit")
else:
   print("break even")