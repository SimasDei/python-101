# Destructuring variables Module

t = 5, 11
x, y = t

print(x, y)

studen_attendance = {
    'Rolf': 96,
    'Bob': 80,
    'Jen': 100,
    'Anne': 92
}
print(f"list of students is {list(studen_attendance.items())}")

for name, attendance in studen_attendance.items():
    print(f'{name} has {attendance}% attendance')

people = [('Bob', 42, 'Mechanic'), ('Rolf', 32, 'Engineer'), ('Jen', 45, 'Designer')]
for name, age, profession in people:
    print(f'{name} is a {profession} and is {age} years old')

# Heads and tails of a list
head, *tail = [1, 2, 3, 4, 5]
print(f'head is {head} and tail is {tail}')
