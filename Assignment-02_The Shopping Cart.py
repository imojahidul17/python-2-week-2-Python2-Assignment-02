class ShoppingCart:
    
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_item(self, item_name, price):
        self.items.append((item_name, price))
        print(item_name + " added to cart.")

    def remove_item(self, item_name):
        found = False
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                print(item_name + " removed from cart.")
                found = True
                break
        if found == False:
            print(item_name + " not found in cart.")


    def total(self):
        total_price = 0
        for item in self.items:
            total_price = total_price + item[1]
        return total_price

    def show_cart(self):
        print("Cart owner:", self.owner)
        print("Items:")
        
        if len(self.items) == 0:
            print("Cart is empty.")
        else:
            for item in self.items:
                print(item[0] + " - £" + str(item[1]))
        
        print("Total: £" + str(self.total()))
        print()


# Creating 2 shopping cart objects
cart1 = ShoppingCart("Mojahid")
cart2 = ShoppingCart("Ali")


# Add items (cart1)
cart1.add_item("Book", 10)
cart1.add_item("Pen", 2)
cart1.add_item("Notebook", 5)

# Add items (cart2)
cart2.add_item("Shoes", 50)
cart2.add_item("T-shirt", 20)
cart2.add_item("Cap", 8)


# Remove items 
cart1.remove_item("Pen")
cart2.remove_item("Cap")


# Show both carts
print("\n--- Cart 1 ---")
cart1.show_cart()

print("--- Cart 2 ---")
cart2.show_cart()