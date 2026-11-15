# favourite_chai = [
#     "Masala chai", "Green Tea", "Masala chai", "lemon tea", "Green Tea", "Elaichi Chai"
# ]
# unique_chai = {chai for chai in favourite_chai}
# #unique_chai = {chai for chai in favourite_chai if len(chai)<10}
# print(unique_chai)


recipes = {
    "Masala chai" : ["ginger", "cardamom", "clove"],
    "Elaichi chai" : ["cardamom", "milk"],
    "Spicy Chai" : ["ginger", "black pepper", "clove"],
}
unique_spices = {spice for ingridients in recipes.values() for spice in ingridients} #unique value 
print(unique_spices)