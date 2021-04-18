# 1. Создать строку равную третьему символу введенной строки.

str1 = input("Введите строку: ")

try:
    new_str1 = str1[2]
    print(new_str1)
except IndexError:
    print("Слишком короткая строка!")


# 2. Создать строку равную предпоследнему символу введенной строки.

str2 = input("Введите строку: ")

try:
    new_str2 = str2[-2]
    print(new_str2)
except IndexError:
    print("Слишком короткая строка!")


# 3. Создать строку равную первым пяти символам введенной строки.
# nb! счет с 0 до х, не включая х

str3 = input("Введите строку: ")

if len(str3) < 5:
    print("Длинна строки меньше 5, ответ смотреть ниже.")

try:
    new_str3 = str3[:5]
    print("Новая строка: ", new_str3)
except IndexError:
    print("Слишком короткая строка!")


# 4. Создать строку равную введенной строку без последних двух символов.

str4 = input("Введите строку: ")

if len(str4) <= 2:
    print("Слишком короткая строка! ")

try:
    new_str4 = str4[:-2]
    print(new_str4)
except IndexError:
    print("Слишком короткая строка!")


#  Создать строку равную всем элементам введенной строки с четными индексами.
#  (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого, индексы 0,2,4,6….).

str5 = input("Введите строку: ")

new_str5 = str5[0::2]
print(new_str5)
