from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True

while  is_on:
    user_input = input('What would you like? (espresso/latte/cappuccino/):')
    if user_input == 'off':
        is_on = False
    else:
        print(user_input)
