print('Welcome to Primed Pizzaria')

cheese_pizza = 15
veggie_pizza = 14.5
pepperoni_pizza = 26
meat_pizza = 14

quest = input('DO you want Pizza? Y or N\n')




if quest == "Y":
    pizza_flavour = input('What flavour of pizza do you want? cheese, veggie, pepperoni or meat?\n')
    pizza_size = input('What size of pizza do you want? S, M or L\n')
    if pizza_flavour == "cheese":
        if pizza_size == "S":
            bill = cheese_pizza * 0.5
            print(f'Your bill is £{bill}')
        elif pizza_size == "M":
            bill = cheese_pizza * 0.75
            print(f'Your bill is £{bill}')
        else:
            print(f'Your bill is £{cheese_pizza}')
    elif pizza_flavour == "veggie":
        if pizza_size == "S":
            bill = veggie_pizza * 0.5
            print(f'Your bill is £{bill}')
        elif pizza_size == "M":
            bill = veggie_pizza * 0.75
            print(f'Your bill is £{bill}')
        else:
            print(f'Your bill is £{veggie_pizza}')
    elif pizza_flavour == "pepperoni":
        if pizza_size == "S":
            bill = pepperoni_pizza * 0.5
            print(f'Your bill is £{bill}')
        elif pizza_size == "M":
            bill = pepperoni_pizza * 0.75
            print(f'Your bill is £{bill}')
        else:
            print(f'Your bill is £{pepperoni_pizza}')
    elif pizza_flavour == "meat":
        if pizza_size == "S":
            bill = meat_pizza * 0.5
            print(f'Your bill is £{bill}')
        elif pizza_size == "M":
            bill = meat_pizza * 0.75
            print(f'Your bill is £{bill}')
        else:
            print(f'Your bill is £{meat_pizza}')
    else:
        print(f'Please choose a flavour {pizza_flavour}')    

else:
    print('Thank you')