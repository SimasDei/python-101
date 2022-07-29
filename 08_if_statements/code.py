# Module showcasing the use of if statements

dayOfTheWeek = input('What day is it? ')
dayOfTheWeek = dayOfTheWeek.lower().strip()

if dayOfTheWeek == 'monday':
    print('It\'s Monday!')
elif dayOfTheWeek == 'tuesday':
    print('It\'s Tuesday!')
elif dayOfTheWeek == 'wednesday':
    print('It\'s Wednesday! My Dudes!')
elif dayOfTheWeek == 'thursday':
    print('It\'s Thursday!')
elif dayOfTheWeek == 'friday':
    print('Happy Big Friday!')
elif dayOfTheWeek == 'saturday':
    print('It\'s Saturday!')
elif dayOfTheWeek == 'sunday':
    print('It\'s Sunday!')
else:
    print('Excuse me, what day is it? Try again bucko!')
