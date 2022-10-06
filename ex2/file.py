# . Напишите программу, которая найдёт произведение пар чисел списка 
# (Cписок создаем как в предыдущем задании).
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random


num_inter = int(input('Введите число: '))

arr =[]
for i in range(num_inter):
    arr.append(random.randint(0,10))
print()
print('Создали массив')
print(arr)
print()

new_arr = []
for i in range((len(arr)+1)//2):
    new_arr.append(arr[i]*arr[len(arr)-1-i])
print('Новый массив')
print(new_arr)