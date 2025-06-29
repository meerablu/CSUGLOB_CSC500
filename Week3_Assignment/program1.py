###############program start #################
import sys
from array import array # using the array library  to store the 2 parts of the meal price
from decimal import Decimal # selected the Decimal datatype for value precision reasons instead of float
def mainprog(): # Our function name mainprog       
    try:
        print("Welcome to Python Restaurants!")
        tip = Decimal('0.18') #assigned tip percentage value 18%
        tax = Decimal('0.07') #assigned tax percentage value 7%
        user_input = input("Press enter to continue or Type Q to quit! ")
        if user_input == 'Q': #having a way to exit the program press Q
            print("Exiting program...Thank you!")
            sys.exit() # Exit gracefully
        else:
            print("Let\'s get your food bill ready!") # Go into the program cycle
            inputnum1 = input("Enter your total meal price: ") # Ask the user to enter the meal price
            stillcheckinginputval = True
            while stillcheckinginputval:
                if not inputnum1 == "" : # if the meal price is being entered , then check the values entered
                    if "." in inputnum1: # if the meal price has a dot, we break the string into an array to check the 2 parts 
                        numlist = inputnum1.split('.')
                        if len(numlist)==2:
                            if not numlist[0].isdigit(): # first if we find the first part is not a digit , ask user to re-enter
                                print("Meal price is invalid") # let the user know they have entered an invalid meal price
                                inputnum1 = input("Enter your total meal price: ")
                                continue
                            elif not numlist[1].isdigit(): # if we find the second part is not a digit , ask user to re-enter
                                print("Meal price is invalid")
                                inputnum1 = input("Enter your total meal price: ")
                                continue
                            else: # all else would mean the 2 parts are digits 
                                amount1 = round(Decimal(inputnum1),2) # we have a good value
                                stillcheckinginputval=False
                                break  
                        else:
                            print("Meal price is invalid") #if there is more than a single dot, its not a numerical value
                            inputnum1 = input("Enter your total meal price: ")
                            continue
                                                 
                    else:
                        if inputnum1.isdigit(): # double checking when the value is whole before proceeding
                            amount1 = round(Decimal(inputnum1),2) #rounding being applied to the values for consistency
                            stillcheckinginputval=False
                            break
                        else:
                            print("Meal price is invalid")
                            inputnum1 = input("Enter your total meal price: ")
                            continue
                else:
                    print("Meal price can not be empty")
                    inputnum1 = input("Enter your total meal price: ")
                    continue

            print("Your total food price is: $"+str(amount1)) #displaying only food price
            plustip = round(amount1*tip,2)
            plustax = round(amount1*tax,2)
            print("Your total tip is: $"+str(plustip)) #displaying total tip based on percentage
            print("Your total tax is: $"+str(plustax)) #displaying total tax based on percentage
            total = round(amount1+plustip+plustax,2) #add all values and rounded 
            print("Your TOTAL is: $"+str(total)) #display the full total
            
            input("Press enter to continue...")
            mainprog()  # Unless user explicitly exits the program would return
    except Exception as e:
        print(f"An error occurred: {e} Exitting the program..")
        sys.exit() # Exit out from exception

if __name__ ==  '__main__': mainprog() #calling the main - mainprog to run

###############program end #################

