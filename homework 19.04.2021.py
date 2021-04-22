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

# способ 1 - создать новый list. номер 2 переделать имеющиеся?
new_fruit = []
for i in fruit[0:4]:
    new_fruit.append(i.title())
new_fruit.append(fruit[-1])     # добавить цену

new_vegetables = []
for i in vegetables[0:3]:
    new_vegetables.append(i.title())
new_vegetables.append(vegetables[-1])   # добавить цену

new_berries = []
for i in berries[0:3]:
    new_berries.append(i.title())
new_berries.append(berries[-1])   # добавить цену

# делаем товары неизменяемыми (tuple)
new_berries = tuple(new_berries)
new_vegetables = tuple(new_vegetables)
new_fruit = tuple(new_fruit)

# add cabbage to vegetables
new_vegetables = list(new_vegetables)
new_vegetables.append("Cabbage")
new_vegetables[3], new_vegetables[4] = new_vegetables[4], new_vegetables[3]         # поставить цену в конец списка

new_vegetables = tuple(new_vegetables)      # вернули к неизменяемым


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
new_vegetables.pop()        # удалим цену

eco_vegetables = []         # сэкономили бумагу (обрезали до 6)
for x in new_vegetables:
    x = x[0:6]
    eco_vegetables.append(x)
eco_vegetables.append(vegetables[-1])   # добавили цену из овощей
print(eco_vegetables)


# та же процедура с фруктами

new_fruit = list(new_fruit)
new_fruit.pop()             # удалим цену

eco_fruit = []
for x in new_fruit:
    x = x[0:6]
    eco_fruit.append(x)
eco_fruit.append(fruit[-1])   # добавили цену из фруктов
print(eco_fruit)


# та же процедура с ягодками

new_berries = list(new_berries)
new_berries.pop()           # удалим цену

eco_berries = []
for x in new_berries:
    x = x[0:6]
    eco_berries.append(x)
eco_berries.append(berries[-1])     # добавили цену из фруктов
print(eco_berries)


'''
Дополнительные задачи:
'''
# 5. На все товары, где есть буква "r", нужно сделать скидку в 20%.
# А если их 2, то 25,5%, и сумму округлить до 2 символов после запятой.
# Рассчитать и вывести на экран стоимость каждого отдельного продукта.


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
        print(f"Price {i} is {fruit[-1]}")

""" пятое задание нужно через словарь, но уже нет времени ... """

# 6. Когда кто-то покупает товар, на экране должен отобразиться чек с товаром, кол-вом и суммой.
# Сейчас бы воспользоваться словарем, которого нет (см задание 5)
product_list = []  # В эту переменную нужно добавить все актуальные товары
product_list = new_vegetables + new_berries + new_fruit     # просто объединил оставшиеся товары (или нужно было с эко?)
print(product_list)

order = {choice(product_list): randrange(10)}     # Заказ на товар и кол-во

for key in order.keys():
    quantity = order[key]

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