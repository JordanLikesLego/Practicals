number_of_items = int(input("Please enter number of items: "))
price = 0
for n in range(0, number_of_items):
    item_price = float(input("Price of item: $"))
    price = price + item_price
if price > 100:
    total_price = price * 0.9
    print("Total price for {} items is ${:,.2f}".format(number_of_items, total_price))
else:
    print("Total price for {} items is ${:,.2f}".format(number_of_items, price))