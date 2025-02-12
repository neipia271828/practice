
inventory = {}

def add_product(name, quantify):
    if name in inventory:
        inventory[name] += quantify
    else:
        inventory[name] = quantify

def remove_product(name, quantify):
    if name in inventory:
        if inventory[name] >= quantify:
            inventory[name] -= quantify
        else:
            print("Not enough stock to remove")
    else:
        print("Product not found in inventory")

def display_inventory():
    print(inventory)

def process():
    user_input = input("Enter 'add' to add a product, 'remove' to remove a product, 'display' to display inventory, or 'exit' to exit:' ")
    if user_input == 'add':
        name = input("Enter product name:")
        quantify = int(input("Enter quantify:"))
        add_product(name, quantify)
    elif user_input == 'remove':
        name = input("Enter product name:")
        quantify = int(input("Enter quantify:"))
        remove_product(name, quantify)
    elif user_input == 'display':
        display_inventory()
    elif user_input == 'exit':
        return False
    else:
        print("Invalid input")
        return True
    return True

while process():
    pass

print("Goodbye!")