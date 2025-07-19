class Book:
    def __init__(self, book_name, author, price, stash):
        self.book_name = book_name
        self.author = author
        self.price = round(float(price), 2)
        self.stash = int(stash)

    def __repr__(self):
        return f"{self.book_name} by {self.author} - ₦{self.price} ({self.stash} in stock)"

    def to_inventory(self):
        return{
            "title": self.book_name,
            "author":self.author,
            "price": self.price,
            "quantity": self.stash
        }
    @staticmethod
    def from_inventory(item):
        return Book(item['title'], 
                     item['author'], 
                     item['price'], 
                     item['quantity']
                     )
    
