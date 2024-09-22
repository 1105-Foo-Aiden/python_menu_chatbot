import time

def Message():
    print("Invalid choice, please try again")

def get_name():
    name = input("Enter your name: ")
    return name

def Milk_choice():
    print("What kind of milk would you like?")
    type = input("[a] Whole milk \n[b] Almond milk \n[c] Oat milk \n")
    if type == 'a':
        return "Whole milk"
    elif type == 'b':
        return "Almond Milk"
    elif type == 'c':
        return "Oat Milk"
    else:
        Message()
        Milk_choice()

def latte():
    print("You ordered a Latte. Would you like it with milk or without milk?")
    milk = input("[a] With milk\n[b] Without milk \n")
    if milk == 'a':
        milk_choice = Milk_choice()
        return (f"Latte with {milk_choice}")
    elif milk == 'b':
        return "Latte without milk"
    else:
        Message()
        latte()

def Coffee():
    print("You ordered a Coffee. Would you like it with sugar or without sugar?")
    req = input("[a] Yes I would like Sugar\n[b] No I would not like sugar\n")
    if req == 'a':
        sugars = input("How many sugars would you like? \n")
        return (f"Coffee with {sugars} sugar(s)")
    elif req == 'b':
        return "Coffee without sugar"
    else :
        Message()
        Coffee()
        
def Frap():
    print("You ordered a a Frappuccino. Would you like it with or without whipped cream?\n")
    choice = input("[a] With\n[b] Without\n")
    if choice == 'a':
        return "Frap with whipped cream"
    elif choice == 'b':
        return "Frap without whipped cream"
    else:
        Message()
        Frap()

def confrm_Order(drink):
    correct = input(f"You have ordered {drink} is this correct? (y/n)\n")
    if correct == 'y':
        name = get_name()
        print(f"Thank you {name}, your order will be out shortly")
        time.sleep(2)
        print(f"Here you are {name}, your {drink}. Thank you for shopping with us, please come again")
    elif correct == 'n':
        print("I'm sorry to hear that, let's start over")
        get_order()
    else:
        Message()
        confrm_Order(drink)

def get_order():
    order = input("What would you like to order? \n [a] Coffee \n [b] Latte \n [c] Frapachino\n ")
    drink = ''
    
    if order == 'a':
        drink = Coffee()
    elif order == 'b':
        drink = latte()
    elif order == 'c':
        drink = Frap()
    else:
        Message()
        get_order()
    
    confrm_Order(drink)

get_order()

