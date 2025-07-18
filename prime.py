from inventory import KNWHRE_BKSTRE
from book import Book

inventory = KNWHRE_BKSTRE()
inventory.load_inventory()

bk1 = Book ("Zero to hero", "Peter thiel", 5.99, 5)
inventory.add_item(bk1)

inventory.log_inventory()

print("Current Inventory:")
for item in inventory.view_item():
    print(f"{item.book_name} by {item.author} - ₦{item.price} ({item.stash} in stock)")
print("Total stock value:", inventory.grand_total())