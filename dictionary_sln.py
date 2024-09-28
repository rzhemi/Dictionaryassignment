menu_list = {
    'D1':{'name':'SODA','price':3.0, 'stock': 'inf'},
    'D2':{'name':'LEMONADE','price': 3.0, 'stock': 'inf'},
    'D3':{'name':'TEA','price': 2.0, 'stock':'inf'},
    'D4': {'name': 'WATER', 'price': 0.0, 'stock':'inf'},
    'A1': {'name': 'POTATO_CAKES', 'price': 7.0, 'stock': 47},
    'A2': {'name': 'SPINACH_DIP', 'price': 5.0, 'stock': 50},
    'A3': {'name': 'OYSTERS', 'price': 13.0, 'stock': 45},
    'A4': {'name': 'CHEESE_FRIES', 'price': 4.0, 'stock': 31},
    'A5': {'name': 'ONION_RINGS', 'price': 7.0, 'stock': 30},
    'S1': {'name': 'COBB', 'price': 14.0, 'stock': 33},
    'S2': {'name': 'CAESAR', 'price': 13.0, 'stock': 44},
    'S3': {'name': 'GREEK', 'price': 12.0, 'stock': 27},
    'E1': {'name': 'BURGER', 'price': 16.0, 'stock': 50},
    'E2': {'name': 'PASTA', 'price': 15.0, 'stock': 37},
    'E3': {'name': 'GNOCCHI', 'price': 14.0, 'stock': 48},
    'E4': {'name': 'GRILLED_STEAK_SANDWICH', 'price': 17.0, 'stock': 45},
    'T1': {'name': 'CARAMEL_CHEESECAKE', 'price': 13.0, 'stock': 33},
    'T2': {'name': 'APPLE_COBBLER', 'price': 12.0, 'stock': 25},
    'T3': {'name': 'BROWNIE_SUNDAE', 'price': 9.0, 'stock': 44},
    'T4': {'name': 'FLAN', 'price': 8.0, 'stock': 44}


}
# function to add item in the menu_list
def add_item(menu_list, name, price, stock):
 menu_list("add", code= "D5", name = "ICED COFFE", price = 4, stock = float('inf'))

# function to take orders n check if its on menu
 def take_order(menu_list, item_code):
    # Check if the item_code exists in the menu_list
    if item_code in menu_list:
        item = menu_list[item_code]
        print(f"{item['name']} is on the menu. The price is {take_order['order']}.")
        # If the order is above 10, print a special message
        if item['order'] > 10:
            print("This item is large enough.")
    else:
        print("This item is not on the menu.")
   
 