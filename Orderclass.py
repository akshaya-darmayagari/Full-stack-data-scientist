class Order:
    def __init__(self, items):
        self.items = items
    def add_item(self, item,price):
        self.items[item] = price
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
    def calculate_total(self):
        return sum(self.items.values())
    def show_items(self):
        print(self.items.items())
order = Order({})
order.add_item("Shirt", 500)
order.add_item("Shoes", 1500)
print(order.calculate_total())
print(order.show_items())