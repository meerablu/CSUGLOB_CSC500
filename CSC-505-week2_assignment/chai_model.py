#####################Easy Task Tracker Program##################
import sys
from datetime import datetime 

current_date = datetime.now().strftime("%m-%d-%Y") #gets the current date in regular format 

def requeststrinput(verbiage,checktype): # Function which is reusable for capturing user input 
    try:        
        inputval = input(verbiage).lower() #capturing the verbiage from the user and turning it case insensitive
        checkinginputval = True        

        while checkinginputval:
            if inputval!="":
                if checktype=="menu": #this is specially the print menu options which are going to be valid using Python membership
                    if inputval in menuoptions: #comparing the inputval from the array menu options defined
                        if inputval == 'q': # if the user enters a q or Q the program ends
                            checkinginputval=False                           
                        else:
                            return inputval  
                    else:
                        print(f"Sorry! You've entered an Invalid {inputval} menu option!") # letting user know they need to enter a valid option 
                        inputval = input(verbiage).lower() #turning case selection insensitive

                elif checktype=="string": #this user type specification allows string
                        if inputval == 'q': # if the user enters a q or Q the program still ends
                            checkinginputval=False                           
                        else:
                            return inputval
                elif checktype=="digit": #this user type specification allows number only to match datatype              
                        if inputval.isdigit():
                            return inputval  
                        else:
                            if inputval == 'q': # if the user enters a q or Q the program still ends
                                checkinginputval=False                                                       
                elif checktype=="date": #this is for inputting data conforms to the format requirements
                        if inputval == 'q': # if the user enters a q or Q the program ends
                            checkinginputval=False                           
                        elif inputval == 'd':
                            checkinginputval=False
                            return current_date
                        else:
                            try:
                                datetime.strptime(inputval, "%m-%d-%Y")
                                return inputval
                            except ValueError:
                                print(f"Sorry! {inputval} is Invalid! Enter a date in the format e.g., 12/13/2025") # prompting the user for the expected input format
                                inputval = input(verbiage).lower()               
                else:
                    if inputval == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        return inputval # this is for user entering as long as non empty string and is free to enter
            else:
                    print("Sorry! Nothing is entered. Please enter a value. ") # prompting the user to enter a value input
                    inputval = input(verbiage).lower()
        else:
            print("Program exits...Thank you!")
            sys.exit() # exiting the program
                       
    except Exception as e:
        print(f"An error occurred within func-requeststrinput(): {e}. Exiting program.") #prints the error mesage

def print_functions(): #Defines the task tracker program and functionalities 
    try:
        """MENU
            a - Define new process step to list
            r - Clear everything
            c - Change process step details
            p - Output and print Model
            q - Quit
        Choose an option:
        """
        print(f"****** Create your own SPDM models ***********")
        
        print("a - to define a new phase or process ")
        print("r - to remove process steps of start over")
        print("c - to change details of your phase or process")
        print("p - to Print and Output Your SPDM Model ")        
        print("q - to Quit ")
        print("*******************************************************************************")
        menuopt = requeststrinput("What would you like to do:","menu")
        print("*******************************************************************************")
        match menuopt: 
            case "a":
                print(f"Menu {menuopt.upper()} - Begin to add a phase or process")
                stilladding = True                     
                while stilladding:
                    itp = createProcessList()
                    userprocesslist.add_item(itp) 
                    useryesno = requeststrinput("Would you like to continue? Y/N :",False)
                    if useryesno.lower() != 'y':
                        stilladding=False
                        break                                  
                print("Completed updating process step...")

            case "r":
                print(f"Menu {menuopt.upper()} - Clearing all the items")                
                stillremoving = True               
                while stillremoving and userprocesslist.get_num_processes_in_list()>0:
                    itp = processPItems(userprocesslist ,"r") #calling this function passing in the processmodel_list object and setting the R flag for removals                   
                    while itp == None: 
                        itp = processPItems(userprocesslist,"r") #prompts for an alternate retry
                        continue 
                    else:
                        userprocesslist.remove_item(itp)
                        if userprocesslist.get_num_processes_in_list()>0 :
                            #remove everything
                            stillremoving=True
                        else: 
                            stillremoving=False
                            break

            case "c":
                print(f"Menu {menuopt.upper()} - Change phase or process ")
                stillchanging = True
                     
                while stillchanging and userprocesslist.get_num_processes_in_list()>0:
                    itp = processPItems(userprocesslist,"c") #calling this function passing in the processmodel_list object and setting the C flag for modifications
                    while itp == None: 
                        itp = processPItems(userprocesslist,"c")
                        continue 
                    else:
                        userprocesslist.modify_item(itp)
                        if userprocesslist.get_num_processes_in_list()>0 :
                            useryesno = requeststrinput("Would you like to change another step? Y/N :",False)
                            if useryesno.lower() != 'y':
                                stillchanging=False
                                break  # breaking the loop
                        else: 
                            stillchanging=False
                            break

            case "p":
                print(f"Menu {menuopt.upper()} - Print current process model ")
                userprocesslist.print_description()
            case _:
                # it should never reach this case for default        
                print_functions()
                
        print_functions()
    except Exception as e:
        print(f"An error occurred within func-print_functions(): {e}. Exiting program.") 
        sys.exit() 

def processPItems(ProcessList,typecommand): #Defined function to help user pick which items they want to remove or modify from list, turned into 1 function
    try:
        if ProcessList.get_num_processes_in_list() == 0:
            print(f"Nothing defined! ")
            return None
        else:
            print(f"You have {ProcessList.get_num_processes_in_list()} item(s) ")

            itemchglist = {}
            for index, item in enumerate(ProcessList.get_processes_in_list()):
                print(f" Task#{(index+1)}: {item.process_name}") #prints the task list
                itemchglist.update({(index+1):item}) #using a dictionary to store the latest itp objects in the list
                
           
            if typecommand == "r":
                itprem = requeststrinput("Which task do you want to remove? Enter Task#: ","string")

                if itprem.isdigit():
                    if int(itprem) in itemchglist:
                        itp = itemchglist.get(int(itprem))
                        print(f"Remove {itp.process_name} ... from List ...")
                        return itp
                    else:
                        print(f" Item#{itprem} NOT FOUND in list or is Invalid. ")
                else:
                    itpfound = False
                    for key, itpobj in itemchglist.items():
                        if itpobj.process_name == itprem:
                            itp = itemchglist.get(key)
                            itpfound=True                           
                            break                       
                    if itpfound == True:
                        print(f"Remove {itp.process_name} ... from List ...")                       
                        return itp
                    else:
                        print(f" Process#{itprem} NOT FOUND in list or is Invalid. ")
            else:
                itprem = requeststrinput("Which atep do you want to modify? Enter StepNo#: ","string")

                if itprem.isdigit():
                    if int(itprem) in itemchglist:
                        itp = itemchglist.get(int(itprem))
                        print(f"Modify {itp.process_name} ... in List ...")
                        return itp
                    else:
                        print(f" Step#{itprem} NOT FOUND in list or is INVALID. ")
                else:
                    itpfound = False
                    for key, itpobj in itemchglist.items():
                        if itpobj.process_name == itprem:
                            itp = itemchglist.get(key)
                            itpfound=True                           
                            break                       
                    if itpfound == True:
                        print(f"Modify {itp.process_name} ... in List ...")                       
                        return itp
                    else:
                        print(f" Item#{itprem} NOT FOUND in list or is INVALID. ")
                    
    except Exception as e:
        print(f"An error occurred within func-processPItems(): {e}. Exiting program.")
        sys.exit() 

def createProcessList(): # Function for instantiation of the Process object 
    try:        
        processname = requeststrinput("Enter the process step name: ",False)
        processnumber = requeststrinput(f"Enter the process number for {processname} e.g. 1-9: #","digit")
        processdirection = requeststrinput(f"Enter the direction for {processname} e.g. TO|BACK|FLOW: #","string")
        processdescription = requeststrinput(f"Enter the description for this process: ",False)
        processobj = PItem(processname, processdirection,processnumber,processdescription) #create the object
        
        return processobj
    except Exception as e:
        print(f"An error occurred within func-createProcessList(): {e}. Exiting program.")
        sys.exit() 

def modifyProcessList(PItem): # Function for modifying the task object attributes
    try:        
        print(f" Changing the details for {PItem.process_name} ")

        processnumber = requeststrinput(f"Change the process number for {PItem.process_name} was {int(PItem.process_number)}: #","digit")
      
        processdirection = requeststrinput(f"Change the direction for {PItem.process_name} was {PItem.process_direction}: ","string")
        processdescription = requeststrinput(f"Change the Description of {PItem.process_name} was {PItem.process_description} :",False)

        PItem.process_number=int(processnumber)
        PItem.process_direction=processdirection
        PItem.process_description=processdescription
        
        print("Thanks! ["+PItem.process_name+"] has been updated! ")
        return PItem
    except Exception as e:
        print(f"An error occurred within func-modifyProcessList(): {e}. Exiting program.") 
        sys.exit() 

##################### program main ##################################################

class PModel: #Defines the new PMModel class
   
    def __init__(self, lastname, current_date, processmodel_list): #constructor for class object with 3 attributes
        self.lastname = lastname
        self.current_date = current_date
        self.processmodel_list = processmodel_list

    def add_item(self,PItem):
        #Adds an item to processmodel_list 
        print("adding new process item...")
        self.processmodel_list.append(PItem)
                            
    def remove_item(self,PItem):
        #Removes all items from processmodel_list
        print("clearing the model..")
        self.processmodel_list.remove(PItem)
                
    def modify_item(self,PItem):
        #Modifies the attributes of the step"
        print("modifying task item...")
        upditp = modifyProcessList(PItem)
                           
    def get_num_processes_in_list(self):
        #Returns total number processes
        return len(self.processmodel_list)

    def get_processes_in_list(self):
        return self.processmodel_list
            
                  
    def print_description(self):
        #Prints each process phase and write them to date file        
        print(f"{self.lastname.upper()}'s Adaptive Model- {self.current_date.upper()}")
        with open(f"chai_adaptivemodel_{current_date}.txt", "w") as file: #using with open will automatically help us close the resource                       
            for itp in self.processmodel_list:
                if itp.process_direction.upper() == "TO":
                        print(f"{itp.process_number}:{itp.process_name} | {itp.process_description} | {itp.process_direction} ==>")
                        file.write(f"{itp.process_number}:{itp.process_name} | {itp.process_description} \n")
                        file.write(f"      | \n")
                        file.write(f"      V \n")
                elif itp.process_direction.upper() == "FLOW":
                        print(f"{itp.process_number}:{itp.process_name} | {itp.process_description} | {itp.process_direction} <==>")
                        file.write(f"{itp.process_number}:{itp.process_name} | {itp.process_description} \n")
                        file.write(f"      A \n")
                        file.write(f"      V \n")
                elif itp.process_direction.upper() == "BACK":
                        print(f"{itp.process_number}:{itp.process_name} | {itp.process_description} | {itp.process_direction} <==")
                        file.write(f"{itp.process_number}:{itp.process_name} | {itp.process_description}  \n")
                        file.write(f"      A \n")
                        file.write(f"      ] \n")     
                
            
         

class PItem: #Process Item Object - class
  def __init__(self, process_name, process_direction, process_number, process_description): #constructor for class 3 attributes necessary for generating an adaptive model
    self.process_name = process_name
    self.process_number = process_number
    self.process_direction = process_direction
    self.process_description = process_description

print("*******************************************************************************")
print(f"!!Welcome to Easy SPDM Modeler!! Today is {current_date.upper()}!!!")

processmodel_list = [] #defines a process list Array object
menuoptions = ["a","r","c","p","q"] #define valid menu options to work the modeler application

lastname = requeststrinput(f"Please enter your last name: ",False)
userprocesslist = PModel(lastname, current_date,processmodel_list) #initialized the user process object 
      
if __name__ ==  '__main__': print_functions() #calling the main - mainprog to run

#####################program end ####################################
