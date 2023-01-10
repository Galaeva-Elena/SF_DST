"""Игра 'Угадай число'
Компьютер сам загадывает и угадывает число
"""

import math
import numpy as np

def game_core_v3(number:int=1) -> int:
    """Рандомно угадываем число
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
       int: Число попыток.
    """
    
    count = 0
    start = 0
    finish = 100

    while True:
        count += 1
        predict_number = start + math.ceil((finish-start)/2)   # предполагаемое число 

        if number > predict_number:
            start = predict_number
            #print(start, finish)
        elif number < predict_number:
            finish = predict_number 
            #print(start, finish)
        else: 
            #print(f'Угадали!!! Это было число {number}')
            break # конец игры, если угадали

    return(count)


def score_game(game_core_v3) -> int:   
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
    
    Args:
        game_core_v3 ([type]): Функция угадывания.

    Returns:
       int: Среднее количество попыток.
    """
    
    count_lst = []
    np.random.seed(1)   # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_lst.append(game_core_v3(number))
    
    score = int(np.mean(count_lst))
    print(f'Наш алгоритм угадывает число в среднем за {score} попыток')
    return score


score_game(game_core_v3)
