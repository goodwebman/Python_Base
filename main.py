# ======================== String Methods ========================

name = "bro code"

print(len(name))  # 8
print(name.find('o'))  # Index of word
print(name.capitalize())  # First letter Up
print(name.upper())  # All letters Up
print(name.lower())  # All letters Down
print(name.isdigit())  # True or false (is it num?)
print(name.isalpha())  # Состоит ли эта переменная только из букв (без пробелов и цифр) - тут False "bro code"
print(name.count('o'))  # Кол-во 2
print(name.replace("bro", "dude", 1))  # Замена - 1 заменит первое вхождение

# ======================== String Slicing ========================

# slicing = [start:stop:step]
slicing = 'Oh, hello mate!'
print(slicing[::-1])  # Reversed string

website = "http://google.com"

slice = slice(7, -4)  # Срез от 7 до -4 (google)
print(website[slice])

# ======================== Nested loops ========================

# rows = int(input("How many rows?:  "))
# columns = int(input("How many columns?:  "))
# symbol = input("Enter a symbol to use:  ")

# for i in range(rows): # Ряд
#     for j in range(columns): # Колонка
#         print(symbol, end="") # Символ
#     print()


# for i in range(10):  # 5 - не будет, continue пропускает итерацию 
#     if i == 5:
#         continue
#     print(i)


# ======================== List Methods (11) ========================

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

# food.append("ice cream") - Добавляет в конец
# food.remove("hotdog") - Удаляет
# food.pop(i) # Возвращает элемент [на указанной позиции], удаляя его из списка.
# food.sort() - по алфавиту
# food.clear() - очищает
# food.count() - сколько таких элементов в списке
# food.insert(index,"orange") - добавляет на позицию (не удаляя другие)
# food.extend(list) - добавляет список в список
# food.index("hamburger") - индекс первого такого элемента
# food.reverse() - переворачивает
# food.copy() - копирует 1 в 1

# print(food)


# ======================== 2D LISTS ========================

drinks = ["coffe", "soda", "tea"]
dinner = ["pizza", "chicken", "hotdog"]
dessert = ["cake", "ice cream"]

foods = [drinks, dinner, dessert]
print(foods)

# ======================== Tuple and Tuple Methods (2) / Кортежи ========================

student = ("Bro", 21, "male")

print(student.count("Bro"))  # Только два метода
print(student.index("male"))

if "Bro" in student:
    print("Bro is here!")

# ======================== Set and Set Methods / Множества ========================

utensils = {"fork", "spoon", "knife"}  # - значения не могут повторяться ()
dishes = {"bowl", "plate", "cup"}

utensils.add('napkin')  # Добавляет в конец
utensils.remove("fork")  # Удаляет
# utensils.clear() - Очищает
dishes.update(
    utensils)  # update - обновляет/дополняет словарь dict с помощью пар ключ-значение из other, перезаписывая существующие ключи новыми значениями из other. Если ключ в словаре отсутствует, то он добавляется. Метод ничего не возвращает.
# Метод discard() — удаляет элемент из множества без генерации исключения (ошибки), если элемент отсутствует.


# update пример

# >>> x = {'one': 10, 'two': 20, 'three': None}
# >>> y = {'three': 30, 'four': 40, 'five': 50}
# >>> x.update(y)
# >>> x
# {'one': 10, 'two': 20, 'three': 30, 'four': 40, 'five': 50}


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

res = x.union(y)  # Складывает множества
res = x.intersection(y)  # Какие элементы одинаковые для этих множеств ("apple")
res = x.difference(y)  # Какие элементы разные для этих множеств ("banana","google","cherry","microsoft")

myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

myset3 = myset1.symmetric_difference(myset2)
# {1, 2, 5, 6, 7, 8} - Симметрическая разность множеств это множество,
# включающее все элементы исходных множеств, не принадлежащие одновременно обоим исходным множествам.
# Для этой операции существует метод symmetric_difference().

# Метод issubset()
# Для определения, является ли одно из множеств подмножеством другого, используется метод issubset()
# . Данный метод возвращает значение True, если одно множество является подмножеством другого,
# и False, если не является.

set1 = {2, 3}
set2 = {1, 2, 3, 4, 5, 6}

print(set1.issubset(set2))

# Метод issuperset()
# Для определения, является ли одно из множеств надмножеством другого, используется метод issuperset(). Данный метод возвращает значение True, если одно множество является надмножеством другого, в противном случае он возвращает False.

# Приведенный ниже код:

set1 = {'a', 'b', 'c', 'd', 'e'}
set2 = {'c', 'e'}

print(set1.issuperset(set2))

print(dishes)

# Метод isdisjoint()
# Для определения отсутствия общих элементов в множествах используется метод isdisjoint().
# Данный метод возвращает значение True, если множества не имеют общих элементов,
# и False, когда множества имеют общие элементы.

# Приведенный ниже код:

set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7}
set3 = {7, 8, 9}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
print(set2.isdisjoint(set3))

# ======================== Dictionaries / Словари ========================

capitals = {
    'USA': 'Washington DC',
    'India': 'New Dehli',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

# capitals.update({'German': 'Berlin'})

print(capitals.get('Germany'))  # True or False
print(capitals.keys())  # (['USA', 'India', 'China', 'Russia'])
print(capitals.values())  # (['Washington DC','New Dehli','Beijing','Moscow'])
print(
    capitals.items())  # dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

for key, value in capitals.items():
    print(key, value)

# USA Washington DC
# India New Dehli - вывод
# China Beijing
# Russia Moscow

# Метод popitem()
# Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение).

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info['surname'] = 'Sinclar'  # добавляем (щас его съест поп айтем)

item = info.popitem()

print(item)
print(info)


# ======================== def / args and kwargs ========================


def add(*args):  # args можно назвать как угодно - *danya ; *vasya - похуй
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(5, 6, 21))


def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title='Mr.', first='Bro', middle='Dude', last='Code')


def testing_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} {value}")


testing_kwargs(num1=1, num2=2, num3=3, num4=4, num5=5)

# Кваргс - для передачи переменных с ключем, аргс - без ключа


# ======================== String Format ========================

animal = "cow"
item = "moon"

# print("The {} jumped over the {}".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item))
# print("The {} jumped over the {}".format(animal="cow",item="moon")) если переменные не определены
# print("The {item} jumped over the {item}".format(animal="cow",item="moon")) - если переменные не определены


text = "The {} jumped over the {}"
print(text.format(animal, item))

# number = 3.14159

# print('The number pi is {:.3f}'.format(number))

number = 1000

print('The number is {:.3f}'.format(number))  # Сколько цифр выведется после точки
print('The number is {:,}'.format(number))  # Наводит красоту
print('The number is {:b}'.format(number))  # Бинарная запись числа
print('The number is {:o}'.format(number))  # Акто число
print('The number is {:X}'.format(number))  # Хекс

# ======================== Random ========================


import random

x = random.randint(1, 6)  # целое число от 1 до 6
y = random.random()  # число от 0 до 1 (float)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']

random.shuffle(cards)

print(cards)

# ======================== Try Except ========================

# try:
#     numerator = int(input("Введите делимое:  "))
#     denominator = int(input("Введите делитель:  "))
#     result = numerator / denominator
#     print(result)

# except ZeroDivisionError as e:
#     print(e)
#     print("На ноль делить нельзя! Сука! ")

# except ValueError as e:
#     print(e)
#     print("Число блять введи!")


# except Exception as e:
#     print(e)
#     print("Что то пошло не так :( ")
# #обработка любой ошибки

# finally:
#     print("end")


# ======================== Import os | Проверка файла ========================

import os

path = 'C:\Python Projects\Python basic stuff (12h)\import os text.txt'

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):  # проверка на файл
        print("That is a file")
    elif os.path.isdir(path):  # проверка на папку
        print("That is a directory!")
else:
    print("That location doesn't exist!")

# ======================== Import os | Чтение файла ========================
import os

# with open('test.txt') as file:
#     print(file.read())
# print(file.closed)

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

# ======================== Import os | Запись в файл ========================

text = 'Yoooooooooooooooooo\nThis is some text\nHave a good one!\n'

with open('test.txt', 'w') as file:  # Переписывает весь текст который был на данный
    file.write(text)

with open('test.txt', 'a') as file:  # Добавляет текст a - append
    file.write(text)

# ======================== Import os | Copy file ========================

import shutil

shutil.copyfile('test.txt', 'copy.txt')  # src, dst

# ======================== Import os | Move file ========================
import os

source = "text.txt"
destination = "C:\Python Projects\dude.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

# ======================== Import os | Delete file ========================

path = "delete me.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")

# ======================== lambda ========================

# 1 line function

double = lambda x: x * 2

multiply = lambda x, y: x * y

add = lambda x, y, z: x + y + z

full_name = lambda first_name, last_name: first_name + " " + last_name

age_check = lambda age: True if age >= 18 else False

print(double(500))
print(full_name("Vasya", "Bobrov"))

# ======================== Sort ========================

# sort() method = used with list
# sort() function = used with iterables


# sort () сортирует список на месте, изменяя его индексы

# sorted () возвращает новый отсортированный список, оставляя исходный список неизменным - записовать в другую переменную


students = ["Squidward", "Sandy", "Patrik", "Spongebob", "Mr.Krabs"]

students.sort()  # В алфавитном порядке
# students.sort(reverse=True)

for i in students:
    print(i)

# - сорт работает с списком

# Чтобы так сделать с tuple (кортежем), нужно:

# sorted_students = sorted(students)

# for i in sorted_students:
# print(i)


# Сортировка кортежей в списке

students_2 = [("Squidward", "F", 60),
              ("Sandy", "A", 33),
              ("Patrik", "D", 36),
              ("Spongebob", "B", 20),
              ("Mr.Krabs", "C", 78)]

grade = lambda grades: grades[1]
age = lambda ages: ages[2]

# name.sort(key= lambda function, reverse if u want)

students_2.sort(key=age, reverse=True)

for i in students_2:
    print(i)

students_3 = (("Squidward", "F", 60),
              ("Sandy", "A", 33),
              ("Patrik", "D", 36),
              ("Spongebob", "B", 20),
              ("Mr.Krabs", "C", 78))

students_3 = sorted(students_3, key=age)

for i in students_3:
    print(i)

# ======================== Map ========================


# map()

# map(function,iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

b = map(int, ['1', '2', '3', '4', '5', '6'])  # Преобразует строку в числа
sum = 0
for i in b:
    sum += i  # Складываем их
print(sum)

# map - Два параметра (функция, сам объект) - проходится по каждому элементу


# ======================== Filter ========================

# Название говорит само за себя (фильтрует объект)


friends = [("Rachel", 19),
           ("Dima", 18),
           ("Vlad", 17),
           ("Danil", 21),
           ("Dima", 20)]

age = lambda data: data[1] >= 18

driknig_buddies = list(filter(age, friends))

for i in driknig_buddies:
    print(i)

# ======================== Reduce ========================

# reduce - функция библиотеки functools

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

# word = "".join(letterds) - тоже самое методом join


factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)

# ======================== List comprehension ========================


squares = []

for i in range(1, 11):
    squares.append(i * i)
print(squares)

squares_comp = [i * i for i in range(1, 11)]  # - тоже самое, но короче

print(squares_comp)

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# passed_students = list(filter(lambda x: x >= 60, students))

passed_students = [i for i in students if i >= 60]  # тоже самое, но блять опять короче)

passed_students_f = [i if i >= 60 else "Failed" for i in students]
print(passed_students)
print(passed_students_f)

# ======================== Dictionary comprehension ========================

# dictionary = {key: expression for (key,value) in iterable.items()}

cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

cities_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudly'}

sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather)

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
print(desc_cities)


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"


def_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(def_cities)

# ======================== Zip ========================


username = ["Dude", "Bro", "Mister"]
password = ("p@ssword", "abc123", "guest")

# users = zip(username,password)

# for i in users:
#     print(i)


users = dict(zip(username, password))

for key, value in users.items():
    print(key + " : " + value)

# ======================== threading ========================

import time
import threading


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffe():
    time.sleep(4)
    print("You drankcoffe")


def study():
    time.sleep(5)
    print("You finish study")


# через вызов всех функций =>  12 секунд

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffe, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# через потоки => 5 секунд

print(threading.active_count())
print(threading.enumerate())

# ======================== daemon threads 😈 ========================
import threading
import time


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:", count, "seconds")


daemon = threading.Thread(target=timer, daemon=True)
daemon.start()

answer = input('Do you wish to exit? ')

# ======================== multiprocessing ========================

from multiprocessing import Process, cpu_count


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    a = Process(target=counter, args=(1000000000,))
    b = Process(target=counter, args=(1000000000,))
    c = Process(target=counter, args=(1000000000,))
    d = Process(target=counter, args=(1000000000,))
    e = Process(target=counter, args=(1000000000,))
    f = Process(target=counter, args=(1000000000,))  # - запятая обязательно
    g = Process(target=counter, args=(1000000000,))
    h = Process(target=counter, args=(1000000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print('finished in:', time.perf_counter(), 'seconds')


if __name__ == '__main__':
    main()


    # ======================== decorators ========================

    def hello_world():
        print('Hello world!')


    def decorator_function(func):
        def wrapper():
            print('Функция-обёртка!')
            print('Оборачиваемая функция: {}'.format(func))
            print('Выполняем обёрнутую функцию...')
            func()
            print('Выходим из обёртки')

        return wrapper


    @decorator_function
    def hello_world():
        print('Hello world!')


def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage()

# Пузырьковая сортировка

nums = [2, 5, 1, 8, 7, 4, 3, 6, 9]
print(nums)

for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)

# Последовательность Фибоначчи

f1 = f2 = 1
n = 10

print(f1, end=' ')
print(f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
