# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

mas_a = []
num = int(input("Введите количество элементов в массиве: "))
for i in range(num):
    mas_a.append(int(input()))
x = int(input("Введите искомое число: "))
result = mas_a[0]
for i in mas_a:
    if abs(i - x) < abs(result - x):
        result = i
print(result)