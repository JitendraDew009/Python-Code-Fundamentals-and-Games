# Generators are used to save the memory.
# You don't want the results immediately
# Lazy evaluation

daily_sales = [5, 10 ,12, 15, 7, 3, 4, 5, 15]

total_cups = (sale for sale in daily_sales if sale > 5)
print(total_cups) # <generator object <genexpr> at 0x000001FC37AAB920>

# ======================================================================

total_cups1 = [sale for sale in daily_sales if sale > 5]
print(total_cups1) # [10, 12, 15, 7, 15]

# ======================================================================
total_cups2 = sum(sale for sale in daily_sales if sale > 5)
print(total_cups2) # 59
