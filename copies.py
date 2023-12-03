class Inventory:
    def __init__(self, total):
        self.total_copies = total
        self.rented = 0
        self.in_store = self.total_copies - self.rented

    def set_rented_amt(self, value):
        self.rented = value

    def get_instore_amt(self):
        return self.in_store


