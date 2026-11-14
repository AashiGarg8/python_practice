#we can check the type of an object using the type() function

print(type(12))
print(type(95.5))
print(type(True))
print(type(2+3j))


#integers

black_tea = 12
green_tea = 4

total_tea = black_tea + green_tea
print(f"total tea: {total_tea}")

tea_remaining = black_tea - green_tea
print(f'tea remaining : {tea_remaining}')


milk_litres = 7
servings = 4

milk_per_servings = milk_litres / servings
print(f'milk per servings: {milk_per_servings}')  #1.75  floor number even the ans is a whole number (eg = 5).



#floor division
print(7 // 4)


#modulo
total_teabags = 7
pots = 4

leftover = total_teabags % pots
print(leftover)


# exponentiation
print(2 ** 3)  # 2*2*2 = 8