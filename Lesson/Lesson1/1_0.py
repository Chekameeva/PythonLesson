# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут
# длиной m километров? При решении этой задачи
# нельзя пользоваться условной инструкцией if и циклами.

n = int(input("Введите количество км  \n"))
m = int(input("Введите количество всех км \n"))
print(-(-m//n))
