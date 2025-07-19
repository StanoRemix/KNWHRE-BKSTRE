class Book:
    def __init__(self, book_name, author, price, stash):
        self.book_name = book_name
        self.author = author
        self.price = round(float(price), 2)
        self.stash = int(stash)

    def to_inventory(self):
        return{
            "title": self.book_name,
            "author":self.author,
            "price": self.price,
            "quantity": self.stash
        }
    @staticmethod
    def from_inventory(state, item):
        return state(item['title'], 
                     item['author'], 
                     item['price'], 
                     item['quantity']
                     )
    
