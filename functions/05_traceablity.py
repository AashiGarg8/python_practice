#your shop adds a 10% VAT on every order. you want this to be consistent and traceable.
#task: write add_vat(price, vat_rate)
#use it to compute final prices for 3 orders.

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 150, 200]
for price in orders:
    final_amount = add_vat(price,10)
    print(f"Orignal: {price}, Final with VAT: {final_amount}")