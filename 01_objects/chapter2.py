#mutable example

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
spice_mix.add("Ginger")
spice_mix.add("cardamom")
print(f"After spice mix id: {id(spice_mix)}")


#address(refrence didnt change)
#so set is an example of mutable object.