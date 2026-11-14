#boolean

water_added = True
chai_added = False
ischai = water_added and chai_added

print(f"ischai: {ischai}")


#example
print(True + 5)
print(False + 5)
print(int(True))
print(int(False))



stir_count = 5
is_boiling = True
total_action = stir_count + is_boiling
print(f"total_action: {total_action}")     #upcasting ---- Python's arithmetic operation converts the Boolean to an integer value for the calculation.


#logical operators (and or not)
chai_added = True
water_added = False

chai_ready = chai_added and water_added
print(f'chai_ready: {chai_ready}')

water_added = True
chai_ready = chai_added and water_added
print(f'chai_ready: {chai_ready}')