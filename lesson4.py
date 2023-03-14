# ===== Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# print("Выведем по возрастанию элементы из двух наборов !")
# n = int(input("Введите лимит первого множества: "))
# m = int(input("Введите лимит второго множества: "))

# num_list_1=[]
# for i in range(n):
#     num = int(input("Введите список 1 "))
#     num_list_1.append(num)
# print(num_list_1)

# num_list_2 = []
# for i in range(m):
#     num = int(input("Введите список 2 "))
#     num_list_2.append(num)
# print(num_list_2)

# num_list3 = num_list_1+num_list_2
# checked_nums_list = []
# for i in num_list3:
#     if num_list3.count(i) > 1 and i not in checked_nums_list:
#         checked_nums_list.append(i)
#         print(f"{i} - наш ответ!")

# ===== Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int( input("Введите количество кустов! ") )
print(f"А теперь - сколько ягод на кустах!")

array = list()
for i in range(n):
    x = int(input())
    array.append(x)

array_count = list()
for i in range(len(array) - 1):
    array_count.append(array[i - 1] + array[i] + array[i + 1])
array_count.append(array[-2] + array[-1] + array[0])
y = max(array_count)

print(f"{y} ягод за заход!")