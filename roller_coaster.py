print('Welcome to the roller coaster ride')

height = int(input('What is your height in cm?\n'))

ticket = 0
photo_price = 4
icecream_price = 3

if height >= 120:
    print('You are eligible to ride')
    age = int(input('What is your age?\n'))
    if age <= 18:
        ticket = 7
        print(f'you have a child ticket which is £{ticket}')
    elif age <= 22:
        ticket = 12
        print(f'You have a youth ticket which is £{ticket}')
    elif age < 45:
        ticket = 15
        print(f'You have an adult ticket which is £{ticket}')
    elif age >= 45 and age <= 55:
        ticket = 0
        print(f'You have a senior citizen ticket which is £{ticket}')
    photo = input(f'Do you want your photo taken? The price is £{photo_price} Y or N\n')
    icecream = input(f'Do you want icecream during rid? The price is £{icecream_price} Y or N\n')
    if photo == "Y" and icecream == "Y":
        ticket = ticket + icecream_price + photo_price
        print(f'Your total bill is £{ticket}')
    elif photo == "Y" and icecream == "N":
        ticket = ticket + photo_price
        print(f'Your total bill is £{ticket}')
    elif photo == "N" and icecream == "Y":
        ticket = ticket + icecream_price
        print(f'Your total bill is £{ticket}')
else:
    print('Sorry, you have to grow taller and have an even height before you can ride')