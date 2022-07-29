user_age = input('How old are you? ')
years = int(user_age)
months = years * 12
days = years * 365
minutes = years * 525600
seconds = years * 365 * 24 * 60 * 60
message = f"You are {years} years, {months} months, {days} days, {minutes} minutes, and {seconds} seconds old."
print(message)
