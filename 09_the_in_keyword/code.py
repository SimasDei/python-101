# Module showcasing the use of the in keyword
import random

friends = ['Rolf', 'Bob', 'Jen', 'Anne']
print('Rolf' in friends)

moviesWatched = {'The Matrix', 'Green Book', 'Her'}
userMovie = input('What movie do you want to watch? ')
if userMovie in moviesWatched:
    print(f'You have already watched {userMovie}')
else:
    print(f'You have not watched {userMovie} yet')

magicNumber: int = random.randint(1, 10)
promptGame = input('Do you want to play a game? (y/n) ')
acceptedInput = ['y', 'yes', 'Y', 'Yes', 'YES']
if promptGame in acceptedInput:
    print('Let\'s play a game!')
    userNumber = int(input('Pick a number between 1 and 10: '))
    if userNumber == magicNumber:
        print('You guessed the magic number!')
    else:
        print(f'Sorry, you didn\'t guess the magic number. It was {magicNumber}')
else:
    print('Bye!')
