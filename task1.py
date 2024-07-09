#Create a class Product with properties name, price, and quantity. Create a child class Book that inherits from Product and adds a property author and a method called read that prints information about the book.
#Створити клас Product з властивостями name, price та quantianti. Створити дочірній клас Book, який успадковується від Product і додає властивість author і метод read, який виводить інформацію про книгу.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        return f"Книга: {self.name}, Автор: {self.author}, Ціна: {self.price}, Кількість: {self.quantity}"

book = Book('Смерть на Нілі', "250 грн", "1 книга", "Агата Крісті")
print(book.read())