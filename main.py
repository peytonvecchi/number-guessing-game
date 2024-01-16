import random

#getting random number
random_number = random.randint(1, 20)

user_guess = 0
times_guessed = 0

#prompting user to guess the random number
print('I am thinking of a number between 1 and 20.')
print('Take a guess')

#repeating user prompts until user guesses the number
#incrementing 'times_guessed' every time the user guesses
while user_guess != random_number:

    user_guess = int(input())

    if user_guess < random_number:

        print('Too low, try again')        

    else:

        print('Too high, try again')
        
    times_guessed += 1

#congratualting the user once they guess the number
if times_guessed > 1:

    print(f'Good job! You guessed my number in {times_guessed} guesses!')

else:

    print(f'Wow! you guessed my number in {times_guessed} guess! You have my respect.')


