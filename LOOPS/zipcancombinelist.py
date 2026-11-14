name = ["hitesh", "jack", "maya", "dolly"]
bills = [50, 70, 90, 100]

for name, amount in zip(name, bills):
    print(f"{name} paid {amount}")


#zip iterate over several iterables in parallel ,producing tuples with an item from each one.