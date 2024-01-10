# Импорт функций для чтения ввода и стратегий для крестика и нолика
from data_loader import read_input
from cross import cross
from zero import zero

# Основная точка входа в программу
if __name__ == '__main__':
    # Загрузка данных с использованием функции read_input() из data_loader.py
    matrix = read_input()

    # Проверка количества соотношения крестиков и ноликов
    # Если разность равна нулю, то значит сейчас ходят крестики
    # Иначе они уже ходили и сейчас ходят нолики
    if matrix.count('X') - matrix.count("0") == 0:
        # Вызов стратегии для крестика в случае равенства
        result = cross(matrix)
    else:
        # Вызов стратегии для нолика в противном случае
        result = zero(matrix)

    # Вывод результата на экран
    print(result)
