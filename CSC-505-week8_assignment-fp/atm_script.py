############### ATM program start ###################################################
import sys # import basic sys library
import calendar #import calendar library to prettify the dates
import os # checks the file path to ensure the account exists
import time # wants to let user see the error message
from datetime import datetime #import the date time library
    
current_year = datetime.now().year #prints the current year
current_month = datetime.now().month #prints the current month
current_day = datetime.now().day # prints the current day
current_month_name = calendar.month_name[current_month] # prints current month name
    
def userwishestoexit(): # function is used for exiting the program 
    try:
        user_input = input("Press Enter to continue or Type Q to exit program! ")
        if user_input.upper() == 'Q': 
            print("Program will now exit...Thank you!")
            time.sleep(3) # Pauses for 3 seconds
            sys.exit() # Exit gracefully
        else:
            return True # return to main for flow of execution
    except Exception as e:
        print(f"An error occurred within func-userwishestoexit(): {e}. Exiting program.") 

def requeststrinput(verbiage,inputtype,retry): # generic function defined to capture string type inputs or prompts
    try:        
        if retry <3:
            checkinginputval = True
            inputval = input(verbiage) #actual verbiage is getting passed into the function for prompting the user        
        else:
            checkinginputval = False

        while checkinginputval:

            if inputtype == "":
                if inputval!="":                
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        return inputval # this is for user entering as long as non empty string 
                else:
                    print("Sorry! You have not entered anything yet. ") # user prompt for empty string
                    retry = retry+1
                    inputval = requeststrinput(f"{verbiage}","", retry)  
                    
            elif inputtype == "menuopt":
                if inputval!="":
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        if inputval.isdigit() and int(inputval) > 0 and int(inputval) < 5  :
                            return inputval 
                        else:
                            print("Sorry! Your entry is Invalid. ") # user prompt for empty string
                            retry = retry+1
                            inputval =requeststrinput(f"{verbiage}","menuopt", retry)  
                else:
                    print("Sorry! You have not entered any options. ") # user prompt for empty string
                    retry = retry+1
                    inputval =requeststrinput(f"{verbiage}","digit", retry)  
                   
            elif inputtype == "digit":
                if inputval!="":
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        if inputval.isdigit() and int(inputval) > 0:
                            return inputval 
                        else:
                            print("Sorry! Your entry is Invalid. ") # user prompt for empty string
                            retry = retry+1
                            inputval =requeststrinput(f"{verbiage}","digit", retry)  
                else:
                    print("Sorry! You have not entered any options. ") # user prompt for empty string
                    retry = retry+1
                    inputval =requeststrinput(f"{verbiage}","digit", retry)  
                    
            elif inputtype == "pin":
                if inputval!="":
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        if inputval.isdigit() and int(inputval) > 0 and len(inputval) == 4: #Pins are 4digit long
                            return inputval 
                        else:
                            print("Sorry! Your entry is Invalid! ") # user prompt for empty string
                            retry = retry+1
                            inputval =requeststrinput(f"{verbiage}","pin", retry)
                
        else:
            print(f"Cancelling and Exiting program...Thank you!")
            time.sleep(3) # Pauses for 3 seconds
            sys.exit() # calling system.exit                       
    except Exception as e:
        print(f"An error occurred within func-requeststrinput(): {e}. Exiting program.") 

def atm_menu(account,cardnumber):
    try:
       
        menuopt = requeststrinput(f" Enter [1] for Withdrawal| [2] for Deposits | [3] For Account Balance | Your selection = | [4] To Exit ","menuopt",0)   
        match menuopt:
            case "1":
                print("Process Withdrawal************************")
                amountwithdraw = requeststrinput("Please enter your $$amount to withdraw (Note: Only full amounts no Cents): ","digit", 0)
                if int(amountwithdraw) > int(account.accbalance):
                    print(f"Sorry you've exceeded the limit of the withdrawal!")
                elif int(amountwithdraw) == int(account.accbalance):
                    withdrawupdateaccount(account,amountwithdraw,cardnumber)
                    print(f"Success! ${amountwithdraw} has been withdrawn. Your account will be closed! Thank you!")
                    time.sleep(3) # Pauses for 3 seconds
                    sys.exit() # system exit
                else:
                    withdrawupdateaccount(account,amountwithdraw,cardnumber)
                    print(f"Success! ${amountwithdraw} has been withdrawn.")
          
            case "2":
                print("Process Deposit************************")
                amountdeposit = requeststrinput("Please enter the $$amount to deposit (Note: Only full amounts no Cents): ","digit", 0)
               
                depositupdateaccount(account,amountdeposit,cardnumber)
                print(f"Success! ${amountdeposit} has been deposited.")
          
            case "3":
                print("Print Balance************************")
                accountobj = load_accountinformation(cardnumber)
                print(f"Your Current Balance is: ${accountobj.accbalance}")
                print("Thank you!! ***********")
                
            case "4":
                print("Process Exit************************")
                print("Thank you!! Please Come Back another time!***********")
                time.sleep(3) # Pauses for 3 seconds
                sys.exit() # system exit
            case _:
                print(f"*******************************************")

        atm_menu(account,cardnumber)
    except Exception as e:
        print(f"An error occurred within func-atm_menu(): {e}. Exiting program.")
        sys.exit() # system exit

        
def atm_demo_proto(customer): # main python program    
    try:        
        whileuserunexited = userwishestoexit()
        """Renders the app continues           
            """
        while whileuserunexited:       
            if customer == "" : 
                cardnumber = requeststrinput("Please insert your account card number: ","digit", 0)  

                if check_ifaccountexists(cardnumber) == True:
                    accountobj = load_accountinformation(cardnumber)
                   
                    authenticate_user(accountobj,pinattempts)
                    authsuccess = accountobj.authstate
                    
                    if authsuccess == "True":
                        isactive = check_ifaccountisactive(accountobj)
                        if isactive == True:
                            print(f"*******************************************")
                            print(f"Welcome {accountobj.loginuser}! {current_day} {current_month_name.upper()}, {current_year}")
                            print(f"*******************************************")
                            atm_menu(accountobj,cardnumber)
                        else:
                            print(f"Your account is Inactive with $0 ! Exitting program.")
                            time.sleep(3) # Pauses for 3 seconds
                            sys.exit() # system exit                       
                    else:
                        print(f"Your authorization is denied! Exitting program.")
                        time.sleep(3) # Pauses for 3 seconds
                        sys.exit() # system exit
                else:
                    print(f"Your account is not found! Exitting program.")
                    time.sleep(3) # Pauses for 3 seconds
                    sys.exit() # system exit
                        
    except Exception as e:
        print(f"An error occurred within func-atm_demo_proto(): {e}. Exiting program.")
        time.sleep(3) # Pauses for 3 seconds
        sys.exit() # system exit


##################### program main ##################################################
pinattempts = 0

def check_ifaccountisactive(account):
    try:
        if int(account.accbalance) >0 :
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred within check_ifaccountexists(): {e}. Exiting program.")        
        
def authenticate_user(account,pinattempts):
    try:        
        if pinattempts<3:
            pinnumber = requeststrinput(f"Please enter your Pin: ","pin", pinattempts)
            if str(account.loginpass) == str(pinnumber):
                pinattempts=pinattempts
                account.authstate = "True"
                return True
            else:
                pinattempts = pinattempts+1
                pinnumber = authenticate_user(account,pinattempts)
        else:
            return False        
    except Exception as e:
        print(f"An error occurred within authenticate_user(): {e}. Exiting program.")        
      
      
def check_ifaccountexists(cardnumber):
    try:
        accountfile = "aci_"+cardnumber+".txt" 
        if os.path.isfile(accountfile):
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred within check_ifaccountexists(): {e}. Exiting program.")        
  
def load_accountinformation(cardnumber):
    try:
        accountfile = "aci_"+cardnumber+".txt" 
        with open(accountfile, "r") as file:
            contentline = file.readline()

        if len(contentline) != 0:
            rconst = contentline.split("|")
            if len(rconst) > 1:
                customerobj = account() 
                               
                customerobj.loginuser = rconst[0]
                customerobj.loginpass = rconst[1]                 
                customerobj.accbalance = rconst[2]
                                
                return customerobj                 
    except Exception as e:
        print(f"An error occurred within func1-load_accountinformation(): {e}. Exiting program.")        

def updateaccountfile(self, cardnumber, newbalance):
    try:               
        accountfile = "aci_"+cardnumber+".txt" 
        with open(accountfile, "r") as file:
            contentline = file.readline()

        if len(contentline) != 0:
            rconst = contentline.split("|")
            if len(rconst) > 1:
                customerobj = account() 
                               
                customerobj.loginuser = rconst[0]
                customerobj.loginpass = rconst[1]                 
                customerobj.accbalance = newbalance
                newcontentline =   customerobj.loginuser+"|"+customerobj.loginpass+"|"+str(customerobj.accbalance)               
                with open(accountfile, "w") as file:                    
                    file.write(newcontentline)

                return customerobj   
    except Exception as e:
        print(f"An error occurred within func1-updateaccountfile(): {e}. Exiting program.")
       
class account: #defines the account class
    def __init__(self, loginuser="", loginpass="",accbalance="", authstate=""):         
        self.loginuser = loginuser
        self.loginpass = loginpass
        self.authstate = authstate
        self.accbalance = accbalance       

def withdrawupdateaccount(self, amount, cardnumber):      
    try:
        balance =  self.accbalance
        newbalance = int(balance)-int(amount)
        self.accbalance = newbalance
        print(f"Your New balance is ${self.accbalance} ")       

        updatedcustomerobj = updateaccountfile(self, cardnumber, newbalance)

        return updatedcustomerobj
    
    except Exception as e:
        print(f"An error occurred within func1-load_withdrawupdateaccount(): {e}. Exiting program.")

def depositupdateaccount(self, amount, cardnumber):      
    try:
        balance =  self.accbalance
        newbalance = int(balance)+int(amount)
        self.accbalance = newbalance
        print(f"Your New balance is ${self.accbalance} ")       

        updatedcustomerobj = updateaccountfile(self, cardnumber, newbalance)

        return updatedcustomerobj
    
    except Exception as e:
        print(f"An error occurred within func1-load_depositupdateaccounwupdateaccount(): {e}. Exiting program.")


###############ATM program ###################################################
print(f"*******************************************")
print(f"WELCOME to Sample ATM: {current_day} {current_month_name.upper()}, {current_year}")
print(f"*******************************************")
if __name__ ==  '__main__': atm_demo_proto("")
############### ATM program end ###################################################

