# Module to showcase lists tuples and sets

# List
l = [1, 2, 3, 4, 5]
l[0] = -1
l.append(6)
for i in l:
    print(f'value of i is {i}')

print(f'first value of list is {l[0]}')

# Tuple
t = (6, 7, 8, 9, 10)
for i in t:
    print(f'value of i is {i}')

print(f'first value of tuple is {t[0]}')

# Set
s = {11, 12, 13, 14, 15}
s.add(16)
for i in s:
    print(f'value of i is {i}')

print(f'first value of set is {s.pop()}')
