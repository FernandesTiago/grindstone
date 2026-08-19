# game.py

import random, time

player = {
    "woodcutting_xp": 0,
    "firemaking_xp": 0,
    "inventory": {},
}

def add_item(item, quantity):
    if item in player["inventory"]:
        player["inventory"][item] += quantity
    else:
        player["inventory"][item] = quantity

def remove_item(item, quantity):
    if player["inventory"].get(item, 0) < quantity:
        return False

    player["inventory"][item] -= quantity

    if player["inventory"][item] == 0:
        del player["inventory"][item]

    return True

def can_afford(price):
    return player["inventory"].get("coins", 0) >= price

def buy_item(item, quantity, price):
    if not can_afford(price):
        print("You don't have enough money")
        return False

    remove_item("coins", price)
    add_item(item, quantity)
    return True

SHOP = {
    "1": ("bronze axe", 25),
    "2": ("bronze pickaxe", 25),
}

def shop():
    print("What would you like to buy? 'Q' to quit")
    for key, (item, price) in SHOP.items():
        print(f"{key}) {item} - {price}c")

    choice = input("> ").upper()
    if choice == "Q":
        return

    if choice not in SHOP:
        print("Invalid choice")
        return

    item, price = SHOP[choice]
    if buy_item(item, 1, price):
        print(f"You bought a {item}!")
        time.sleep(2)
    
def chop_tree():
    if "bronze axe" not in player["inventory"]:
        print("You need an axe!")
        return
    add_item("logs", 1)
    player["woodcutting_xp"] += 25
    print("You get some logs. (+25 Woodcutting XP)")

def show_inventory():
    print("\n--- Inventory ---")
    print(f"Coins: {player['inventory'].get('coins', 0)}")
    for item, qty in player["inventory"].items():
        if item == "coins":
            continue
        print(f"{item} x{qty}")

def gather_coins():
    print("gathering coins on the floor... (press Ctrl + C to stop)")
    try:
        while True:
            time.sleep(2.4)
            amount = random.randint(1,100)
            add_item("coins",amount)
            if amount == 1:
                print("You collected 1 coin")
            else:
                print(f"you collected {amount} coins")

    except KeyboardInterrupt:
        print("you stop collecting")

MENU = {
    "1": ("Inventory", show_inventory),
    "2": ("Shop", shop),
    "3": ("Gather coins", gather_coins),
    "4": ("Chop tree", chop_tree),
}

while True:
    print()
    for key, (label, _) in MENU.items():
        print(f"{key}) {label}")
    print("Q) Quit")

    choice = input("> ").upper()
    if choice == "Q":
        break

    if choice in MENU:
        MENU[choice][1]()
    else:
        print("Invalid choice")