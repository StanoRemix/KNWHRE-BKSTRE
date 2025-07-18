class Book:
    def __init__(self, book_name, author, price, stash):
        self.book_name = book_name
        self.author = author
        self.price = price
        self.stash = stash

    def to_inventory(self):
        return{
            "title": self.book_name,
            "author":self.author,
            "price": self.price,
            "quantity": self.stash
        }
    @classmethod
    def from_inventory(state, item):
        return state(item['title'], item['author'], item['price'], item['quantity'])
    
