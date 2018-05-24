# shopping_cart.py

import datetime # its a module. we need to import it to use it :-)

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

checkout_start_at = datetime.datetime.now()

#
# CAPTURE USER INPUTS
#

product_ids = []

while True:
    product_id = input("Hey, please input a product identifier: ") # capture user input and store in variable
    if product_id == "DONE":
        break # stop the infinite loop!
    else:
        product_ids.append(int(product_id)) # need to convert to integer because user inputs are treated as strings!

#
# PRINT EVERYTHING (RECEIPT) AT THE SAME TIME, AFTER CAPTURING INPUTS
#

running_total_price = 0

print("-------------------------------")
print("PROF ROSSETTI'S ITALIAN GROCERY STORE")
print("Phone: 1.234.567.8900")
print("Web: www.prof-rossetti-italian-grocery.com")
print(checkout_start_at.strftime("%A, %B %d, %Y at %I:%M %p"))
print("-------------------------------")

# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50), optionally sorted alphabetically by name, optionally grouped by department and displayed underneath the respective department name.
print("PURCHASED ITEMS:")
for product_id in product_ids:
    matching_products = [product for product in products if product["id"] == product_id] # list comprehensions return a list but we want the actual dictionary item
    matching_product = matching_products[0] # we can assume there will only be one matching any given unique identifier
    running_total_price += matching_product["price"] # accumulate a running total
    price_usd = ' (${0:.2f})'.format(matching_product["price"]) # this is just for printing, not for adding!!!!!!!
    print(" + " + matching_product["name"] + price_usd )


# The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $1.50), calculated as the sum of their prices.
print("-------------------------------")
running_total_price_usd = '${0:.2f}'.format(running_total_price) # for printing!
print("RUNNING TOTAL: " + str(running_total_price_usd))

# The amount of tax owed, calculated by multiplying the total cost by a New York City sales tax rate of 0.08875.
tax_owed = running_total_price * 0.08875
tax_owed_usd = '${0:.2f}'.format(tax_owed) # for printing!
print("PLUS NYC SALES TAX: " + str(tax_owed_usd))

# The total amount owed, formatted as US dollars and cents (e.g. $1.63), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items.
total_owed = running_total_price + tax_owed # use the original, numeric values for mathematic operations. NOT THE STRING VERSIONS!
total_owed_usd = '${0:.2f}'.format(total_owed) # for printing!
print("TOTAL: " + str(total_owed_usd))

# A friendly message thanking the customer and/or encouraging the customer to shop again.
print("-------------------------------")
print("THANK YOU! COME BACK SOON!")
print("-------------------------------")
