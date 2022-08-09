# # Playing with Tuples

# my_first_tupal = ("Dennis", 27, "Male")

# name, age, gender = my_first_tupal
# # print(my_first_tupal)
# # print(name)
# # print(age)
# # print(gender)
# # print(name + " " + str(age) + " " + gender)

# # Playing with zips()

# kids = ["Darryl", "Emery", "Ellie"]
# ages = [8, 6, 4]

# kids_and_ages = zip(kids, ages)
# # print(list(kids_and_ages))

# # First python loops 

# # For Loops

# statement = "Loop number"

# for x in range(100):
#     print(statement + " " + str(x))

# Hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = sum(prices)
average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0
for i in range(0, len(hairstyles)):
  revenue = prices[i] * last_week[i]
  total_revenue += revenue

print("Total Revenue: " + str(total_revenue))
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

under_30 = [price for price in prices if price < 30];