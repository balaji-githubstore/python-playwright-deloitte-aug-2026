class Item:
    def __init__(self, id=None, description=None, quantity=0, price=0):
        self.id = id
        self.description = description
        self.quantity = quantity
        self.price = price

    def print_discounted_price(self):
        print("For item",self.description)
        if self.quantity >= 2:
            print("Discount can be applied for 1000 - 1000HOLIDAY")
        elif self.quantity == 1:
            print("Discount can be applied for 500 - 500HOLIDAY")

    def set_discounted_price(self):
            if self.quantity >= 2:
                self.price=self.price-1000
            elif self.quantity == 1:
                self.price=self.price-500