
# cart.py
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        self.items.append(item_name)

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
        else:
            print(f"{item_name} not found in cart.")

    def checkout(self):
        print("You bought:")
        for item in self.items:
            print(f"- {item}")
        self.items.clear()

# Only runs when this file is executed directly
if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item("Apples")
    cart.add_item("Bread")
    cart.remove_item("Milk")
    cart.checkout()