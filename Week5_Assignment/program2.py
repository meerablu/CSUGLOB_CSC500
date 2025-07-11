###############program start ###################################################
import sys # import basic sys library
import math # import basic math library
import calendar #import calendar library to prettify the dates
from datetime import datetime #import the date time library

current_month = datetime.now().month #gets the current month
current_month_name = calendar.month_name[current_month] # gets the name of current month

def userwishestoexit(): # function is used for capturing the user input q used for exiting the program 
    try:
        user_input = input("Press enter to continue or Type Q to quit! ")
        if user_input.upper() == 'Q': #input is case insensitive 
            print("Exiting program...Thank you!")
            sys.exit() # Exit gracefully
        else:
            return True # return to main for flow of execution
    except Exception as e:
        print(f"An error occurred within func-userwishestoexit(): {e}. Exiting program.") 
        
def requestnumericinput(verbiage,checktype): #this function accepts numeric inputs and performs basic validation
    try:        
        inputval1 = input(verbiage) #reusing the same input value function now appropriate to capture numeric inputs 
        checkinginputval = True
        while checkinginputval:
                if inputval1.isdigit():                   
                        return int(inputval1)                       
                else:
                     if checktype=="float": 
                        try: # ie. checking for that float input 
                            float(inputval1)
                            return float(inputval1)                           
                        except ValueError:
                            print(f"Sorry! You've entered {inputval1} which is not a number!") # letting user know they need to enter a valid digit
                            inputval1 = input(verbiage)     
                     else:
                        print(f"Sorry! You've entered {inputval1} which is not a number!") # letting user know they need to enter a valid digit
                        inputval1 = input(verbiage)   
        return inputval1
    except Exception as e:
        print(f"An error occurred within func-requestnumericinput(): {e}. Exiting program.") # using curly braces to print out the exception and remarking which function is erroring out

def printstudentrewards(): # main python program that prints how many points a student has accumulated
       
    try:
        print("Welcome to Python CSU Books and Rewards!!!!")
        whileuserunexited = userwishestoexit()

        while whileuserunexited:       
            print("****************************************************************************** ")
            print(f"This program will Print #Points accumulated based on #Books Purchased in {current_month_name.upper()} ")
            print("****************************************************************************** ")
            currentmonthpurchasedtotal = int(requestnumericinput("How many books have you purchased this month? ","numonly"))

            """ assuming book configuration changes all the time, and assuming first item is 0 which is fine but might still get points
                idea is to variabilize and dynamicitize this program instead of values being hard coded which will
                cause programs to be rewritten everytime the key values change - so the goal is book club can always decide and change their
                reward system configuration without having to rewrite this program.
            """
            bookclubconfigsize = len(bookpoints_config) #ensures there is config entries in the dictionary

            for bkey, bval in bookpoints_config.items():
                 #print(f"k is {bkey}")
                 #print(f"v is {bval}")
                 if bval>0:
                    minbp_wpoints=bkey #find the key which holds any value reward points - this is minimum book purchased with points yield
                    minibp_points=bval # capture its value
                    break #then we go ahead and break the for loop - we found those values already
            
            if bookclubconfigsize>0:
                maxbookp_wpoints = list(bookpoints_config.keys())[-1]
                maxbp_points = bookpoints_config.get(maxbookp_wpoints)
                #print(f"maxk is {maxbookp_wpoints}")
                #print(f"maxv is {maxbp_points}")
                #print(f"mink is { minbp_wpoints}")
                #print(f"minv is {minibp_points}")


                if currentmonthpurchasedtotal == 0: #when no books have been purchased yet
                        print("")
                        print(f"Sorry you haven't purchased any books yet. You will have to purchase at least {minbp_wpoints} books to get {minibp_points} points!")
                elif currentmonthpurchasedtotal < minbp_wpoints: # if lets say book purchased is only 1
                        print("")
                        howmanymore=minbp_wpoints-currentmonthpurchasedtotal
                        print(f"So if you have purchased only {currentmonthpurchasedtotal} book(s) this month - You need to purchase at least {howmanymore} more book(s) to get {minibp_points} points! ")             
                elif currentmonthpurchasedtotal >= minbp_wpoints: #when books purchased reaches at least min book with points yield
                    if currentmonthpurchasedtotal >= maxbookp_wpoints: #when its eq or greater than the max points yield
                        print("")
                        print(f"Congratulations! for purchasing {currentmonthpurchasedtotal} books this month. You have accumulated {maxbp_points} total points now! ")           
                    else:
                        print("")						
                        derivedfnum = currentmonthpurchasedtotal%2 #we use the mod value which will always be either 1 or 0 in this case to acquire the position of the key value
                        keyval=currentmonthpurchasedtotal-derivedfnum #position of the key value
                        print(f"So based on {currentmonthpurchasedtotal} books purchased - You have accumulated {bookpoints_config[keyval]} total points now! ")

                print("***************************THANK YOU!!!! HAVE A NICE DAY ****************** ")
                print("")
                         
            else:
               print("Book points system has not yet been setup")
               sys.exit()
                                 
            printstudentrewards()  #return to program
    except Exception as e:
        print(f"An error occurred within func-printstudentrewards(): {e}. Exiting program.")
        sys.exit() # Exit out from exception      


###############program main ###################################################
#initialized and defined book club reward points config
bookpoints_config = { 
  0: 0,
  2: 5,
  4: 15,
  6: 30,
  8: 60
}

if __name__ ==  '__main__': printstudentrewards() #calling main program execution

###############program end ###################################################

