def add(item):
    if item:
        inventory.append(item)
        print()
        print(f" Item # {item} has been added to the inventory system.")
        print()
    else:
        print()
        print("Enter a valid item.")
        print()

def display_inventory():
    print()
    print("Current inventory:")
    print()
    if not inventory:
        print("There are no items currently in inventory.")
    else:
        for item in inventory:
            print(item)

def search(item):
    print()
    if item in inventory:
        print("Item is in stock.")
    else:
        print("Item is not in stock.")
    print()

def remove(item):
    print()
    if item in inventory:
        inventory.remove(item)
        print(f" {item} has been removed from the inventory system.")
    else:
        print("The item does not exist in the inventory system.")
    print()

def close():
    print()
    print("Goodbye!")
    exit()

inventory = []
print("Welcome to the Anduril Inventory Management System 1.0")

while(True):
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
            print()
            item = input("Provide the item you would like to add to the inventory system: ")
            item.strip().lower()
            item = item.strip().lower()
            add(item)
        case '2':
            display_inventory()
        case '3':
            print()
            item = input("Please input the item you are searching for: ")
            item = item.strip().lower()
            search(item)
        case '4':
            print()
            item = input("Please provide the item you would like to remove from the inventory system: ")
            item = item.strip().lower() 
            remove(item)
        case '5':
            close()
        case _:
            print()
            print("Choose a valid option.")
            print()
            continue