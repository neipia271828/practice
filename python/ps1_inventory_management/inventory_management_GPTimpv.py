inventory = {}

def add_product(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity

def remove_product(name, quantity):
    if name in inventory:
        if inventory[name] >= quantity:
            inventory[name] -= quantity
        else:
            print("Not enough stock to remove")
    else:
        print("Product not found in inventory")

def display_inventory():
    if inventory:
        print("Current Inventory:")
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")
    else:
        print("Inventory is empty.")

def process():
    user_input = input("Enter 'add' to add a product, 'remove' to remove a product, 'display' to display inventory, or 'exit' to exit: ").strip().lower()
    
    if user_input == 'add':
        name = input("Enter product name: ").strip()
        while True:
            try:
                quantity = int(input("Enter quantity: ").strip())
                if quantity < 1:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for quantity.")
        add_product(name, quantity)
    elif user_input == 'remove':
        name = input("Enter product name: ").strip()
        while True:
            try:
                quantity = int(input("Enter quantity: ").strip())
                if quantity < 1:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for quantity.")
        remove_product(name, quantity)
    elif user_input == 'display':
        display_inventory()
    elif user_input == 'exit':
        return False
    else:
        print("Invalid input")
        return True
    return True

# メイン処理ループ
while process():
    pass

print("Goodbye!")