#run online tea store if order amount more than 300, delivery is free, otherwise 30 rupees
#task Input: order_amount
#use ternary operator to decide delivery fee.

# order_amount = int(input("order amount: "))
# if order_amount > 300 :
#     print("Delivery free")
# else:
#     print("It cost 30 rupee")


order_amount = int(input("Enter the order amount: "))
delivery_fees = 0 if order_amount>300 else 30
print(f"Delivery fees is : {delivery_fees}")
