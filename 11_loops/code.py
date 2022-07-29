# Module introducing loops
import random

number = random.randint(1, 10)
user_input = input('Would you like to play a game? (Y/n) ')

if user_input.lower() == 'y' or user_input.lower() == '':
    quitMessage = 'If you want to quit, type "q"'
    print(quitMessage)
    while True:
        user_input = input('Guess a number between 1 and 10: ')
        if user_input == 'q':
            print('Bye!')
            break
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input == number:
                print('You guessed the number!')
                break
            elif user_input < number:
                print('Your guess is too low!')
            else:
                print('Your guess is too high!')
        else:
            print('Please enter a number!')

friendsList = ['Rolf', 'Bob', 'Jen', 'Anne']

for friend in friendsList:
    if friend == 'Jen':
        print(f'{friend} is my friend too!')
    else:
        print(friend)

for friend in range(len(friendsList) - 1):
    print(f'{friendsList[friend]} got a new friend {friendsList[friend + 1]}')

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
passingGrades = []
total = 0
for grade in grades:
    total += grade
    if grade >= 70:
        passingGrades.append(grade)

print(f'Amount of submitted grades is: {len(grades)}')
print(f'The total is {total}')
print(f'The average is {total / len(grades)}')
print(f'The number of passing grades is {len(passingGrades)}')
