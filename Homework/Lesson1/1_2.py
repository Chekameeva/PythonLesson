# Tребуется написать программу, которая проверяет счастливость билета.

n = int(input("Введите номер билета: "))
left = 0
right = 0
for i in range(6):
    if i < 3:
        right += n // 10**i % 10
    else:
        left += n // 10**i % 10
if left == right:
    print("Да")
else:
    print("Нет")
