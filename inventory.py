import json
from book import Book
from math import ceil


class KNWHRE_BKSTRE:
    def __init__(self):
        self.stock = []

    def add_item(self, item):
        self.stock.append(item)

    def view_item(self):
        return self.stock

    def log_inventory(self, filename="KNWHRE-BKSTRE.json"):
        with open(filename, "w") as f:
            gen = [item.to_inventory() for item in self.stock]
            json.dump(gen, f, indent=4)

    def load_inventory(self, filename="KNWHRE-BKSTRE.json"):
        try:
            with open(filename, "r") as f:
                gen = json.load(f)
                self.stock = [Book.from_inventory(item) for item in gen]
        except FileNotFoundError:
            self.stock = []

    def grand_total(self):
        return ceil(sum(item.price * item.stash for item in self.stock))
