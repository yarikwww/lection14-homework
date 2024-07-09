'''
#Створіть клас Ресторан з назвою властивостей, кухнею та меню. Властивість меню має бути словником, де ключі — це назва страви, а значення — ціна.
# Створіть дочірній клас FastFood, який успадковується від Ресторан і додає властивість drive_thru (логічне значення, що вказує на те, чи є в ресторані проїзд чи ні) і метод order, який приймає назву страви та кількість і повертає загальну вартість замовлення.
# Метод також повинен оновити словник меню, щоб відняти впорядковану кількість від доступної кількості.
# Якщо страви немає в наявності або якщо запитувана кількість перевищує доступну, метод повинен повернути повідомлення про те, що замовлення не може бути виконано. Приклад використання:
#class Restaurant:
    # your code here
    pass

class FastFood(Restaurant):
    # your code here
    pass

menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available
'''

class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name not in self.menu:
            return "Страва недоступна"

        dish = self.menu[dish_name]

        if dish['quantity'] < quantity:
            return "Запитана кількість недоступна"

        total_price = dish['price'] * quantity
        self.menu[dish_name]['quantity'] -= quantity

        return total_price


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available