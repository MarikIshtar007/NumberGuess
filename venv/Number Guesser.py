import random

print('********************************************')
print('*    WELCOME TO THE NUMBER GUESSING GAME   *')
print('********************************************')

outer = True
while outer:
    init = random.randint(1, 500)
    fin = init + 50
    print('The Number you need to guess lies between ', init, ' and ', fin)
    count = 0
    answer = random.randint(init, fin)

    while True:
        guess = int(input('Enter your Guess: '))
        if answer > guess:
            print('Your answer is lower than the number.')
            count += 1
            print('Your Number is between ', init, ' and ', fin)
        elif answer < guess:
            print('Your answer is greater than the number.')
            count += 1
            print('Your Number is between ', init, ' and ', fin)
        elif answer == guess:
            print('**************************************')
            print('**************************************')
            print('You got it! That was the ANSWER')
            print('Congratulations!!!')
            count += 1
            print('You guessed the number in ', count, ' guesses.')
            print('Thank you for playing!')
            print('**************************************')
            print('**************************************')
            replay = input('Would you like to play again ?')
            if replay.lower() == 'yes' or replay.lower() == 'y':
                outer = True
                break
            else:
                outer = False
                break
print("Thank you for Pllaying!!")
print("Exiting the Program......")
