#Name: Jaden Auville
# Prog Purpose: This program finds the personal prop tax for 6 months



#  PPT rate: 4.2% (annually)
#  Relief rate: 33% (for personal vechicle)

import datetime

############## define global variables ######################
# define tax rate and prices
PERSONAL_RATE = .042
TAX_RELIEF = .33

###################define global variables ###########
relief = 2 #1 is qualified, 2 is non-qualified
relief_amt = 0
assesed_value = 0

annual_amt = 0
six_month_amt = 0

############## Define program functions ################
def main():

    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate the tax amount for another vehicle? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            print("Thank you, have a nice day!")

def get_user_data():
    global relief, assesed_value
    print('**** PERSONAL PROPERTY TAX BILL ****')
    assesed_value = int(input("Assesed value of the vahicle: $"))
    relief = int(input("\nIs your vehicle eligible for tax relief? (1 for YES, 2 for NO): "))
    

def perform_calculations():
    global relief_amt, annual_amt, six_month_amt, pre_relief

    if relief == 1:
        pre_relief = PERSONAL_RATE * assesed_value
        relief_amt = pre_relief * TAX_RELIEF
        annual_amt = pre_relief - relief_amt
    else:
        annual_amt = PERSONAL_RATE * assesed_value

    six_month_amt = annual_amt / 2

def display_results():
    currency = '8,.2f'
    line = '--------------------------------------------------'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]

    print(line)
    print(' **** PERSONAL PROPERTY TAX BILL ****')
    print('    Please Pay in a Timely Manner')
    print('\tDate/Time: ' + dt_short)
    print(line)
    print('\tAssessed Value      $ ' + format(assesed_value,currency))
    print('\tRelief Amount       $ ' + format(relief_amt,currency))
    print('\tFull Annual Amount  $ ' + format(annual_amt,currency))
    print(line)
    print('\tTotal Due           $ ' + format(six_month_amt,currency))
############ call on main program to execute ############
main()

