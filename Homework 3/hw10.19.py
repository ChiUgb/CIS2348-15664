# Chiamaka Ugbaja
# 1772427

class ItemToPurchase:
    total_cost = 0

    # start with a a blank slate that will be filled with user input
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        ItemToPurchase.total_cost += item_price * item_quantity

    def print_item_cost(self):  # print for item layout of cost
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity,
                                     self.item_price, (self.item_price * self.item_quantity)))

    def print_item_description(self):  # print of item description
        print('%s: %s' % (self.item_name, self.item_description,))


class ShoppingCart:  # starts receipt for user
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, item):  # adds item to cart
        self.cart_items.append(item)

    def remove_item(self):  # removes item from cart
        print('\nREMOVE ITEM FROM CART')
        string = input('Enter name of item to remove:\n')
        i = 0
        item_removed = False
        for item in self.cart_items:
            if item.item_name == string:
                del self.cart_items[i]
                item_removed = True
            i += 1
        if not item_removed:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self):  # changes quality of item already in cart
        print('\nCHANGE ITEM QUANTITY')
        name = input('Enter the item name:\n')
        quantity = int(input('Enter the new quantity:\n'))
        item_removed = False
        for item in self.cart_items:
            if item.item_name == name:
                item.item_quantity = quantity
                item_removed = True
        if not item_removed:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):  # counts how many items are in the cart
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total

    def get_cost_of_cart(self): # adds up total cost of what is in the cart
        total = 0
        for item in self.cart_items:
            total += item.item_quantity * item.item_price
        return total

    def print_total():  # prints total of cart if item exit within it or prints 'empty' statement below
        total_cost = get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            output_cart()

    def print_descriptions(self):  # prints out the description of the item in cart
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('\nItem Descriptions')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))

    def output_cart(self):  # display cart
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        print('Number of Items:', total_items)
        print()
        tc = 0
        for item in self.cart_items:  # shows each item in cart with is quality and cast with name
            print('%s %d @ $%d = $%d' % (item.item_name, item.item_quantity,
                                         item.item_price, (item.item_quantity * item.item_price)), end='\n')
            tc += (item.item_quantity * item.item_price)
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print('\nTotal: $%d' % tc)


def print_menu(ShoppingCart):  # prints the menu for the user
    customer_Cart = newCart
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')
    command = ''
    while command != 'q': # loops the cart until the user choose the quit option
        print(menu)
        command = input('Choose an option:\n')
        while command != 'a' and command != 'o' and command != 'i' and command != 'r' \
                and command != 'c' and command != 'q':
            command = input('Choose an option:\n')
        if command == 'a':
            print('\nADD ITEM TO CART')
            item_name = input('Enter the item name:')
            item_description = input('\nEnter the item description:')
            item_price = float(input('\nEnter the item price:'))
            item_quantity = int(input('\nEnter the item quantity:\n'))
            customer_Cart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))
        if command == 'o':
            customer_Cart.output_cart()
        if command == 'i':
            customer_Cart.print_descriptions()
        if command == 'r':
            customer_Cart.remove_item()
        if command == 'c':
            customer_Cart.modify_item()


if __name__ == "__main__":
    # calls this function to go first to collect user input for need portions of the program
    customer_name = str(input('Enter customer\'s name:\n'))
    current_date = str(input('Enter today\'s date:\n'))
    print()
    print('Customer name:', customer_name)
    print('Today\'s date:', current_date)
    newCart = ShoppingCart(customer_name, current_date)
    print_menu(newCart)
