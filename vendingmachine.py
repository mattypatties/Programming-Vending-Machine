"""
Matty's Vending Machine
"""
print("")#space
print("")
print("")
print("\033[35mWELCOME!!!\033[0m")

#menu
menu ={
        "Cold Drinks": { #categories
            "1":{"name": "Soda", "price": 1.50},
            "2":{"name": "Water", "price": 0.50},
            "3":{"name": "Milk", "price": 1.25},
            "4":{"name": "Root Beer", "price": 2.25},
            },
        "Hot Drinks": {
            "5":{"name": "Instant Coffee", "price": 1.00},
            "6":{"name": "Cappuccino", "price": 1.50},
            "7":{"name": "Cafe Latte", "price": 1.50},
            "8":{"name": "Americano", "price": 1.25},
            "9":{"name": "Ginger Tea", "price": 1.00},
            },
        "Room Temp Drinks": {
            "10":{"name": "Water", "price": 0.50},
            "11":{"name": "Milk", "price": 1.25},
            },
        "Snacks": {
            "12":{"name": "Chips", "price": 2.00},
            "13":{"name": "Chocolate Bar", "price": 1.25},
            "14":{"name": "Skittles", "price": 1.25},
            "15":{"name": "Lollipop", "price": 1.00},
            "16":{"name": "Protein Bar", "price": 1.75},
            },   
}
print("")#space
#displaying menu
def display_menu():
    print("\033[36m----MENU-----\033[0m")
    for category, items in menu.items():
        print(f"\n{category}:")
        for code, item in items.items():
            print(f"  {code}. {item["name"]} - {item["price"]:.2f}aed")

#calculate the total of the items inside the cart
def calculate_cart(cart):
    total=0
    for item in cart:
        total += item ["price"]*item["quantity"]
    return total
 
#receipt   
def print_receipt(cart,total_paid, change):
    print("\033[36m----RECEIPT-----\033[0m")
    for item in cart:
        print(f"{item["quantity"]} x {item["name"]} at \033[32m{item["price"]:.2f}aed\033[0m = \033[32m{item["quantity"]*item["price"]:.2f}aed\033[0m")
    print(f"\nTotal Paid: \033[32m{total_paid:.2f}aed\033[0m")
    print(f"Change: \033[32m{change:.2f}aed\033[0m")
    print("\n\033[35mThank You For Your purchase!\033[0m")
    
#main function - vending machine operation
def vm_operator():
    cart=[] #user's selected items are stored in a cart (to an empty list)
    while True:
        display_menu()
        
        #choose a category
        category=input("\033[36m\nCold Drinks\nHot Drinks\nRoom Temp Drinks\nSnacks\033[0m\nSelect a category:").title()
        if category not in menu:
            print("\033[31mInvalid category. Please Try Again.\033[0m")
            continue
        
        #select an item
        select_item=input(f"Enter the item code from {category}: ")
        if select_item not in menu[category]:
            print("\033[31mInvalid item code. Please try again.\033[0m")
            continue
        
        #get quantity of item
        selected_item=menu[category][select_item]
        try:
            quantity= int(input(f"How many {selected_item['name']} would you like? "))
            if quantity < 1:
                print("Quantity must be at least 1. Try again")
                continue
        #when user inputs non-numerical value, ask for a valid quantity
        except ValueError:
            print("\033[31mInvalid quantity. Please try again\033[0m")
            continue
        
        #add to cart
        cart.append({"name":selected_item["name"], "price": selected_item["price"],"quantity": quantity})
        print(f"\033[32m{quantity}x{selected_item["name"]} is added to your cart.\033[0m")
        
        #ask if user wants to add more items
        add_items=input("\nWould you like to add more items? (yes/no): ").lower()
        if add_items != "yes":
            break
        
    
    #calculate total in cart
    total_cost= calculate_cart(cart)
    print(f"\nYour total is: \033[32m{total_cost:.2f}aed\033[0m")
    
    #payment process
    try:
        total_paid=float(input("Insert money: \033[32m \033[0m"))
        if total_paid<total_cost:
            print("\033[31mInsufficient money. Transaction Canceled.\033[0m")
            return
        change=total_paid - total_cost
        print(f"\033[35mTransaction successful! The item/s you've purchased are dispersed.\n\033[0m\033[32mYour change is {change:.2f}aed.\033[0m")
    except ValueError:
        print("\033[31mInvalid input. Please enter a valid amount.\033[0m")
        return
    
    #print receipt
    print_receipt(cart, total_paid, change)

#vm operator
if __name__ == "__main__":
    while True:
        vm_operator()
        another=input("\nDo you want to make another purchase? (yes/no): ").lower()
        if another != "yes":
            print("\033[35mThank you for using Matty's Vending Machine. See you!\033[0m")
            break
        
"""
P.S
i added some colors to some of the prints so it might be a bit confusing
"""