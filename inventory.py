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
            print("\nNo Books Available. Come back later")
        else:
            print("-"*30)
            for i , item in enumerate(self.stock, 1):
                print(f"{i}. {item}")
            print("-"*30)

    def log_inventory(self, filename="KNWHRE-BKSTRE.json"):
        gen = [item.to_inventory() for item in self.stock]
        with open(filename, "w") as f:
            json.dump(gen, f, indent=4)
        print(f"\nItem saved to {filename} successfully!")

    def load_inventory(self, filename="KNWHRE-BKSTRE.json"):
        try:
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    gen = json.load(f)
                    self.stock = [Book.from_inventory(item) for item in gen]
                print(f"\nFiles loaded from {filename} Successfully!")
            else:
                print(f"\nNo files found. {filename} empty.")
        except FileExistsError:
            print("\nError.")

    def grand_total(self):
        return ceil(sum(item.price * item.stash for item in self.stock))
