import random

guesses_made = 0
name = input('Hey there! What is your name?\n')

number = random.randint(1, 100)

print('\nWell %s... I am thinking of a number between 1 and 100.\n' % name)
print('I want you to guess the number.')
print('You have 8 guesses\n')

while guesses_made < 9:
    guess = int(input('Make a guess: '))
    guesses_made += 1

    if guess < 1 or guess > 100:
        print('> The number is between 1 and 100.\n')
    if number > guess > 0:
        print('> The number is higher than %d.\n' % guess)
    if 101 > guess > number:
        print('> The number is lower than %d.\n' % guess)
    if guess == number:
        break

if guess == number:
    print('\nGreat job %s! You guessed the number in %d guesses.' % (name, guesses_made))
else:
    print('\nYou ran out of your guesses. The number I was thinking was %d.' % number)
