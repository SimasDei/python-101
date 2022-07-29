# Dictionaries Module
# Dictionaries are a data structure that can store data in key-value pairs.
# Dictionaries are similar to arrays, but they are more flexible.
# Dictionaries are also more efficient than lists.

friend_ages = {
    'Rolf': 24,
    'Bob': 30,
    'Jen': 27,
    'Anne': 21,
    'Samantha': 35
}

friendKey = 'Bob'

print(f'{friendKey} is {friend_ages[friendKey]} years old')

friends = [{'name': 'Rolf', 'age': 24}, {'name': 'Bob', 'age': 30}, {'name': 'Jen', 'age': 27}]
firstFriendIndex = 0
firstFiend = friends[firstFriendIndex]
print(
    f"first person in friend group is {firstFiend['name']}, his age is {firstFiend['age']}")
