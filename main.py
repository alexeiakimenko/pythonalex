# name = "Alexei"
#
# print("Hello,", name)
#
# age = 20
# print(age)

# a = 5
# print(a)
# print(type(a))
# b= "6"
# print(b)
# print(type(b))

# a = 4
# b = 5
# print(a)
# print(id(a))
# a = b
# print(a)
# print(id(a))

# a, b, c = 2, "Hello", 4.5
# print(a, b, c)
# print(id(a), id(b), id(c))
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# print("строка символов")
# print('строка символов')

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + "," + s2 + "! \t \t"
#
# print(s3 * 3)
# print(757348993040506099696)
# print(7.57348993040506099696)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 ** 2)
# print(6 / 4)
# print(6 // 4)
# print(6 % 4)
# print(6 // 4)

# nom = 10
# nom += 5
# print(nom)
# nom -= 3
# print(nom)
# nom *= 4
# print(nom)

# num = 7492
# print(num)
# a1 = num % 10
# print(a1)
# num = num // 10
# a2 = num % 10
# print(a2)
# num = num // 10
# a3 = num % 10
# print(a3)
# num = num // 10
# a4 = num % 10
# print(a4)
# num = 1000 * a1 + 100 * a2 + 10 * a3 + a4
# print(num)
# num = 4728
# print(num)
# res = num % 10 * 1000
# num = num // 10
# res += num % 10 * 100
# num = num // 10
# res += num % 10 * 10
# num = num // 10
# res += num % 10
# print(res)
# a = 1
# b = 2
# print("a: ", a)
# print("b: ", b)
# a,b =  b,a
# # c = a
# # a = b
# # b = c
# print("a: ", a)
# print("b: ", b)
# Функции явного преобразования типов:
# int()-приводит строку к целочисленному значению
# str()-приводит число к строковому значению
# float()-приводит строку к вещественному числу

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
# a = 3.891
#
# a = round(a, 1)
# # print(a)
# num1 = "5.2"
# nim2 = 10
# c = float(num1) + nim2
# print(c)

# name = "Alex"
# age = 44
# print("Меня зовут " + name + ".Мне", age, "года.")
# print("Меня зовут " + name + ".Мне ", age, " года.", sep="", end=" ")
# print("Я учу Python.")
# name=input("Введите имя: ")
# print("Вас зовут",name)
# num = float(input("Введите число: "))
# power = float(input("Введите степень: "))
#
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)
# num1 = int(input("1: "))
# num2 = int(input("2: "))
# num3 = int(input("3: "))
# num4 = int(input("4: "))
# sum1 = num1 + num2
# sum2 = num3 + num4
# res = round(sum1 / sum2, 2)
# print("Result:", round((sum1 / sum2), 2))
# b1 =  True
# b2 = False
# print(b2 + 5)


# test=5
# print(test)
# test =None
# print(test)
# print(2 + 5 == 7)
# print(2 + 5 != 7)
# print("hEllo" > "hellO")

# print(2 < 4 > 9)
# print(3*3 <= 7 >= 2)
# print(2*5 > 7 >=4 +3)
# a = 10
# b = 5
# c = a==b
# print(a,b,c)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён.")
# else:
#     print("Доступ запрещён.")

# = 5
# if a > b:
#     print("a>b")
# if b > a:
#     print("b>a")
# else:
#     print("a=b")
# a = 15
# b
# a = int(input())
# b = int(input())
# if a > b:
#     print("a>b")
# elif a < b:
#     print("a<b")
# else:
#     print("a=b")
# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(N, "ВОРОНА")(N, "ВОРОНА")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if n == 0 or n > 4:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# day = "вторник"
# match day:
#     case "понедельник"|"вторник":
#         print("Рабочий день")
# case _:действие по умолчанию

# a, b = 40, 20
# print("a=b" if a == b else "a>b" if a > b else "b>a")

# try  ... except
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
#
# print("код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так")
# else:
#     print("Всё нормально.")
# finally:
#     print("Конец программы.")
# print("код далее")

# Циклы

# i = 10
# while i <=100:
#     print("i=", i)
#     i = i + 10
# i = 1
# while i <= 20:
#     print(i)
#     i = i + 2
# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1
# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапозона: "))
# res = 0
# while a <= b:
#
#     if a % 2:
#         res += a
#         print(a, "+")
#     a += 1
# print("=", res)
# n = input("Введите целое число:")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Чётное число.")
# else:
#     print("Нечяётное число.")
# i = 0
# while i < 10:
#
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершён")
# res = 1
#
# while True:
#     n = int(input("Введите число:"))
#     if n == 0:
#         break
#     res = res * n
# print("Результат: ", res)
# i = 0
# while i < 4:
#     print(i)
#     i += 1
# else:
#     print("end ,i=", i)
# i = 1
# while i < 5:
#     print("Внешний цикл:i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл j=", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end='')
#         else:
#             print("-", end="")
#
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# for element in collection:
#   тело цикла
# for i in "Hello":
#     print(i)
# for color in "red", "yellow", "green", "orange":
#     print(color)
# range(start,stop,step)
# for i in range(9, -1, -2):
#     print(i, end=" ")
# print()
# o = 2
# while o < 9:
#     print(o, end=" ")
#     o += 3

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0 and a != i:
#         print(i, end=" ")

# i = 0
# for i in range(1, 101):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print("done!")
# w = int(input("shirina": "))
# h = int(input("vysota: "))
# s = "*"
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print(s, end="")
#
#         else:
#             print(" ", end="")
#     print()

# w = [letter * 2 for letter in "Hello"]
# print(w)
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки
# nums = [8, 3, 9, [2, 5, 7], 4, 1]
# print(nums)
# print(type(nums))

# nums = [8, 3, 9, 4, 1]
#
# print(nums)
# print(nums[1])
# print(nums[-1])
# nums[1] = 256
# print(nums[1])
# nums[3] += 100
# print(len(nums))

# s = [5, 1] * 6
# print(s)
# print(type(s))
#
# b = list("Hello")
# print(b)
# print(type(b))
# print(len(b))
# c = s + b
# print(c)

# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(n2)

#  генератор списков
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)
# a = [0] * int(input("kolichestvo elementov: "))
#
# for i in range(len(a)):
#     a[i] = int(input("vvedite znachenie: "))
# print(a)
# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# a = [9, 8, 6, 4, 3]
# for i in range(len(a)):
#     print(i, ":", a[i])
# for i in a:
#     print(i)

# n = list(range(21, 41))
# s1 = 0
# s2 = 0
# for i in range(len(n)):
#     if i % 2 == 0:
#         s1 = s1 + 1
#     if i % 2 == 1:
#         s2 = s2 + n[i]
# print("kol=", s1, ",summa=", s2)

# a = [6, 3, 0, 8, 2]
# a[0], a[-1] = a[-1], a[0] перемена местами элементов

# срез
# список[start:stop:step]

# a = [6, 3, 0, 8, 2, 7]
# print(a[1:4])
# print(a[2:])
# print(a[:2])
# print(a[0:-1:2])
# print(a[::-1])
# print(a[2:20])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[6:])
# print(s[3:5])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# a = "Hello"
# print(a[1:3])
# print(a[::-1])

# a = [6, 3, 0, 8, 2, 7]
# print(a[:])
# a[1:3] = [1, 1, 1, 1]
# print(a[:])
#
# del a[1:4]
# print(a)
# del-удаляет элементы

# Методы списка

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.append(99)
# # добавляет один элемент в конец списка
# print(a)
# a.extend([5, 3, 7, 9])
# # добавляет несколько элементов в конец списка
# print(a)
# a.extend("add")
# print(a)

# b = []
# for i in range(1, 11):
#     b.extend([i ** 2])
# print(b)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.insert(2,100)
# print(a)      #добавляет элемент списка(второй параметр),в определённое место(первый параметр)

# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33,44,55]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a),len(b)):
#     c.append(b[i])
# print(c)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.remove(3)  # удаляет первый совпадающий элемент из списка
# print(a)
# last = a.pop()  # удаляет последний элемент из списка и возвращает удаляемый элемент
# print(a)
# print(last)
# second = a.pop(0)  # удаляет элемент по индексу
# print(a)
# print(second)
# a.clear()  # очищает список
# print(a)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.pop(2)
# print(a)

# a = [5, 2, 9, 1, 2, 4, 3, 2, 4]
# num = a.count(2)  # считает количество заданных значений в списке
# print(num)
#
# ind = a.index(9)  # возвращает положение первого индекса по заданому значению
# print(ind)
# b= 2
# if b in a:
#     ind=a.index(b,4 -1)     #возвращает положение индекса первого по заданному значению

# c = [1, 2, 3]
# d = c.copy()  # создаёт копию списка в другую ячейку памяти
# print("c=", c)
# print("d=", d)
# c.append(4)
# d.insert(0, 100)
# print("c=", c)
# print("d=", d)

# a = [5, 2, 9, 1, 2, 4, 3, 2, 4]
# print(a)
# a.reverse()  # перевернули элементы в обратном порядке
# print(a)
# a.sort()  # сортирует список по возрастанию
# print(a)
# a.sort(reverse=True)  # сортирует по убыванию
# print(a)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort()
# print(s)
# s.sort(key=len)
# print(s)
# s.sort(key=len, reverse=True)
# print(s)

# b = sorted(a, reverse=True)
# print("b=", b)
# print("a=", a)

# Генерация случайных данных

# import random as r #задание нового имени модуля
#
# print(r.randint(0, 5))
# print(r.randrange(6, 16, 2))

# from random import *  # подключение отдельной функции из модуля.import.* всех функций

# print(randint(0, 5))
# print(randrange(6, 12, 2))
# print(round(uniform(10.5, 20.6), 0))
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург", "Томск"]
# print(choice(city_list))
# print(choices(city_list, k=3))
# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=3))
# shuffle(s)
# print(s)


# nas = [randint(0,20) for i in range(5)]
# print(nas)

# Функции агрегирование

# lst = [19, 17, 2, 7, 17]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
# from random import randint


# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# mx = max(lst)
# print(mx)
# lst.remove(mx)
# lst.insert(0, mx)
# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
#
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# mn = min(lst)
# print(mn)
# ind = lst.index(mn)
# del lst[:ind]
# print(lst)

# lst = [4]
# # if len(lst)==0:
# #     print("Clear list")
# print(bool(lst))

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("First list:", a)
# print("Second list:", b)
# c = a + b
# print("All list", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы без повторений:", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Общие элементы для двух списков:", c)
#
# c = []
# c = [min(a), min(b), max(a), max(b)]
# print("Минимальные и максимальные элементы из списков:",c)

# k = int(input("Введите длину списка:"))
# s = []
# while len(s) < k:
#     w = randint(1, k)
#     if w not in s:
#         s.append(w)
# print(s)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print(m)
# # m[1] = [21, 22, 23, 24]
# # print(m[1][2])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col]**2, end="\t\t")
#     print()


# matrix = [[x * y for x in range(1, 10)] for y in range(1, 10)]

# matrix = []
# for y in range(3):
#     new_row = []
#     for x in range(5):
#         new_row.append(0)
#     matrix.append(new_row)

# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ")", x, "+", y, "=", x + y)


# matrix = [[randint(-20, 10) for x in range(3)] for y in range(4)]
# print(matrix)
# s = 0
# for row in matrix:
#     for x in row:
#         if x < 0:
#             s += 1
#         print(x, end="\t")
#     print()
# print(s)
# n = int(input("Size list:"))
# m = [[randint(0, 100) for i in range(n)] for j in range(n)]
# mn = m[1][1]
# for i in m:
#     for j in i:
#         print(j, end="\t")
#     print()
# for k in range(n):
#     if mn > m[k][k]:
#         mn = m[k][k]
# print(mn)
# print("Hello")

# import math

# num1 = math.e
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.sqrt(4)
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)
# print(dir(math))
# from math import sqrt
#
# num1 = sqrt(9)
# print(num1)

# import math as m
# num1 = m.pi
# print(num1)

# from math import pi
#
# r = float(input("Введите радиус окружности: "))
# print("Длина окружности:", round((2 * r * pi), 2))

# import time

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# t = time.time()
# print(t)
#
# local = time.ctime()
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".0", res.tm_mon, ".", res.tm_year, sep="")
# print(time.strftime("%d.%m.%Y"))
# print(time.strftime("Сегодня: %B %d(%A). %Y."))
# pause = 5
# print("Begin")
# time.sleep(pause)
# print("End")

# text = input("Название напоминания: ")
# t = float(input("Через сколько минут: "))
# t = t * 60
# time.sleep(t)
# print(text)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# def hello(name):
#     print("Hello,", name)
#
#
# hello("Boris")
# def get_sum(a, b):
#     print("Sum")
#     return a + b
#
#
# x = 3
# y = 6
# res = get_sum(x, y)
# print(res)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")
# def mat(a, b):
#     if a > b:
#         return a - b
#     if a <= b:
#         return a + b
#
#
# n1 = float(input("n1:"))
# n2 = float(input("n2:"))
# print(mat(n1, n2))

# def cub(a):
#     return a * a * a
#
#
# for i in range(1,11):
#     print(i ,"=", cub(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     a = lst.pop()
#     b = lst.pop(0)
#     lst.append(b)
#     lst.insert(0, a)
#     return lst


# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))
# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(5, 7))

# def check_password(password):
#     has_upper = False
#     has_number = False
#     has_lower = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_number = True
#     if len(password) >= 8 and has_upper and has_lower and has_number:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# print(check_password(p))
# if check_password(p):
#     print("Это надёжный пароль.")
# else:
#     print("Это не надёжный пароль!")

# def get_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# print("result", get_sum(d=1, a=5), sep="&&")

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, end="\n\n")
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")

# def summa(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg
#
#
# a1 = summa(2, 5, 8)
# print(a1 ** 2)

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s = s + cur_digit
#     elif not even and cur_digit % 2:
#     s = s + cur_digit
#
#
# n = (n - cur_digit) / 10
# return s
#
# print("Сумма чётных:")
# print(digits_sum(9874023))
# print(digits_sum(382271))
# print(digits_sum(123456789))
# print("Сумма нечётных:")
# print(digits_sum(9874023, False)
# print(digits_sum(382271, False)
# print(digits_sum(123456789, False)


# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
# a = 2
# b = 2
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(id(lt1))
# lt1.pop(1)
# print(id(lt1))
# lt1[1] = "Hello"

# s = "Hello"
# print(id(s))
# s += "World"
# print(id(s))

# a = 5
# print(id(a))
# a = a + 1
# print(id(a))

# def add_number(n):
#     print(n, "=", id(n))
#     n1 = n + [4]
#     print(n1, "=", id(n1))
#
#
# x = [1, 2, 3]
# print("x:", x, id(x))
# add_number(x)
# print("x:", x, id(x))

# кортеж (tuple)
# lst = [1, 2, 3]
#
# # print(lst.__sizeof__())
# # print(tpl.__sizeof__())
# print(type(tpl))
# a = ()
#
# b = tuple()
# print(type(b))
# a = (1,)
# print(a)
# print(type(a))
# b = tuple(("Hello"))
# print(b)
# print(type(b))
# c = c + 4,
# print(c)
# tpl = (1, 2, 3, 5, 6, 7, 8, 9)
# print(tpl)
# print(tpl[2])
# print(tpl[1:3])
# from random import randint

# s = tuple(2 ** i for i in range(1, 13))
# print(s)
# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3 * 2)
# print(len(t3))
# print(t3.count("l"))
# print(t3.index("l", 4))

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tpl(n1, n2):
#     return tuple(randint(n1, n2) for _ in range(10))
#
#
# tl1 = tpl(0, 5)
# tl2 = tpl(-5, 0)
#
# print(tl1)
# print(tl2)
# tl3 = tl1 + tl2
# print(tl3)

# t = (10, 11, [1, 2, 3], ["hello", "world"])
# print(t, id(t))
# t[3][0] = "new"
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name)
# print(year)
# print(married)
# t = (1, 2, 3)
# del t
# print(t)


# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# lst2 = list(tpl)
# print(type(lst2))
# print(lst2)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.236), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country


# Множество(set)

# s = {}
# print(s)
# print(type(s))
# lst=list(s)
# print(lst)

# a = set(["banana", "apple", "orange"])
# print(type(a))
# print(a)

# s = {i * i * i for i in range(10)}
# print(s)

# str1 = "я обычная строка"
# str2 = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
#
#
# def to_set(a):
#     return set(a)
#
#
# print(to_set(str1), len(to_set(str1)))
# print(to_set(str2), len(to_set(str2)))

# t = {"red", "green", "blue"}
# for i in t:
#     print(i)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # a = {i for i in lst if "a" not in i}
# a = {"A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"}
# print(a)

# users = {"Tom", "Alice", "Bob"}
# users.add("Ann")
# print(users)
# # user = "Rob"
# # if user in users:
# #     users.remove(user)
# #
# # print(users)
# # users.discard("Rob")
# # print(users)
# # users.pop()
# # print(users)
# users.clear()
# print(users)

# a = {1, 2, 3, 4, 5}
# b = {0, 4, 5, 6, 3}
# # c = a | b
# # c = a<b
# print(c)
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 |s6 | s7
#
# print(s)
# print(min(s))
# print(max(s))


# str1 = "Hello"
# str2 = "How are you"
# s1 = set(str1)
# s2 = set(str2)
# # # s = s1 | s2
# s3 = s1 & s2
# # print(s3)
# for i in s3:
#     print(i, end=" ")
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one = drawing ^ music
# print(one)
# both = drawing & music
# print(both)
# s1= one-both

# frozenset(замороженное множество)
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({"hello","world"})
# print(a)


# Словарь(dict)

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(d)

# d = {"one": 1, "two": 2}
#
# print(d)
# print(type(d))
#
# d1 = dict(one=1, t=2)
# print(d1)
# d = {"one": 1, "two": 2, "three": 3}
# print(list(d))
# # lst = ["one", "two", "three"]
# # print(dict(lst))
#
# a = [
#     ["one", 1],
#     ["two", 2],
#     ["three", 3]
# ]
# print(a)
# print(dict(a))

# d = {"one": 45, 0: "text", (1, 2, 3): "Кортеж", 43: [1, 2, 3, 4]}
# print(d[0][1])

# d = {input("key"): randint(1, 10) for i in range(3)}
# print(d)

#
# # print(d)
# # d["two"] = 200
# # d["one"] += 100
# print(d)
# del d["two"]
# print(d)
# for key in d:
#     print(key, ":", d[key])

# d = {i: input("Введите элемент словаря: ") for i in range(1, 5)}
# print(d)
# de = int(input("Введите ключ удаляемого элемента: "))
# try:
#     del d[de]
# except KeyError:
#     print("Такого ключа нет!")
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# print(d)

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core i5-3450", 5, 6400]
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.", sep="")
# while True:
#     n = input("№: ")
#     if n != "0":
#         qty = int(input("Количество:"))
#         goods[n][1] += qty
#     else:
#         break
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.", sep="")

# d = {"a": 1, "b": 2, "c": 3}
# d2 = d.copy()
# print("D=", d)
# print("D2=", d2)
# d["b"] = 5
# print("D=", d)
# print("D2=", d2)
# d2["e"] = 7
# print("D=", d)
# print("D2=", d2)

# # print(d["b"])
# # value = d.get("b","nokey")
# # print(value)
# print(d.keys())  # ключи
# print(d.values())  # значения
# print(d.items())  # ключи + значения
# for k, v in d.items():
#     print(k, v)

#
# print(d)
# # item = d.pop("b")
# # # item = d.popitem()
# #
# # print(item)
# # d.clear()
# # item = d.setdefault("e", 100)  #устанавливает значение по умолчанию
# d.update([("r", 7), ("c1", 6)])  # преобразует словарь
# d.update({"y": 65, "n": 64})
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = {}
# # z.update(x)
# # z.update(y)
# z = x | y
# print(z)

#
# d2 = dict()
# d2['name'] = d1.pop('name')
# d2['salary'] = d1.pop('salary')
#
# print(d1)
# print(d2)

# d1 = {"name": "Kelly", 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# d1['location'] = d1.pop('city')
# print(d1)
# a = {
#
#     "first": {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: "four",
#         5: "five"
#     }
#
# }
# print(a)
#
# sales = {
#     "Jhon": {"N": 3056, "S": 8463, "E": 8441, "W": 2594},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 4578, "E": 8441, "W": 2594}
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y], sep="")
# person = input("Name: ")
# region = input("Region: ")
# print(sales[person][region])
# new_data = int(input("New money: "))
# sales[person][region] = new_data
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y], sep="")

# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# print({key: value for key, value in d.items()})

# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# k = ''
# for i in lst:
#     if type(i) == str:
#         k = i
#         d[k] = []
#     else:
#         d[k].append(i)
# print(lst)
# print(d)

# zip() объединяет структуры данных

# a = [12, 1, 2, 3]
# b = ['Dec', 'Jan', 'Feb', 'March']
# c = [4.0, 8.5, 4.9, 7.3]
# d = dict(zip(a, b))
# print(d)
# f = {k: v for k, v in zip(b, a)}
# print(f)
# f = list(zip(a, b,c))
# print(f)
dic1 = {'name': 'Igor', 'email': 'igor@mail.com', 'job': 'Consultant'}
dic2 = {'name': 'Irina', 'email': 'irina@mail.com', 'job': 'Manager'}
for (k1, v1), (k2, v2) in zip(dic1.items(), dic2.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)
