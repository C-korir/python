class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity

    def update_item(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] = quantity
        else:
            print("Item not found in inventory.")

    def get_item_info(self, name):
        if name in self.inventory:
            print(f"Name: {name}, Quantity: {self.inventory[name]}")
        else:
            print("Item not found in inventory.")

    def get_total_quantity(self):
        total_quantity = sum(self.inventory.values())
        print(f"Total quantity of all items: {total_quantity}")


def main():
    inventory = Inventory()
    while True:
        print("\n1. Add item")
        print("2. Update item")
        print("3. Get item information")
        print("4. Get total quantity of all items")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(name, quantity)
        elif choice == 2:
            name = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            inventory.update_item(name, quantity)
        elif choice == 3:
            name = input("Enter item name: ")
            inventory.get_item_info(name)
        elif choice == 4:
            inventory.get_total_quantity()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()