# lovely_loveseat_description = '''
# Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
# '''
# lovely_loveseat_price = 254.00

# stylish_settee_description = '''
# Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
# '''

# stylish_settee_price = 180.50

# luxurious_lamp_description = '''
# Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
# '''

# luxurious_lamp_price = 52.15

# sales_tax = .088

# customer_one_total = 0

# customer_one_itemization = stylish_settee_description + luxurious_lamp_description

# customer_one_total += lovely_loveseat_price
# customer_one_total += luxurious_lamp_price

# customer_one_tax = customer_one_total * sales_tax

# customer_one_total += customer_one_tax

# print("Customer One Items:")
# print(customer_one_itemization)
# print("Customer One Total:")
# print(customer_one_total)

# Add leet code stuff when you're ready here

# basic pizza menu 

toppings = ["pineapple", "pepperoni", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 3, 7, 2]
num_two_slices = prices.count(2)
num_pizzas = len(toppings)
# print(num_two_slices)

greeting = "We sell " + str(num_pizzas) + " different kinds of pizza!"

print(greeting)

menu = [["pepperoni", 2], ["pineapple", 6], ["cheese", 1], ["sasuage", 3], ["olives", 2], ["anchovies", 7], ["mushrooms", 2]]

menu.sort()
print(menu)