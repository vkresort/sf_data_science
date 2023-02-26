"""Game guess the number"""

import numpy as np

number = np.random.randint(1,101)# creating random number

# creating number for counting guesses
count = 0

while True:
    count+=1
    predict_number = int(input('Guess the number from 1 to 100 '))

    if predict_number > number:
        print('Predicted number is lower')

    elif predict_number < number:
        print('Predicted number is higher')

    else: 
        print(f'You guess correscty! It was = {number}, you guessed in {count}')
        break #exit game