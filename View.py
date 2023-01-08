import os

clear = lambda: os.system('cls')

def hello():
    clear()
    print("[]Меню")
    print("1. Вставка даних в таблицю")
    print("2. Оновлення даних в таблиці")
    print("3. Видалення даних в таблиці")

def show(mas):
    for element in mas:
        print(element)
        print("\n");

