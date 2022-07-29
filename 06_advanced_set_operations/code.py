# Advanced Set Operations

friends = {'Rolf', 'Bob', 'Jen', 'Anne'}
abroad = {'Bob', 'Anne'}
localFriends = friends.difference(abroad)

print(f'Local friends: {localFriends}, the amount of friends is: {len(localFriends)}')
