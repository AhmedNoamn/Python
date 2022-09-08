# 'init function make the parameter inside it required'
"""
class Books:
    def __init__(self, name, auther, price):
        self.name = name
        self.auther = auther
        self.price = price
        print(name)
        print(auther)
        print(price)


book1 = Books()
"""


class Books:
    def __init__(self, name, auther, price):
        self.name = name
        self.auther = auther
        self.price = price

    def get_name(self):
        print(self.name)

    def get_auther(self):
        print(self.auther)

    def get_price(self):
        print(self.price)


book = Books('ahmed', 'mido', 15)
book.get_name()
book.get_auther()
book.get_price()
