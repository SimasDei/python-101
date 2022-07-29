# Module which showcases the use of boolean values

equalOperator = 5 == 4 + 1
notEqualOperator = 5 != 6
greaterThanOperator = 5 > 2
lessThanOperator = 5 < 2

print(f'5 == 4 + 1: {equalOperator}')
print(f'5 != 6: {notEqualOperator}')
print(f'5 > 2: {greaterThanOperator}')
print(f'5 < 2: {lessThanOperator}')

friends = ['Rolf', 'Bob', 'Jen', 'Anne']
abroad = ['Rolf', 'Bob', 'Jen', 'Anne']
print(f'abroad variable is a reference to friends: {abroad is friends}')

isEqual = friends == abroad
print(f'Friends == abroad: {isEqual}')
abroad = friends
print(f'abroad variable is a reference to friends: {abroad is friends}')

# change to check commit Author
# another change to check commit Author, changed local git config
