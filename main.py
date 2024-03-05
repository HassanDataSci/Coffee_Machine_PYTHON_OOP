
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
is_on = True

def check_res(ing_check):
    for item in ing_check:
        if ing_check[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def money_collection():
    global profit
    print("Please instert coins:")
    profit = int(input("how many quarters?: ")) * 0.25
    profit += int(input("how many dimes?:")) * 0.10
    profit += int(input("how many nickles?: ")) * 0.05
    profit += int(input("how many pennies?:")) * 0.01
    if profit == drink["cost"]:
        print("There you go fuck your coffee!!")

    elif profit < drink["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif profit > drink["cost"]:
        change = profit - drink["cost"]
        print(f"Here is ${change} dollars in change.")

def make_coffee(inge):
    for values in inge:
        resources[values] -= inge[values]









#print(MENU[choice]['ingredients']["water"])

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        if check_res(drink["ingredients"]):
            money_collection()
            make_coffee(drink["ingredients"])





