
# Chapter 9: Python Sets

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# 1. Union: combine all unique spices
all_spices = essential_spices | optional_spices
print("All spices:", all_spices)

# 2. Intersection: find common spices
common_spices = essential_spices & optional_spices
print("Common spices:", common_spices)

# 3. Difference: spices only in essential
only_in_essential = essential_spices - optional_spices
print("Only in essential:", only_in_essential)

# 4. Membership test
print("Is cloves in essential spices?",
      "cloves" in essential_spices)

print("Is cloves in optional spices?",
      "cloves" in optional_spices)


#frozen set