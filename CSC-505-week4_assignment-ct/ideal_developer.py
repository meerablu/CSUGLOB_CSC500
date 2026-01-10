############### my ideal developer program start ###################################################
import sys # import basic sys library
import calendar #import calendar library to prettify the dates
from datetime import datetime #import the date time library
    
current_year = datetime.now().year #prints the current year
current_month = datetime.now().month #prints the current month
current_month_name = calendar.month_name[current_month] # prints current month name
    
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

def requeststrinput(verbiage): # generic function defined to capture string type inputs or prompts
    try:        
        inputval = input(verbiage) #actual verbiage is getting passed into the function for prompting the user
        checkinginputval = True        

        while checkinginputval:
            if inputval!="":                
                if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                    checkinginputval=False                           
                else:
                    return inputval # this is for user entering as long as non empty string 
            else:
                print("Sorry! You have not entered anything yet. ") # user prompt for empty string
                inputval = input(verbiage)
        else:
            print(f"Exiting program...Thank you!")
            sys.exit() # calling system.exit                       
    except Exception as e:
        print(f"An error occurred within func-requeststrinput(): {e}. Exiting program.") 

        
def generate_ideal_developer(idealDeveloper): # main python program that accepts input from the creative user       
    try:        
        whileuserunexited = userwishestoexit()
        """Renders the app continues           
            """
        while whileuserunexited:       

            idealDeveloper.developer_name="" #reset the class objects idealDeveloper
            idealDeveloper.developer_role=""
            idealDeveloper.gender=""
            
            personalitydict.clear()  #reset the class object perseonalitytraits

            print(f"Let's discover my ideal developer's 3-Most important personality traits !!!")
            print(f"*******************************************")
            
            if idealDeveloper.developer_name == "": 

                devname = requeststrinput("Please enter your ideal developer's name: ")                
                idealDeveloper.developer_name=devname

                devgen = requeststrinput(f"Is {devname.upper()} Male or Female? ")
                idealDeveloper.gender=devgen
                    
                devrole = requeststrinput("Please enter your ideal developer's job role: ")
                idealDeveloper.developer_role=devrole

                idealDeveloper.gettotalpersonalitytraits() # Prints the total before we added them

                for i in range(3): #adds up to 3 personality trait
                    index = i+1
                    inputstrtrait = requeststrinput(f"Enter {devname.upper()}'s personality trait #{index}: ")
                    inputstrtdescription = requeststrinput(f"Enter the description for ({inputstrtrait.upper()}): ")
              
                    mydevelopertraitsObj = idealDeveloperPersonalitytraits()

                    mydevelopertraitsObj.personality_trait= inputstrtrait
                    mydevelopertraitsObj.personality_description= inputstrtdescription
                    add_personalitydict = {mydevelopertraitsObj.personality_trait: mydevelopertraitsObj.personality_description}
                    personalitydict.update(add_personalitydict)


                idealDeveloper.print_myidealdeveloper()
                idealDeveloper.gettotalpersonalitytraits()
                idealDeveloper.printpersonalitytraits()

            generate_ideal_developer(idealDeveloper)  #return to program
    except Exception as e:
        print(f"An error occurred within func-generate_ideal_developer(): {e}. Exiting program.")
        sys.exit() # system exit


##################### program main ##################################################

personalitydict = {} #defines a personality traits dictionary

class idealDeveloperPersonalitytraits: #defines the idealdevelopers' personality traits
    def __init__(self, personality_trait="", personality_description=""): 
        self.personality_trait = personality_trait
        self.personality_description = personality_description

    def addpersonalitytraittodict(self):
        personalitytrait = self.personality_trait            
        personalitydescription = self.personality_description

class idealDeveloper: #defines the idealdeveloper class
    def __init__(self, developer_name="", gender="", developer_role="", personalitydict = {} ): 
        
        self.developer_name = developer_name
        self.developer_role = developer_role
        self.gender = gender

        self.personalitydict = personalitydict 

    def gettotalpersonalitytraits(self):
        print(f"************************************")
        total_traits = len(personalitydict)
        print(f"Total personality traits [{self.developer_name.upper()}] = {total_traits} ")
        print(f"************************************")

    def printpersonalitytraits(self):
        print(f"************************************")
        index = 0
        total_traits = len(personalitydict)
        for key, value in personalitydict.items():
            index += 1
            print(f" Trait#{index} : {key} - {value}. ")
            
    def print_myidealdeveloper(self): #class method
        devname= self.developer_name.upper()
        devrole = self.developer_role.upper()
        devgender = self.gender.upper()
        if devgender == "M" or devgender == "MALE":       
            genderp = "His"
        else:        
            genderp = "Her"

        print(f"************************************")
        print(f"My Ideal Developer is: {devname}")
        print(f"{genderp} job role is : {devrole}")      
        
mydeveloperObj = idealDeveloper()    #initialized the developer object using the defaults
###############IDEAL Developer program ###################################################
print(f"WELCOME- Discovering your Ideal Software Developer!!! - {current_month_name.upper()}/{current_year}")
if __name__ ==  '__main__': generate_ideal_developer(mydeveloperObj) #calling main program execution
###############IDEAL Developer program end ###################################################

