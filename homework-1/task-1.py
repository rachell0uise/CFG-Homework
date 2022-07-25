class CashRegister:

    def __init__(self):

        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_and_price):
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, amount):
        self.discount += amount

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        return total_before_discount - self.discount

    def show_items(self):
        for item, price in self.total_items.items():
            print(f"- {item} - £{price:.2f}")

    def reset_register(self):
        self.total_items = {}
        self.discount = 0


CR_1 = CashRegister()
CR_2 = CashRegister()

CR_1.add_item({'Milk': 0.70})
CR_1.add_item({'Eggs': 2.00})
CR_1.add_item({'Chocolate': 1.50})

CR_1.remove_item('Eggs')

CR_1.apply_discount(1.00)

CR_1.get_total()

CR_1.show_items()

CR_1.reset_register()