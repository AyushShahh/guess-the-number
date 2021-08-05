import random

guesses_made = 0
name = input('Hey there! What is your name?\n')

number = random.randint(1, 100)

print('\nWell %s... I am thinking of a number between 1 and 100\n' % name)
print('I want you to guess the number.')
print('You have 10 guesses.\n')

while guesses_made < 11:
    guess = int(input('Make a guess: '))
    guesses_made += 1

    if guess < 1 or guess > 100:
        print('> The number should be between 1 and 100.\n')
    if number > guess > 0:
        print('> Your guess is low.\n')
    if 101 > guess > number:
        print('> Your guess is high.\n')
    if guess == number:
        break

if guess == number:
    print('Great job %s, You guessed my number in %d guesses.' % (name, guesses_made))
else:
    print('Nope, the number I was thinking was %d.' % number)
