# # Задайте список из вещественных чисел.
# #  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# # ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
# # Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


num_intr = int(input('Введите число: '))

arr =[]
for i in range(num_intr) :
    arr.append(random.uniform(0.0, 10.0)*100//1/1000)
print(arr)



arr =[round(i%1, 2) for i in arr if i%1 != 0]
result = max(arr) - min(arr)
print(f'Разность = {result*1000//1/1000}')