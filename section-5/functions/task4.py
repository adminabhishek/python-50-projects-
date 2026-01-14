# you sell different  chai sizes 
# instead of writtig formulas every where ,create function 
# task :
# .write calculate_bills(cups,price_per_cup)
# .return total bill
# .use this function for multuple orders 

def calculate_bills(cups,price_per_cup):
    return cups*price_per_cup

my_bill = calculate_bills(5,9)
print(f" total calculated bill {my_bill}")