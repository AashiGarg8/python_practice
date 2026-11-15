a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [num for num in a if num % 2 == 0]
print(res)


menu = [
    "Iced Peach Tea",
    "Gimger Chai",
    "Lemon Tea"
]
iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)