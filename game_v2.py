"""Game: guess the number
Computer auto_mode"""

import numpy as np

number = np.random.randint (1,101)# creating number

def random_predict(number:int=1) -> int:
    count = 0
    while True:
        count +=1
        predict_number = np.random.randint(1,101) #generating a number from 1 to 100
        if number == predict_number:
            break # of they match exit the ciqle
    return (count)


def game_score (random_predicte) -> int:
    count_ls=[]
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=1000) #random list for 1k number from 1 to 100

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'your algoritm in average {score} guess number')
    return(score)


game_score(random_predict)