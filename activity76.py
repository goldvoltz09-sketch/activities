def total_calc(bill_amount, tip_percent):
 total = bill_amount + (bill_amount * tip_percent / 100)
 total = round(total, 2)
 return total
total = total_calc(1500, 20)
print(f"Payable amount is: {total}")