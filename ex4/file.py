# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def binar(n):
    
    if n > 1:
        binar(n//2)
        print(n%2, end=' ')
        
    

num_input = int(input('Введите число: '))



num_bin = binar(num_input)

print()

print(f'Перевели число {num_input} в десятичное {num_bin}')

