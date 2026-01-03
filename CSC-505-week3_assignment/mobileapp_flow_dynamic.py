###############mobile app skeleton program start ###################################################
import sys # import basic sys library
from bs4 import BeautifulSoup #import the html simple file renderer - dependency non native library
import webbrowser #open the app as a web page on a web browser
import os # needed to retrieve the local file system
import calendar #import calendar library for dates
import time #for simulated wait time
from datetime import datetime #import the date time library
    
curnt_year = datetime.now().year #gets the current year
curnt_month = datetime.now().month #gets the current month
curnt_month_name = calendar.month_name[curnt_month] # gets the name of current month

def userwishestoexit(): # function is used for exiting the program 
    try:
        user_input = input("Press Enter to continue or Type Q to exit program! ")
        if user_input.upper() == 'Q': 
            print("Program will now exit...Thank you!")
            sys.exit() # Exit gracefully
        else:
            return True # return to main for flow of execution
    except Exception as e:
        print(f"An error occurred within func-userwishestoexit(): {e}. Exiting program.") 
        
def requestdemomode(verbiage): #this function accepts the demo mode requested by the user 1 or 2
    try:        
        inputval1 = input(verbiage) 
        checkinginputval = True
        while checkinginputval:
                if inputval1.isdigit():                    
                    if int(inputval1) > 0 and int(inputval1) <=2: #only 2 modes are valid                            
                        return int(inputval1)
                    else:
                       print(f"Sorry! {inputval1} is invalid!") # entered invalid screen number
                       inputval1 = input(verbiage)                         
                else:
                     print(f"Sorry! {inputval1} is invalid!")
                     inputval1 = input(verbiage)                     
        return inputval1
    except Exception as e:
        print(f"An error occurred within func-requestdemomode(): {e}. Exiting program.") # using curly braces f notation to print out the exception

def validatelinkedpages(inputval, fromscr): #this function accepts numeric inputs and performs basic validation
    try:
        match inputval:
                case "add pet":                       
                    if fromscr == 2 or fromscr ==4 :
                        return 3
                    else:
                        print("Invalid page flow")
                        return fromscr
                case "update pet":                       
                    if fromscr ==4 :
                        return 7
                    else:
                        print("Invalid page flow")
                        return fromscr
                case "add appointment":                       
                    if fromscr == 2 or fromscr ==4 :
                        return 10
                    else:
                        print("Invalid page flow")
                        return fromscr
                case "add regimen":                       
                    if fromscr == 2 or fromscr ==4 :
                        return 9
                    else:
                        print("Invalid page flow")
                        return fromscr
                case "pet journals":                       
                    if fromscr == 2 :
                        return 5
                    else:
                        print("Invalid page flow")
                        return fromscr
                case "write pet journal":                       
                    if fromscr == 5 :
                        return 6
                    else:
                        print("Invalid page flow")
                        return fromscr
                case "home":                       
                    if fromscr == 5 or fromscr ==4 or fromscr ==8 or fromscr ==7:
                        return 2
                    else:
                        print("Invalid page flow")
                        return fromscr
                case "settings":                       
                    if fromscr == 2:
                        return 8
                    else:
                        print("Invalid page flow")
                        return fromscr
                case "logout":                       
                    if fromscr == 2 or fromscr ==8:
                        return 1
                    else:
                        print("Invalid page flow")
                        return fromscr
                case _:
                    return False
    except Exception as e:
        print(f"An error occurred within func-requestdemomode(): {e}. Exiting program.") # using curly braces to print out the exception
        
def renderprocscreenpage(screennum):
    try:        

        with open(f"frame{screennum}.txt", "r") as file: #using with open will automatically help us close the resource
        
            lines = file.readlines()
            for line in lines:
                print(f"{line}")

            match screennum:
                    case 1:                       
                       inputstr1 = input("Enter your username: ")
                       inputstr2 = input("Enter your password: ")
                       if authenticateusers(inputstr1, inputstr2):
                            return True
                       else:
                            return False                       
                    case 2:
                       inputstr1 = input("[Simulate Next Page], type options - 'add pet' or 'pet journals' or 'add regimen' or 'add appointment' or 'settings' or 'logout': ")                       
                       gotoscreen = validatelinkedpages(inputstr1, screennum)
                       if gotoscreen != False:
                            return gotoscreen
                       else:
                            return screennum
                    case 3:
                           time.sleep(2) #wait a bit as if clicking
                           return 2 #return home only
                           #return True
                    case 4:
                       inputstr1 = input("[Simulate Next Page], type options - 'add pet' or 'update pet' or 'add appointment' or 'add regimen' or 'home': ")                       
                       gotoscreen = validatelinkedpages(inputstr1, screennum)
                       if gotoscreen != False:
                            return gotoscreen
                       else:
                            return screennum
                    case 5:
                       inputstr1 = input("[Simulate Next Page], type options - 'write pet journal' or 'home' : ")                       
                       gotoscreen = validatelinkedpages(inputstr1, screennum)                      
                       if gotoscreen != False:
                            return gotoscreen
                       else:
                            return screennum
                    case 6:
                           time.sleep(3) #wait a bit as if clicking
                           return 5 #return journal page
                    case 7:
                        inputstr1 = input("[Simulate Next Page], type options - 'home': ")                       
                        gotoscreen = validatelinkedpages(inputstr1, screennum)                       
                        if gotoscreen != False:
                            return gotoscreen
                        else:
                            return screennum
                    case 8:
                        inputstr1 = input("[Simulate Next Page], type options - 'logout' or 'home': ")                       
                        gotoscreen = validatelinkedpages(inputstr1, screennum)                       
                        if gotoscreen != False:
                            return gotoscreen
                        else:
                            return screennum
                    case 9:
                           time.sleep(2) #wait a bit as if clicking
                           return 4 #return page 4 listing
                    case 10:
                           time.sleep(3) #wait a bit as if clicking
                           return 4 #return page 4 listing
                    case _:
                        return False                   
    except Exception as e:
        print(f"An error occurred within renderprocscreenpage(): {e}. Exiting program.")
        sys.exit() # Exit out from exception

def renderscreenpage(screennum):
    try:        

        with open(f"frame{screennum}.html", "r", encoding="utf-8") as f:
            htmlpage = f.read()
            appframe = BeautifulSoup(htmlpage, 'html.parser')
            file_path = os.path.abspath(f"frame{screennum}.html")
            webbrowser.open(f"file://{file_path}")
           
            match screennum:
                    case 1:                       
                       
                       inputform1 = appframe.find('input', id='username')
                       inputform2 = appframe.find('input', id='password')
                       if inputform1:
                        inputstr1 = inputform1.get('value')
                        print(f"Username value: {inputstr1}")
                       if inputform2:
                        inputstr2 = inputform2.get('value')

                       if authenticateusers(inputstr1, inputstr2):
                            time.sleep(2) #wait a bit as if clicking
                            return True
                       else:
                            return False                       
                    case 2:
                           time.sleep(3) #wait a bit as if clicking
                           return True
                    case 3:
                           time.sleep(2) #wait a bit as if clicking
                           return True
                    case 4:
                           time.sleep(4) #wait a bit as if clicking
                           return True
                    case 5:
                           time.sleep(2) #wait a bit as if clicking
                           return True
                    case 6:
                           time.sleep(3) #wait a bit as if clicking
                           return True
                    case 7:
                           time.sleep(2) #wait a bit as if clicking
                           return True
                    case 8:
                           time.sleep(3) #wait a bit as if clicking
                           return True
                    case 9:
                           time.sleep(2) #wait a bit as if clicking
                           return True
                    case 10:
                           time.sleep(3) #wait a bit as if clicking
                           return True
                    case _:
                        return False                   
    except Exception as e:
        print(f"An error occurred within renderscreenpage(): {e}. Exiting program.")
        sys.exit() # Exit out from exception

def authenticateusers(user, passw):
    try:        
        with open(f"users.txt", "r") as file: #using with open will automatically help us close the resource
            lines = file.readlines()
            for line in lines:                  
                print(f"Logging in as {user}...")
                if(line.split("|")[0]==user) and (line.split("|")[1]==passw):
                    return True
                else:
                    print(f"Invalid username or password!!")                   
    except Exception as e:
        print(f"An error occurred within authenticateusers((): {e}. Exiting program.")
        sys.exit() # Exit out from exception
        
def loopscreenflow(nextscreen):
    try:
        print(f"Rendering in Screen{nextscreen}******")
        whilescreenhasnext = True
        if nextscreen == 1 or nextscreen == "None":
            gonext =renderprocscreenpage(1)
            whilescreenhasnext = False
        """Renders the next screen          
            """
        while whilescreenhasnext:
            gonext =renderprocscreenpage(nextscreen)
            loopscreenflow(gonext)
            
    except Exception as e:
        print(f"An error occurred within func-loopscreenflow(): {e}. Exiting program.")
        sys.exit() # Exit out from exception


def mobileapp_skeletonflow(): # main python program that accepts a menu target screen number and presents the reference screen       
    try:        
        whileuserunexited = userwishestoexit()
        """Renders the mobile app frame by reference number            
            """
        while whileuserunexited:       
           
            print("Welcome to Habbi Pets - This mobile app will help you manage your Pet(s).")          

            demomode = requestdemomode("Enter [1 for Text mode] demo, Enter [2 for HTML slide] demo: ")
            if demomode ==1: # menu option interactions flow 
                authsuc = renderprocscreenpage(1)
               
                if authsuc:
                    nextscreen = renderprocscreenpage(2)
                    loopscreenflow(nextscreen)                   
                else:
                    renderprocscreenpage(1)
            else: #HTML renderer flow
                authsuc = renderscreenpage(1)              
                if authsuc:
                    renderscreenpage(2)
                    renderscreenpage(3)
                    renderscreenpage(4)
                    renderscreenpage(7)
                    renderscreenpage(5)
                    renderscreenpage(6)
                    renderscreenpage(10)
                    renderscreenpage(9)
                    renderscreenpage(8)
                    renderscreenpage(1)
                else:
                    renderscreenpage(1)

            mobileapp_skeletonflow()  #return to program
    except Exception as e:
        print(f"An error occurred within func-mobileapp_skeletonflow(): {e}. Exiting program.")
        sys.exit() # Exit out from exception

###############MOBILE APP SKELETONS program main ###################################################
print(f"WELCOME to Happy Pets mobile app's skeleton! - {curnt_month_name.upper()}/{curnt_year}")
print(f"Total number of screens = 10")
 
if __name__ ==  '__main__': mobileapp_skeletonflow() #calling main program execution
###############MOBILE APP SKELETONS program end ###################################################

