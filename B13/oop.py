class CartItem:
    def __init__(self, item_id: int, name: str, price: float):
        self.__item_id = item_id
        self.__name = name
        self.__price = price

    def get_item_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} (${self.__price})"


class Cart:
    def __init__(self):
        self.cartItems = {}  # {item_id: quantity}

    def add_item(self, item_id: int, quantity: int):
        if item_id in self.cartItems:
            self.cartItems[item_id] += quantity
        else:
            self.cartItems[item_id] = quantity

    def remove_item(self, item_id: int):
        if item_id in self.cartItems:
            del self.cartItems[item_id]

    def update_quantity(self, item_id: int, quantity: int):
        if quantity <= 0:
            self.remove_item(item_id)
        else:
            self.cartItems[item_id] = quantity


class Cashier:
    def __init__(self, uid: int, cart: Cart, item_catalog: dict):
        self.uid = uid
        self.cart = cart
        self.total = 0
        self.item_catalog = item_catalog

    def ask_item(self, item_id: int, quantity: int) -> bool:
        item = self.item_catalog[item_id]
        response = input(f"{item.get_name()}: qty {quantity} => Add to bill? (y/n): ").strip().lower()
        return response == 'y'

    def checkout(self):
        self.total = 0  # reset total
        for item_id, quantity in list(self.cart.cartItems.items()):
            if self.ask_item(item_id, quantity):
                item = self.item_catalog[item_id]
                self.total += item.get_price() * quantity
            else:
                self.cart.remove_item(item_id)
        self.print_receipt()

    def print_receipt(self):
        print("\n===== RECEIPT =====")
        for item_id, quantity in self.cart.cartItems.items():
            item = self.item_catalog[item_id]
            item_total = item.get_price() * quantity
            print(f"{item.get_name()} x {quantity} = ${item_total:.2f}")
        print(f"Total bill: ${self.total:.2f}")
        print("===================")


# ---------- MAIN PROGRAM ----------

# Define available items
item1 = CartItem(1, "T-Shirt", 10.0)
item2 = CartItem(2, "Jeans", 25.0)
item3 = CartItem(3, "Shoes", 50.0)
item4 = CartItem(4, "Hat", 7.5)
item5 = CartItem(5, "Socks", 3.0)

# Create item catalog for lookup
item_catalog = {
    item1.get_item_id(): item1,
    item2.get_item_id(): item2,
    item3.get_item_id(): item3,
    item4.get_item_id(): item4,
    item5.get_item_id(): item5,
}

# Initialize cart and add items
cart = Cart()
cart.add_item(1, 2)  # 2 T-Shirts
cart.add_item(3, 1)  # 1 pair of Shoes
cart.add_item(5, 3)  # 3 Socks

# Start checkout
cashier = Cashier(101, cart, item_catalog)
cashier.checkout()
