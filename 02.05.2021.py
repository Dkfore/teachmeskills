# 1. В отеле есть 3 типа номеров: royal (2-3 комнаты), lux (1-2 комнаты), standard
# (1 комната). надо добавить метод для создания номеров и хранения их в виде словаря.

import random


class Royal():
    def __init__(self):
        self.room = random.randrange(2, 4)
        self.quantity = random.randrange(5, 11)


    def edit(self):
        self.room = int(input("Напишите количесвтво комнат в Royal номерах: "))
        self.quantity = int(input("Напишите количесвтво Royal номеров: "))
        return self.room, self.quantity


class Lux():
    def __init__(self):
        self.room = random.randrange(1, 3)
        self.quantity = random.randrange(5, 11)


    def edit(self):
        self.room = int(input("Напишите количесвтво комнат в Lux номерах: "))
        self.quantity = int(input("Напишите количесвтво Lux номеров: "))
        return self.room, self.quantity


class Standard():
    def __init__(self):
        self.room = 1
        self.quantity = random.randrange(5, 11)


    def edit(self):
        self.room = int(input("Напишите количесвтво комнат в Standard номерах: "))
        self.quantity = int(input("Напишите количесвтво Standard номеров: "))
        return self.room, self.quantity


def hotel():
    royal_hotel_rooms, lux_hotel_rooms, standard_hotel_rooms = Royal(), Lux(), Standard()
    types = ['Royal', 'Lux', 'Standard']
    all_room = [royal_hotel_rooms.quantity, lux_hotel_rooms.quantity, standard_hotel_rooms.quantity]
    dict1 = dict(zip(types, all_room))
    print(dict1)
hotel()


# 2. В комнате есть мебель для ванной, спальни и зала (если есть зал). нужно
# добавить метод для добавления и удаления из комнаты мебели в любом количестве.


class Room():
    def __init__(self, bathroom, bedroom, hall):
        self.bathroom = bathroom
        self.bedroom = bedroom
        self.hall = hall


    # def edit(self):
    #     self.bathroom = int(input("Напишите количесвтво мебели для ванной "))
    #     self.bedroom = int(input("Напишите количество мебели для спальни "))
    #     self.hall = int(input("Напишите количесвтво мебели для зала "))
    #     return self.bedroom, self.bathroom, self.hall

    def edit(self):
        print("При добавлении мебели введите число, при удалении число со знаком минус")

        self.bathroom = self.bathroom + int(input("Напишите количесвтво изменяемой мебели для ванной "))
        if self.bathroom < 0:
            self.bathroom = int(input("Произошла ошибка, столько мебели нет в наличии, введите новое число мебели: "))

        self.bedroom = self.bedroom + int(input("Напишите количество изменяемой мебели для спальни "))
        if self.bedroom < 0:
            self.bedroom = int(input("Произошла ошибка, столько мебели нет в наличии, введите новое число мебели: "))

        self.hall = self.hall + int(input("Напишите количесвтво изменяемой мебели для зала "))
        if self.hall < 0:
            self.hall = int(input("Произошла ошибка, столько мебели нет в наличии, введите новое число мебели: "))
        return self.bedroom, self.bathroom, self.hall


room_1 = Room(3, 5, 1)
print(room_1.__dict__)
room_1.edit()
print(room_1.__dict__)


# 3. Нужно создать один метод для изменения любого номера по заданным параметрам,
# в том числе удалению и изменению номеров и комнат.

# her = Lux()
# print(her.room)
# print(her.quantity)
#
#
# def g_edit():
#     choise = input("Какой номер вы хотите изменить? Royal, Lux или Standard ")
#     if choise == 'Royal':
#         her.edit()
#     elif choise == 'Lux':
#         her.edit()
#     elif choise == "Standard":
#         her.edit()
#     else:
#         print("Неправильно введен номер")
#
#
# g_edit()
#
# print(her.room)
# print(her.quantity)
