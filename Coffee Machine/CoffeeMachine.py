espresso = {
    "water": 50,
    "coffee": 18,
}

latte = {
    "water": 200,
    "milk": 150,
    "coffee": 24,
}

cappuccino = {
    "water": 250,
    "milk": 100,
    "coffee": 24,
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
} 


def process_coins(): 
        print("Please insert coins.")
        quarters=int(input("How many quarters? "))*0.25
        dimes=int(input("How many dimes? "))*0.10
        nickels=int(input("How many nickels? "))*0.05
        pennies=int(input("How many pennies? "))*0.01
        total=quarters+dimes+nickels+pennies
        print(total)
        if total>bill:
            change=round(total-bill, 2)
            print(f"Here is ${change} in change.\nHere is your {coffee} ☕ Enjoy!")
            order=True
        elif total<bill:
            print(f"Sorry not enough money. Here is your refund.")
            order=True
        elif total==bill:
            print(f"Here is your {coffee} ☕ Enjoy!")
            order=True

print("WELCOME TO CAFE COFFEE DAY!\nEspresso:$1.50\nLatte:$2.50\nCappuccino:$3.00\n")

order=True
while order:
    coffee=input("What would you like? ")


    bill=0
    if coffee=="report" :
        for elements in resources: 
            print(f"{elements}:{resources[elements]}")
        order=True     
    elif coffee=="espresso":
        resources["Water"] -= espresso["water"]      
        resources["Coffee"] -= espresso["coffee"]
        bill += 1.50
        process_coins()
    elif coffee=="latte":
        resources["Water"] -= latte["water"]
        resources["Coffee"] -= latte["coffee"]
        resources["Milk"] -= latte["milk"] 
        bill += 2.50 
        process_coins()
    elif coffee=="cappuccino":
        resources["Water"] -= cappuccino["water"]
        resources["Coffee"] -= cappuccino["coffee"]
        resources["Milk"] -= cappuccino["milk"]
        bill+=3.00
        process_coins()     
    elif coffee=="off":
        order=False



     

     
