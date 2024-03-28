#NAME:Xinnan Wei, Jaden Auville
# Prog Purpose: Palermo Pizza Company

import datetime

#define tax rate and prices
SMALL_PIZZA = 9.99
MEDIUM_PIZZA = 12.99
LARGE_PIZZA = 17.99
EXTRA_LARGE_PIZZA = 21.99
DRINK = 3.99
BREADSTICKS = 6.99
SALES_TAX_RATE = .055

#define global variables
num_pizzas = 0
num_drinks = 0
num_breadsticks = 0
cost_pizzas = 0
cost_drinks = 0
cost_breadsticks = 0
salestax = 0
total = 0
subtotal = 0

############    define program functions ############
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno == "n" :
            more = False
            print("Thank you for your order. Enjoy your meal!")


def get_user_data():
    global pizza_size, num_pizzas, num_drinks, num_breadsticks
    part1="Palermo Pizzas \n\tSmall (S) \n\tMedium (M) \n\tLarge (L) \n\tExtra Large (X)"
    part2="\nWhat size pizza would you like (S, M, L, X): "
    pizza_size = input(part1 + part2)
    pizza_size = pizza_size.upper()
    num_pizzas = int(input("How many pizzas would you like? "))
    num_drinks = int(input("How many drinks would you like? "))
    num_breadsticks = int(input("How many breadsticks would you like? "))

def perform_calculations():
    global cost_pizzas, cost_drinks, cost_breadsticks, subtotal, salestax, total
    if pizza_size == "S":
        cost_pizzas = num_pizzas*SMALL_PIZZA
    elif pizza_size == "M":
        cost_pizzas = num_pizzas*MEDIUM_PIZZA
    elif pizza_size == "L":
        cost_pizzas = num_pizzas*LARGE_PIZZA
    else:
        cost_pizzas = num_pizzas*EXTRA_LARGE_PIZZA
        
    cost_drinks = num_drinks*DRINK
    cost_breadsticks = num_breadsticks*BREADSTICKS
    subtotal = cost_pizzas + cost_drinks + cost_breadsticks
    salestax = subtotal*SALES_TAX_RATE
    total = subtotal + salestax

def display_results():
    currency='8,.2f'
    line='------------------------------'
    dt_full=str(datetime.datetime.now())
    dt_short=dt_full[0:16]
    
    print(line)
    print('**** Palermo Pizza ****')
    print('Your neighborhood Pizza shop')
    print(dt_short)
    print("Number of Pizzas     : "+str(num_pizzas))
    print("Number of Drinks     : "+str(num_drinks))
    print("Number of Breadsticks: "+str(num_breadsticks))
    print(line)
    print('Pizzas         $  ' + format(cost_pizzas,currency))
    print('Drinks         $  ' + format(cost_drinks,currency))
    print('Breadsticks    $  ' + format(cost_breadsticks,currency))
    print(line)
    print('Subtotal       $  ' + format(subtotal,currency))  
    print('Sales Tax      $  ' + format(salestax,currency))
    print('Total          $  ' + format(total,currency))
    print(line)
    


main()

    
