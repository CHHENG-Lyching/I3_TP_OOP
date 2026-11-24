
# 1. Create a Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price  #private attribute

    # 2. Encapsulation
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


# 3. Inheritance
class EBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)


# Get Book input
print("Enter Book Information")
title = input("Enter book title: ")
author = input("Enter author name: ")
price = float(input("Enter book price $: "))

# Get EBook input
print("\n--- Enter EBook Information ---")
ebook_title = input("Enter ebook title: ")
ebook_author = input("Enter author name: ")
ebook_price = float(input("Enter ebook price $: "))

# Create Book object
book1 = Book(title, author, price)

# Create EBook object
ebook1 = EBook(ebook_title, ebook_author, ebook_price)

# Display Book information
print("\n--- Book Information ---")
print("Title:", book1.title)
print("Author:", book1.author)
print("Price:", book1.get_price())

# Display EBook information
print("\n--- EBook Information ---")
print("Title:", ebook1.title)
print("Author:", ebook1.author)
print("Price ($):", ebook1.get_price())
