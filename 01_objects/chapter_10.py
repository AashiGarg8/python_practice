# Chapter 10: Python Dictionaries

# 1. Create a dictionary
chai_order = {
    "type": "Ginger chai",
    "size": "Medium",
    "sugar": 1
}

print("Original order:", chai_order)

# 2. Access a value
print("Chai type:", chai_order["type"])
print("Chai size:", chai_order["size"])

# 3. Create an empty dictionary
chai_recipe = {}

# 4. Add data
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print("Recipe:", chai_recipe)

# 5. Delete a key
del chai_recipe["liquid"]

print("Recipe after deletion:", chai_recipe)

# 6. Membership testing
print("Is sugar a key?", "sugar" in chai_order)
print("Is milk a key?", "milk" in chai_order)

# 7. Get all keys
print("Keys:", chai_order.keys())

# 8. Get all values
print("Values:", chai_order.values())

# 9. Get all key-value pairs
print("Items:", chai_order.items())

# 10. Remove a specific entry
removed_sugar = chai_order.pop("sugar")
print("Removed sugar:", removed_sugar)
print("Order after pop:", chai_order)

# 11. Add or update entries
chai_order.update({
    "sugar": 2,
    "customer_note": "Extra hot"
})

print("Updated order:", chai_order)

# 12. Safely access a possibly missing key
note = chai_order.get("special_request", "No special request")
print("Special request:", note)

# 13. Remove the last inserted entry
removed_item = chai_order.popitem()
print("Removed last item:", removed_item)
print("Final order:", chai_order)
