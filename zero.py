from random import choice

# Определение игровых символов
friend = "0"  # Нолик
enemy = "X"   # Крестик
space = "_"   # Пустое поле

# Комбинации выигрышных ходов
win = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтали
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикали
    (0, 4, 8), (2, 4, 6)              # Диагонали
)


def zero(matrix):
    # Определение первого или последующего хода в зависимости от текущей ситуации на поле
    if matrix.count(friend) == 0:
        return first_turn(matrix)  # Первый ход
    else:
        return second_plus_turn(matrix)  # Последующие ходы


def where_win(matrix, flag):
    # Проверка, есть ли возможность выиграть или блокировать противника
    for i in win:
        if (matrix[i[0]], matrix[i[1]], matrix[i[2]]).count(flag) >= 2:
            if matrix[i[0]] != flag:
                return i[0]
            elif matrix[i[1]] != flag:
                return i[1]
            elif matrix[i[2]] != flag:
                return i[2]


def first_turn(matrix):
    # Первый ход: выбор центральной ячейки, если доступна, иначе угловой
    if space in matrix[5 - 1]:
        return 5
    elif space in matrix[1 - 1]:
        return 1


def second_plus_turn(matrix):
    # Выбор хода для блокировки или выигрыша, либо случайный ход
    if where_win(matrix, friend):
        return where_win(matrix, friend) + 1
    elif where_win(matrix, enemy):
        return where_win(matrix, enemy) + 1
    else:
        return choice([index for index, value in enumerate(matrix) if value == space]) + 1
