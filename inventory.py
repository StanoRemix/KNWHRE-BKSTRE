import json
import os
from book import Book
from math import ceil


class KNWHRE_BKSTRE:
    def __init__(self):
        self.stock = []

    def add_item(self, book_name, author, price, stash):
        new_item = Book(book_name, author, price, stash)
        self.stock.append(new_item)

    def view_item(self):
        if not self.stock:
            print("No Books Available. Come back later")
        else:
            for i , item in enumerate(self.stock, 1):
                print(f"{i}. {item}")

    def log_inventory(self, filename="KNWHRE-BKSTRE.json"):
        gen = [item.to_inventory() for item in self.stock]
        with open(filename, "w") as f:
            json.dump(gen, f, indent=4)
        print(f"Item saved to {filename} successfully!")

    def load_inventory(self, filename="KNWHRE-BKSTRE.json"):
        try:
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    gen = json.load(f)
                    self.stock = [Book.from_inventory(item) for item in gen]
                print(f"Files loaded from {filename} Successfully!")
            else:
                print(f"No files found. {filename} empty.")
        except FileExistsError:
            print("Error.")

    def grand_total(self):
        return ceil(sum(item.price * item.stash for item in self.stock))
