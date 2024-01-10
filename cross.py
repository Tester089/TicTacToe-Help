from random import choice
from switch import switch

friend = "X"
enemy = "0"
space = "_"
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
       (0, 3, 6), (1, 4, 7), (2, 5, 8),
       (0, 4, 8), (2, 4, 6))


def cross(matrix):
    for case in switch(matrix.count(friend)):
        if case(0):
            return first_turn()
        elif case(1):
            return second_turn(matrix)
        elif case(2):
            return third_turn(matrix)
        else:
            return fourth_plus_turn(matrix)


def where_win(matrix, flag):
    for i in win:
        if (matrix[i[0]], matrix[i[1]], matrix[i[2]]).count(flag) >= 2:
            if matrix[i[0]] == space:
                return i[0]
            elif matrix[i[1]] == space:
                return i[1]
            elif matrix[i[2]] == space:
                return i[2]


def first_turn(*args, **kwargs):
    return 5


def second_turn(matrix):
    if all([(enemy != matrix[i]) for i in (0, 2, 6, 8)]):
        return 1
    elif where_win(matrix, friend):
        return where_win(matrix, friend)+1
    elif where_win(matrix, enemy):
        return where_win(matrix, enemy)+1
    else:
        return choice([index for index, value in enumerate(matrix) if value == space])+1


def third_turn(matrix):
    if where_win(matrix, friend):
        return where_win(matrix, friend)+1
    elif where_win(matrix, enemy):
        return where_win(matrix, enemy)+1
    else:
        return choice([index for index, value in enumerate(matrix) if value == space])+1


def fourth_plus_turn(matrix):
    if all([(enemy != matrix[i]) for i in (0, 2, 6, 8)]):
        return 1
    elif where_win(matrix, friend):
        return where_win(matrix, friend)+1
    elif where_win(matrix, enemy):
        return where_win(matrix, enemy)+1
    else:
        return choice([index for index, value in enumerate(matrix) if value == space])+1