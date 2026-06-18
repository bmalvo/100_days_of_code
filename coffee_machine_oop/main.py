from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
coffe_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while  is_on:
    user_input = input('What would you like? (espresso/latte/cappuccino/):')
    if user_input == 'off':
        is_on = False
    elif user_input == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        cost = drink.cost
        if drink:
            coffe_maker.is_resource_sufficient(drink)
            money_machine.make_payment(cost)
