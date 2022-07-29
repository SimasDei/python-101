# Module showcasing how to get user input

name = input('What is your name? ')

greeting = 'Hello, {}'.format(name)

print(greeting)

size_input = input('How big is your house? (in square meters) ')
square_feet = int(size_input) * 10.7639
formatted_string = f"Your house is {square_feet} square feet."

print(formatted_string)
