price=int(input("enter the price"))
tax=int(input("enter percentage of tax"))
multip=(100-tax)/100
final_price=price*multip
discount=int(input("enter discount percentage"))
multip2=(100-discount)/100
finalprice2=final_price*multip2
print("The final price is:",finalprice2)
