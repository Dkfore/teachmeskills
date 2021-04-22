from random import choice, randrange

fruit = ('apple', 'pear', 'cherry', 'banana', 12)
vegetables = ['tomato', 'onion', 'carrot', 17]
berries = ('blueberry', 'cranberry', 'watermelon', 8)

'''
Обязательные задачи
'''
# 1. На склад поступил новый товар. Надо пересмотреть склад и исправить ошибки, сделать первую товара букву заглавной.
# Все типы товаров должны быть неизменяемыми, чтобы кто-то случайно не перепутал их снова.
# В овощи забыли добавить капусту. Цифра в категории - это цена товара этого типа.


new_fruit = []
for i in fruit[0:-1]:
    new_fruit.append(i.title())


new_vegetables = []
for i in vegetables[0:-1]:
    new_vegetables.append(i.title())

new_berries = []
for i in berries[0:-1]:
    new_berries.append(i.title())

# делаем товары неизменяемыми (tuple)
new_berries = tuple(new_berries)
new_vegetables = tuple(new_vegetables)
new_fruit = tuple(new_fruit)

# add cabbage to vegetables
new_vegetables = list(new_vegetables)
new_vegetables.append("Cabbage")

new_vegetables = tuple(new_vegetables)      # вернули к неизменяемым

print(new_fruit, new_berries, new_vegetables)

# 2. Для удобства хранения, нужно объединить все товары в один объект, при этом сохранить структуру типов.

# через dict ?
store = {"Berries": new_berries, "Vegetables": new_vegetables, "Fruit": new_fruit}
print("Cклад: ", store)

# 3. На складе закончились морковка и арбузы. Надо перенести их в категорию "finished".

finished = []
finished.append("Carrot")
finished.append("Watermelon")
print("Закончились: ", finished)

new_vegetables = list(new_vegetables)   # удалили мокрковку из овощей
new_vegetables.remove("Carrot")
new_vegetables = tuple(new_vegetables)
print("Овощи: ", new_vegetables)

new_berries = list(new_berries)         # удалили арбузы
new_berries.remove("Watermelon")
new_berries = tuple(new_berries)
print("Ягоды: ", new_berries)


new_store = {"Berries": new_berries, "Vegetables": new_vegetables, "Fruit": new_fruit}   # обновим склад
print("Обновленный склад: ", store)


# 4. Если название продукта длиннее 6 символов, нужно отображать только первые 6.

new_vegetables = list(new_vegetables)

eco_vegetables = []         # сэкономили бумагу (обрезали до 6)
for x in new_vegetables:
    x = x[0:6]
    eco_vegetables.append(x)
print(eco_vegetables)


# та же процедура с фруктами

new_fruit = list(new_fruit)

eco_fruit = []
for x in new_fruit:
    x = x[0:6]
    eco_fruit.append(x)
print(eco_fruit)


# та же процедура с ягодками

new_berries = list(new_berries)

eco_berries = []
for x in new_berries:
    x = x[0:6]
    eco_berries.append(x)
print(eco_berries)


'''
Дополнительные задачи:
'''
# 5. На все товары, где есть буква "r", нужно сделать скидку в 20%.
# А если их 2, то 25,5%, и сумму округлить до 2 символов после запятой.
# Рассчитать и вывести на экран стоимость каждого отдельного продукта.

''' слишком длинный и не тот метод
for i in new_vegetables:         # new_vegetables - это обновленный лист с заглавной буквы (в процессе перешел из tuple)
    if "r" in i:
        print(f"Price {i} is {vegetables[-1]*0.8}")
    elif "rr" in i:
        print(f"Price {i} is {vegetables[-1]*0.745}")
    else:
        print(f"Price {i} is {vegetables[-1]}")


for i in new_berries:           # new_berries - это обновленный лист с заглавной буквы (в процессе перешел из tuple)
    if "r" in i:
        print(f"Price {i} is {round(berries[-1]*0.8, 2)}")
    elif "rr" in i:                                     # если бы не две вместе, то код другой, то же самое, если r = 3
        print(f"Price {i} is {round(berries[-1]*0.745, 2)}")
    else:
        print(f"Price {i} is {berries[-1]}")


for i in new_fruit:            # new_fruit - это обновленный лист с заглавной буквы (в процессе перешел из tuple)
    if "r" in i:
        print(f"Price {i} is {round(fruit[-1]*0.8, 2)}")
    elif "rr" in i:                                     # если бы не две вместе, то код другой, то же самое, если r = 3
        print(f"Price {i} is {round(fruit[-1]*0.745, 2)}")
    else:
        print(f"Price {i} is {fruit[-1]}")'''

""" пятое задание нужно через словарь, но уже нет времени ... """

# через словарь

vegetables_price = dict.fromkeys(new_vegetables, vegetables[-1])
berries_price = dict.fromkeys(new_berries, berries[-1])
fruit_price = dict.fromkeys(new_fruit, fruit[-1])

final_product = vegetables_price
final_product.update(berries_price)
final_product.update(fruit_price)
print(final_product)            # вот этот дикт (можно было не делать отдельные словари, а обновить один)

for product, prices in final_product.items():

    if "r" in product:
        final_price = round(prices * 0.8, 2)
        print(f"Price {product} - {final_price}")
    elif "rr" in product:
        final_price = round(prices * 0.8, 2)            # если бы не две вместе, то код другой, и другой, если r = 3
        print(f"Price {product} - {final_price}")
    else:
        final_price = prices
        print(f"Price {product} - {final_price}")


# 6. Когда кто-то покупает товар, на экране должен отобразиться чек с товаром, кол-вом и суммой.
# Сейчас бы воспользоваться словарем, которого нет (см задание 5)

product_list = []  # В эту переменную нужно добавить все актуальные товары
product_list.extend(new_vegetables)
product_list.extend(new_berries)
product_list.extend(new_fruit)
print("Product list: ", product_list)

order = {choice(product_list): randrange(10)}     # Заказ на товар и кол-во

for key in order.keys():            # долгий метод без словаря
    quantity = order[key]           # лишняя строка

    if key in new_vegetables:        # если это овощ
        if "r" in key:
            price = vegetables[-1]*0.8 * quantity
        elif "rr" in key:
            price = vegetables[-1]*0.745 * quantity
        else:
            price = vegetables[-1] * quantity

    if key in new_fruit:        # если это фрукт
        if "r" in key:
            price = fruit[-1]*0.8 * quantity
        elif "rr" in key:
            price = fruit[-1]*0.745 * quantity
        else:
            price = fruit[-1] * quantity

    if key in new_berries:        # если это ягода
        if "r" in key:
            price = berries[-1]*0.8 * quantity
        elif "rr" in key:
            price = berries[-1]*0.745 * quantity
        else:
            price = berries[-1] * quantity

    print(f"Товар {key}, количество {order[key]}, стоимость {round(price, 2)}")

for goods in order.keys():

    print(f"Товар {goods}, количество {order[goods]}, стоимость {round(final_price * order[goods], 2)}")
