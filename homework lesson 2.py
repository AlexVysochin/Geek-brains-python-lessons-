# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruits = ["mango", "apple", "apricot"]
i = 1
for fruit in fruits:
     print('{}{:>10}'.format(i,fruit))
     i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list1 = [1,2,3,15]
list2 = [2,15,28,16]
for x in list1:
        for y in list2:
                if x==y:
                        list1.remove(x)
                        print (list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list = [22,15,11,33,18]
a=0
for x in list:
        if list[a] % 2 == 0:
                list[a] = list[a]/4
        else:
                list[a]=list[a]*2
        a=a+1
print(list)
