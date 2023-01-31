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

def display_info(name, age):
    print("Name:", name, "\nAge:", age, end="\n\n")


display_info("Ira", 23)
display_info(age=23, name="Ira")
