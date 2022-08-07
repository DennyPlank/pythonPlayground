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

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory = sorted(inventory)
print(inventory)