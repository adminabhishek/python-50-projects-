# your shop adds 10% VAT on evry order 
# you want this to be consistent and tracebale 
# task:
#  write add_vat(price ,vat_rate)
#  use it compute final order for three orders  

def add_vat(price,vat_rate):
    return price*(100 + vat_rate)/100

orders=[100,150,200]

for price in orders :
    final_amount=add_vat(price,10)
    print(f"original:{price} fianl with vat{final_amount}")

