from inventory import KNWHRE_BKSTRE


def prime():
    Inventory = KNWHRE_BKSTRE()
    Inventory.load_inventory()

    while True:
        print("\n======= KNWHRE BOOKSTORE =======")
        print("-"*30)
        print("Menu:")
        print("1. Add a Book")
        print("2. View Inventory")
        print("3. Save Inventory")
        print("4. Load Inventory")
        print("5. Exit")
        print("-"*30)

        in_req = int(input("Choose an option: "))

        if in_req == 1:
            book_name = input("\nEnter book title: ")
            author = input("Enter Author's name: ")
            try:
                price = float(input("Price: "))
                stash = int(input("Quantity: "))
                Inventory.add_item(book_name, author, price, stash)
                print(f"\n{book_name} added successfully!")
            except ValueError:
                print("\nInvalid entry in price or quantity. Numeric values only")
        elif in_req == 2:
            Inventory.view_item()
        elif in_req == 3:
            Inventory.log_inventory()
        elif in_req == 4:
            Inventory.load_inventory()
        elif in_req == 5:
            print("\nExiting Bookstore...")
            break
        else:
            print("\nInvalid option. pick from the number provided.")


prime()
