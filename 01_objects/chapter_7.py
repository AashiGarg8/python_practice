#tuples
masala_spices = ("cardamom", "clove", "cinnamon")

# Unpack the tuple
spice1, spice2, spice3 = masala_spices

print(f"My spices: {spice1}, {spice2}, {spice3}")

# Check membership
print("ginger" in masala_spices)
print("clove" in masala_spices)

# Swap two ratios
ginger_ratio = 2
cardamom_ratio = 1

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"Ginger ratio: {ginger_ratio}")
print(f"Cardamom ratio: {cardamom_ratio}")
