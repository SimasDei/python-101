# Advanced Set Operations

friends = {'Rolf', 'Bob', 'Jen', 'Anne'}
abroad = {'Bob', 'Anne'}
localFriends = friends.difference(abroad)

print(f'Local friends: {localFriends}, the amount of friends is: {len(localFriends)}')

friends = localFriends.union(abroad)
print(f'Friends: {friends}, the amount of friends is: {len(friends)}')

art = {'Bob', 'Jen', 'Anne', 'Charlie', 'Eve'}
science = {'Jen', 'Charlie', 'Rolf', 'Adam', 'Gregory'}

studyBothSubjects = art.intersection(science)

print(f'Study both subjects: {studyBothSubjects}, the amount of friends is: {len(studyBothSubjects)}')
