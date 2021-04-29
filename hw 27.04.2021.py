# У нас есть кафе. Нам нужно написать программу для работы баристы.
# Перед тем как писать программу, надо создать тестовые данные.

# 1. Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.
# Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.

import random
import datetime as dt


def one_day():
    customer = random.randrange(5, 21)
    all_cups = []
    for i in range(1, customer + 1):
        choise = random.randrange(1, 4)
        all_cups.append(choise)
    # print(all_cups)
    cups = sum(all_cups)
    return customer, cups


customer, cups = one_day()

print("Количество покупателей в этот день: ", customer)
print("Количесвто всех чашек кофе, проданных за день: ", cups)

print("---")


# 2. К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).
# Время работы кафе - с 9 до 20 часов.

def time():
    day_today = dt.date.today()
    day_today = day_today.strftime("%d/%m/%Y")
    list_of_time = []
    for cup in range(1, cups + 1):
        x = random.randrange(9, 20)
        y = random.randrange(0, 60)
        time1 = dt.time(x, y)
        time2 = time1.strftime("%H:%M")         # это строка
        time3 = time2 + " " + day_today
        print("Покупаки осуществлялись в: ", time3)
        list_of_time.append(time2)
    return list_of_time


list_of_time = time()       # список со временем

print("---")


# def time(cups):
#     time_of_sales = []
#     for cup in range(1, cups + 1):
#         hours = random.randrange(9, 21)
#         minute = random.randrange(0, 60)
#         if hours <= 9:
#             hours = str(hours)
#             hours = "0" + hours
#         if minute <= 9:
#             minute = str(minute)
#             minute = "0" + minute
#         time_of_sales.append(f"{hours}:{minute}")
#
#     print(time_of_sales)
#
# time(cups)


# 3. Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.

def week():
    all_sales = 0
    all_customers = 0
    for i in range(5):
        all_customers += one_day()[0]
        all_sales += one_day()[1]

    print("Количесвто клиентов: ", all_customers, "Количество покупок: ", all_sales)


week()


"""Дополнительные задачи"""

# 4. Нужно посмотреть, в какое время дня у баристы были перерывы в работе.
# Для этого, нужно взять все покупки за каждый день, сравнить время между ними и отобразить промежутки больше часа.


import math


def breaks():
    minutes = []
    for i in list_of_time:
        a = i.split(":")
        minutes.append(int(a[0]) * 60 + int(a[1]))

    m = sorted(minutes, reverse=False)
    # print(m)      # список в минутрах, отсортированный по наростанию
    break_times = 0

    for i, value in enumerate(m[:-1]):
        # print(i, m[i])
        if m[i + 1] - 60 > m[i]:
            # print(m[i], m[i + 1])
            hours = math.floor(m[i] / 60)
            minutes = m[i] - hours * 60
            hours1 = math.floor(m[i + 1] / 60)
            minutes1 = m[i + 1] - hours1 * 60
            print(f"breaks > 60 min was from {hours}:{minutes} to {hours1}:{minutes1}")
            break_times += 1
    print("Break times - ", break_times)


breaks()


# 5. После перерасчёта оказалось, что для окупаемости, каждый день в кафе должно продаваться не меньше 20 чашек кофе.
# Надо написать декоратор, который будет проверять кол-во чашек кофе на каждый день. И если их было меньше 20,
# возвращать сообщение с ошибкой (подсказка: try/except).


def check_cups(cups_day):
    def wrapper():          # это обертка
        print("What is day?")
        cups_day(cups)
        try:
            cups >= 20
        except:
            print("Mistake? And it's way to close our cafe")
        print("Perfect day")
    return wrapper()


@check_cups
def cups_day(cups):
    print("One work day")
    return
