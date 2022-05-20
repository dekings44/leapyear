print('Welcome to a leap year calculator!!!')

year = int(input('Please enter a year. eg. 2020\n'))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'Yay!! {year} is a leap year')
        else:
            print(f'{year} did not satisfy condition 3 for a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

