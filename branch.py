# Name: Jaden Auville
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime


# define tax rate, service fee, and prices
ADULT_MEAL = 19.95
KIDS_MEAL = 11.95
SALES_TAX_RATE = .062
SERVICE_FEE = .1

# define global variables
num_adult_meals = 0
num_kids_meals = 0
subtotal_adult = 0
subtotal_child = 0
subtotal = 0
sales_tax = 0
servicefee = 0
total = 0


############    define program functions ##############
def main():

        more_meals = True

        while more_meals:
            get_user_data()
            perform_calculations()
            display_results()

            yesno = input("\nWould you like to order again (Y or N)? ")
            if yesno == "n" or yesno =="N":
                more_meals = False
                print("Thank you for your order. Enjoy your meal!")


def get_user_data():
    global num_adult_meals, num_kids_meals
    num_adult_meals = int(input("Number of adult meals: "))
    num_kids_meals = int(input("Number of kids meals: "))
    

def perform_calculations():
    global subtotal_adult, subtotal_child, subtotal, sales_tax, total, servicefee
    subtotal_adult= ADULT_MEAL*num_adult_meals
    subtotal_child= num_kids_meals * KIDS_MEAL
    subtotal = subtotal_adult + subtotal_child
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    servicefee = total * SERVICE_FEE


def display_results():
    line='---------------------------------'
    dt_full=str(datetime.datetime.now())
    dt_short=dt_full[0:16]
    
    print('---------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print(dt_short)
    print('---------------------------------')
    print('Adult Meals       $' + format (subtotal_adult, '8,.2f'))
    print('Kids Meals        $' + format (subtotal_child, '8,.2f'))
    print('Subtotal          $' + format (subtotal,'8,.2f'))
    print('Sales Tax         $' + format (sales_tax, '8,.2f'))
    print('Service Fee       $' + format (servicefee, '8,.2f'))
    print(line)
    print('Total             $' + format (total, '8,.2f'))



##########  call on main program to execute ##########
main()
