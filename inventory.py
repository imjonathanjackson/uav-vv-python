def add(item, inventory):
    inventory.append(item)
    print(f" Item # {item} has been added to the inventory system.")

def view(inventory):
    print("The following items are in the current inventory:")
    for item in inventory:
        print(item)

def search(item, inventory):
    if item in inventory:
        print("Item is in stock.")
    else:
        print("Item is not in stock.")

def remove(item, inventory):
        inventory.remove(item)
        print(f" {item} has been removed from the inventory system.")

def close():
    print()
    print("Goodbye!")
    exit()

inventory = []

while(True):
    print("Welcome to the Anduril Inventory Management System 1.0")
    print()
    print("1. Add")
    print("2. View inventory.")
    print("3. Search")
    print("4. Remove")
    print("5. Exit")
    print()
    option = input("Choose 1. ")

    match option:
        case '1':
            item = input("Provide the item you would like to add to the inventory system: ")
            add(item, inventory)
        case '2':
            view(inventory)
        case '3':
            item = input("Please input the item you are searching for: ")
            search(item, inventory)
        case '4':
            item = input("Please provide the item you would like to remove from the inventory system: ")
            remove(item, inventory)
        case '5':
            close()
        case _:
            print()
            print("Choose a valid option.")
            print()
            continue