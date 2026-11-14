# 1. Create a list
ingredients = ["water", "milk", "black tea"]
print("Original ingredients:", ingredients)

# 2. Append - add an item at the end
ingredients.append("sugar")
print("After append:", ingredients)

# 3. Remove - remove an item by value
ingredients.remove("water")
print("After remove:", ingredients)

# 4. Create another list
spice_options = ["ginger", "cardamom"]
print("Spice options:", spice_options)

# 5. Extend - add items from another list
chai_ingredients = ["water", "milk"]
chai_ingredients.extend(spice_options)
print("After extend:", chai_ingredients)

# 6. Insert - add an item at a specific index
chai_ingredients.insert(2, "black tea")
print("After insert:", chai_ingredients)

# 7. Pop - remove and return the last item
last_added = chai_ingredients.pop()
print("Popped item:", last_added)
print("After pop:", chai_ingredients)

# 8. Reverse - reverse the list in place
chai_ingredients.reverse()
print("After reverse:", chai_ingredients)

# 9. Sort - sort the list alphabetically
chai_ingredients.sort()
print("After sort:", chai_ingredients)

# 10. Count - count occurrences of an item
print("Milk count:", chai_ingredients.count("milk"))

# 11. Index - find the position of an item
print("Milk index:", chai_ingredients.index("milk"))

# 12. Length - count the total items
print("Total ingredients:", len(chai_ingredients))

# 13. Maximum and minimum
sugar_levels = [1, 2, 3, 4, 5]
print("Maximum sugar level:", max(sugar_levels))
print("Minimum sugar level:", min(sugar_levels))

# 14. Sum - add numeric values
print("Sum of sugar levels:", sum(sugar_levels))

# 15. Clear - remove all items
test_list = ["water", "milk", "sugar"]
test_list.clear()
print("After clear:", test_list)


# Operator Overloading - an operator can perform different operations depending on the types of objects used with it.

base_liquid = ["water" + "ginger"]
extra_flavour = ["ginger"]

liquid_mix = base_liquid + extra_flavour
print(liquid_mix)

strong_brew = ["black tea", "water"] * 3
print(strong_brew)




# ==========================================
# PYTHON LISTS - COMPLETE LECTURE PROGRAM
# Operator Overloading and Bytearray
# ==========================================


# 1. OPERATOR OVERLOADING WITH LISTS

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

# Combine two lists using +
liquid_mix = base_liquid + extra_flavor

print("1. Combined liquid mix:")
print(liquid_mix)


# 2. MULTIPLYING A LIST

strong_tea = ["black tea"]

# Repeat the list three times
strong_brew = strong_tea * 3

print("\n2. Strong brew:")
print(strong_brew)


# 3. MULTIPLYING A LIST WITH MULTIPLE ELEMENTS

ingredients = ["black tea", "water"]

# The entire list repeats three times
strong_brew = ingredients * 3

print("\n3. Strong brew with multiple ingredients:")
print(strong_brew)


# 4. CONVERTING A STRING INTO A LIST

spice = "cinnamon"

# The entire string becomes one list element
raw_spice_data = [spice]

print("\n4. String as one list element:")
print(raw_spice_data)


# 5. CONVERTING A STRING INTO INDIVIDUAL CHARACTERS

raw_spice_data = list(spice)

print("\n5. String converted into a list of characters:")
print(raw_spice_data)


# 6. CREATING A BYTEARRAY

raw_spice_data = bytearray(b"cinnamon")

print("\n6. Original bytearray:")
print(raw_spice_data)


# 7. MODIFYING A BYTEARRAY

raw_spice_data = bytearray(b"cinnamon")

# Change the first character from c to C
raw_spice_data[0] = ord("C")

print("\n7. Modified bytearray:")
print(raw_spice_data)


# 8. USING REPLACE() ON A BYTEARRAY

raw_spice_data = bytearray(b"cinnamon")

# replace() returns a NEW bytearray.
# It does not change the original bytearray in place.

raw_spice_data.replace(b"cinnamon", b"cardamom")

print("\n8. Bytearray without saving the returned value:")
print(raw_spice_data)


# 9. CORRECT WAY TO USE REPLACE()

raw_spice_data = bytearray(b"cinnamon")

# Save the new bytearray returned by replace()
raw_spice_data = raw_spice_data.replace(
    b"cinnamon",
    b"cardamom"
)

print("\n9. Bytearray after saving the returned value:")
print(raw_spice_data)


#itemgetter

from operator import itemgetter
ingredients = ["water", "milk", "ginger", "sugar"]
get_item = itemgetter(2)
print(get_item(ingredients))
