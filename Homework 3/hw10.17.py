# Chiamaka Ugbaja
# 1772427

class ItemToPurchase:  # constructor

    def __init__(self):  # defining variables with default values then prints
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):  # just displays in order of item name, quantity and price
        print(self.item_name + " " + str(self.item_quantity) + " @ $"
              + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))


if __name__ == "__main__":  # FIRST code to run
    print("Item 1")

    first_item = ItemToPurchase()  # first item created
    second_item = ItemToPurchase()  # second item created

    # prompt and reads first_item inputs from user
    first_item.item_name = input('Enter the item name:\n')
    first_item.item_price = int(input('Enter the item price:\n'))
    first_item.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nItem 2")

    # prompt and reads second_item inputs from user
    second_item.item_name = input('Enter the item name:\n')
    second_item.item_price = int(input('Enter the item price:\n'))
    second_item.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")

    # calls the method to print the details for 1st and 2nd item
    first_item.print_item_cost()
    second_item.print_item_cost()

    # calculates total cost of items
    total = (first_item.item_price * first_item.item_quantity) + (second_item.item_price * second_item.item_quantity)

    # prints the total cost
    print("\nTotal: $" + str(total))
