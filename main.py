# TODO 1. Give welcome message
# TODO 2. Ask what the user would like and allow report input to display a report of ingredients
# TODO 3. The word 'off' should turn the machine off.
# TODO 4. Report should include levels of each ingredient
# TODO 5. When user makes a selection, code should check that there are sufficient levels of ingredients.
# TODO 6. If there is sufficient levels of ingredients, prompt user for change
# TODO 7. If not enough ingredients or change, money should be refunded
# TODO 8. If change is sufficient the money gets added to the machine, if too much money a refund is given
# TODO 9. After the machine makes the drink, the ingredients should be deducted from machine
# TODO 10. After drink is made and resourced reduced, give drink to user.

import resources

# set state of the coffee machine
off = False



def give_report():
    print(f"Water: {resources.resources['water']}ml\n"
          f"Milk: {resources.resources['milk']}ml\n"
          f"Coffee: {resources.resources['coffee']}ml")


def check_ingredients(coffee_choice):
    if coffee_choice == 'espresso':
        if resources.MENU[coffee_choice]["ingredients"]["water"] > resources.resources["water"]:
            print("Not enough water")
            return False
        elif resources.MENU[coffee_choice]["ingredients"]["coffee"] > resources.resources["coffee"]:
            print("Not enough coffee")
            return False
        else:
            return True
    else:
        if resources.MENU[coffee_choice]["ingredients"]["water"] > resources.resources["water"]:
            print("Not enough water")
            return False
        elif resources.MENU[coffee_choice]["ingredients"]["coffee"] > resources.resources["coffee"]:
            print("Not enough coffee")
            return False
        elif resources.MENU[coffee_choice]["ingredients"]["milk"] > resources.resources["milk"]:
            print("Not enough milk")
            return False
        else:
            return True


def get_change():
    total = 0
    print("Input Change")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total += (quarters * 0.25)+(dimes * .10)+(nickels * 0.05)+(pennies*0.01)
    return total


def check_change(change, coffee_choice):

    if change < resources.MENU[coffee_choice]["cost"]:
        print("Not enough change")
        return False
    elif change > resources.MENU[coffee_choice]["cost"]:
        refund = change - resources.MENU[coffee_choice]["cost"]
        print(f"Here's a refund of {refund:.2f}.")
        return True
    else:
        return True


def deduct_resources(coffee_choice):
    if coffee_choice == 'espresso':
        water_deduct_amount = resources.MENU[coffee_choice]["ingredients"]["water"]
        coffee_deduct_amount = resources.MENU[coffee_choice]["ingredients"]["coffee"]
        resources.resources["water"] -= water_deduct_amount
        resources.resources["coffee"] -= coffee_deduct_amount
    else:
        water_deduct_amount = resources.MENU[coffee_choice]["ingredients"]["water"]
        coffee_deduct_amount = resources.MENU[coffee_choice]["ingredients"]["coffee"]
        milk_deduct_amount = resources.MENU[coffee_choice]["ingredients"]["milk"]
        resources.resources["water"] -= water_deduct_amount
        resources.resources["coffee"] -= coffee_deduct_amount
        resources.resources["milk"] -= milk_deduct_amount



# coffee machine main function
def coffee_machine():

    coffee_choice = input("What would you like:\n Espresso\nLatte\nCappuccino\n")
    if coffee_choice == 'off':
        global off
        off = True
    elif coffee_choice == 'report':
        give_report()
    else:
        enough_ingredients = check_ingredients(coffee_choice)
        if enough_ingredients == True:
            print("There was enough ingredients.")
            change = get_change()
            enough_change = check_change(change, coffee_choice)
            if enough_change == True:
                resources.resources["money"] = resources.MENU[coffee_choice]["cost"]
                print(f"Here is your {coffee_choice}!")
                deduct_resources(coffee_choice)



print("Ready for a coffee?")
# while the machine is not turned off, let users use machine
while off == False:
    coffee_machine()
print("Good-Bye!")

