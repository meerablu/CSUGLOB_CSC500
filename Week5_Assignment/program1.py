###############program start ###################################################
import sys # import basic sys library
import math # import basic math library
import calendar #import calendar library to prettify the dates
from datetime import datetime #import the date time library

    
current_year = datetime.now().year #gets the current year
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
                #if isinstance(int(inputval1), int) or isinstance(float(inputval1),float):
                if inputval1.isdigit():
                    if checktype=="year": # check type special logic placed to ensure the Year entry is valid
                         # logic is to disallow current year to be entered because we wouldnt make up for a full year unless it is already Dec
                         # considering the nested inner loop will have a fixed iteration to capture 12 months data
                         # also disallow any years that are older than 1900 which is not possible
                         if(current_month==12): #if it is already December then we allow collection for current year to be entered
                            if int(inputval1) >= 1900 and int(inputval1) <=current_year: #Year validation to ensure data entered is valid 
                                #print(f"{inputval1} is OK!") #this was my debug line only
                                return int(inputval1)
                               
                            else:
                                print(f"Sorry! You've entered {inputval1} which is Invalid!") # letting user know they need to enter a valid digit
                                inputval1 = input(verbiage)
                         else: 
                             if int(inputval1) >= 1900 and int(inputval1) <current_year: #Year validation to ensure data entered is valid 
                                #print(f"{inputval1} is OK!") #this was my debug line only
                                return int(inputval1)
                                
                             else:
                                print(f"Sorry! You've entered {inputval1} which is Invalid!") # letting user know they need to enter a valid digit
                                inputval1 = input(verbiage)                    
                    else: #else this is all good just needed to pass digit validation of either integer or float are accepted 
                        #print(f"{inputval1} is OK!") #this was my debug line only
                        return int(inputval1)
                        
                else:
                     if checktype=="float": 
                        try: # ie. checking for that float input 
                            float(inputval1)
                            #print(f"{inputval1} is OK!") #this was my debug line only
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

def collectyeardatafile(year):
    try:
        with open(f"{year}.txt", "w") as file: #using with open will automatically help us close the resource
            if(year == current_year and current_month != 12):
                for month in range(1,current_month+1):
                    monthw = calendar.month_name[month].upper()
                    inchrain = requestnumericinput(f"Enter Rain amount for {monthw} {year}: ","float")
                    file.write(f"{monthw}: {inchrain} \n")
            else: # OK to collect 12 months
                for month in range(1,13):
                    monthw = calendar.month_name[month].upper()
                    inchrain = requestnumericinput(f"Enter Rain amount for {monthw} {year}: ","float")
                    file.write(f"{monthw}: {inchrain} \n")
                
    except Exception as e:
        print(f"An error occurred within func-collectyeardatafile(): {e}. Exiting program.")
        sys.exit() # Exit out from exception

def readyeardatafile(fromyear,toyear):
    try:
        numbofmonths = 0
        totalrainfall = 0 
        for year in range(fromyear,toyear+1):
            with open(f"{year}.txt", "r") as file: #using with open will automatically help us close the resource
                lines = file.readlines()
                for line in lines:
                    numbofmonths=numbofmonths+1
                    rainfallvall  = float(line.split(":")[1].strip())
                    #print(f"rainfall {rainfallvall}")
                    totalrainfall =totalrainfall+rainfallvall
                    print(f"For {year}: {line}")

        avgrainfall = round(totalrainfall/numbofmonths,2)
        print(f"Total number of months = {numbofmonths} from {fromyear} to {toyear}")
        print(f"Total Rainfall = {totalrainfall} inches")
        print(f"Average Rainfall within period = {avgrainfall} inches") 
    except Exception as e:
        print(f"An error occurred within func-readyeardatafile((): {e}. Exiting program.")
        sys.exit() # Exit out from exception
        
def yearlyaveragerainfall(): # main python program that collects yearly rain data
       
    try:
        print("Welcome to Python Yearly Rainfall Data Collector and Reporter!")
        whileuserunexited = userwishestoexit()

        """Prepare the data collector - we will ask the user to input starting from which year
                and for how many years does the user want to enter data for and then for each year -
                we will write the data into a file with the year as its name to store the data               
            """
        while whileuserunexited:       
           
            print("This program will store information about rainfall using basic data entry and generate an Average Annual report.")
            print(f"Current Year :{current_year}  Month: {current_month_name.upper()}")
            startingyear = requestnumericinput("Please enter the Year to start: ","year")
            numofyears = requestnumericinput("How many years would you like to record? ","numonly")
            intyear = int(startingyear)
            lastyear = intyear
            print(f"You are about to enter the yearly data for {startingyear} for {numofyears} consecutive years! ")

            for yr in range(numofyears):
                
                yearis = intyear+yr
                if(yearis > current_year):
                    print(f"{yearis} is already in the future so we cutting off!")
                    break
                else:
                    print(f"Entering data for: {yearis}.....")
                    collectyeardatafile(yearis)
                    lastyear = yearis #reassigned the last year processed for data entry
                  
            print("Now we have finished entering data....")
            print(f"Lets read the data collected from {intyear} to {lastyear}")
            readyeardatafile(intyear,lastyear)

            yearlyaveragerainfall()  #return to program
    except Exception as e:
        print(f"An error occurred within func-yearlyaveragerainfall(): {e}. Exiting program.")
        sys.exit() # Exit out from exception

###############program main ###################################################

if __name__ ==  '__main__': yearlyaveragerainfall() #calling main program execution

###############program end ###################################################

