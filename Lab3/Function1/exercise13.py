import random
def guess():
    print('Hello! What is your name?')
    name = input()
    print('Well, ', name, ' , I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    k = 0
    randomnumber = random.randint(1, 20)
    while True:
        x = int(input())
        if x == randomnumber:
            k += 1 
            print('Good job,', name, 'You guessed my number in', k, 'guesses!')
            break
        else:
            k += 1
            if x < randomnumber:
                print('Your guess is too low.')
            else:
                print('Your guess is too high.')
            print('Take a guess.')
guess()