__author__ = 'Высочин Алексей Львович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

i = 0
while True:
  i += 1
  print (i)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input ("Введите число a: "))
b = int(input ("Введите число b: "))
print (‘a= ', a, ‘b=', b)
a,b=b,a
print (‘a= ', a, ‘b=', b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


a = int (input ("Сколько вам лет? "))
if a >= 18:
    print ("Доступ рашрешен")
else:
    print ("Извините, пользование данным ресурсом только с 18 лет")
