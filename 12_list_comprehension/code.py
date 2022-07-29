numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled = []

for number in numbers:
    doubled.append(number * 2)

print(f'doubled in loop of 10: {doubled}')


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonnacised = []

for number in numbers:
    fibonnacised.append(fibonacci(number))

print(fibonnacised)

# List Comprehension

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numDoubled = [number * 2 for number in num]
print(f'numDoubled: {numDoubled}')

friends = ['Rolf', 'Bob', 'Jen', 'Anne', 'Sebastian', 'Sven']
statsWithCharacter = 'S'
sFriends = [friend for friend in friends if friend.startswith(statsWithCharacter)]
print(f'friends where first name starts with an {statsWithCharacter}: {sFriends}')
print('friends: ', id(friends), 'sFriends: ', id(sFriends))
