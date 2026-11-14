# Challenge: Make a chai calculator ☕
# Your program should:
# - Store 20 grams of tea and 5 grams of ginger.
# - Calculate the total grams.
# - Divide the total by 3 using /.
# - Calculate the whole number of portions using //.
# - Calculate the remainder using %.
# - Print the results using f-strings.


tea_grams = 20
ginger_grams= 5

total_gram = tea_grams + ginger_grams
avg= total_gram /3
whole_portion = total_gram //3
remainder = total_gram % 3
print(f'Total grams: {total_gram}')
print(f'Average grams per portion: {avg}')
print(f'Whole number of portions: {whole_portion}')
print(f'Remainder grams: {remainder}')


