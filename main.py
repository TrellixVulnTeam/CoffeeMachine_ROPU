menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#     []       {}      \
money = 0


def report(resource, money_balance):
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")
    print(f"Money: ${money_balance}")


def wallet():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    balance_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return balance_money


def coffee_request(req):
    bill_req = menu[req]['cost']
    water_req = menu[req]['ingredients']['water']
    coffee_req = menu[req]['ingredients']['coffee']
    milk_req = menu[req]['ingredients']['milk']
    return bill_req, water_req, coffee_req, milk_req


def change_money(req):
    bill, water, coffee, milk = coffee_request(request)
    change = balance - bill
    global money
    money += bill
    resources["water"] -= water
    resources["coffee"] -= coffee
    resources["milk"] -= milk
    print(f"Here is ${change} in change.")
    print(f"Here is your {req} ☕ Enjoy!")


def game():
    bill, water, coffee, milk = coffee_request(request)
    if balance >= bill and resources["water"] >= water and resources["coffee"] >= coffee and resources[
        "milk"] >= milk:
        change_money(request)
    elif balance < bill:
        print("Sorry that's not enough money. Money refunded.")
    elif resources["water"] < water:
        print("Sorry there is not enough water.")
    elif resources["coffee"] < coffee:
        print("Sorry there is not enough coffee.")
    elif resources["milk"] < milk:
        print("Sorry there is not enough milk.")


turn_on = True
while turn_on:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request == "report":
        report(resources, money)
    elif request == "off":
        turn_on = False
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        balance = wallet()
        if request == "espresso":
            game()
        elif request == "latte":
            game()
        elif request == "cappuccino":
            game()
    else:
        print("Your answer is Invalid. Please try again.")
