#####################Easy Task Tracker Program##################
import sys
from datetime import datetime 

current_date = datetime.now().strftime("%m-%d-%Y") #gets the current date in pretty format -"January 1 2020"

def userwishestoexit(): # generic function defined to capture program exit Q
    try:
        user_input = input("Press enter to continue or Type Q to quit! ")
        if user_input.upper() == 'Q': # the user enters case insensitive q to quit
            print("Exiting program...Thank you!")
            sys.exit() # calling system.exit
        else:
            return True # program continues
    except Exception as e:
        print(f"An error occurred within func-userwishestoexit(): {e}. Exiting program.") # output the error message

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
                        print(f"Sorry! You've entered {inputval} which is Invalid!") # letting user know they need to enter a valid option 
                        inputval = input(verbiage).lower() #turning case selection insensitive

                elif checktype=="combination": #this user type specification allows digit or string
                        if inputval.isdigit():
                            return inputval  
                        else:
                            if inputval == 'q': # if the user enters a q or Q the program still ends
                                checkinginputval=False                           
                            else:
                                return inputval  
                elif checktype=="date": #this is amongst the input string prompts to ensure the date conforms to the format requirements
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
                                print(f"Sorry! {inputval} is Invalid! Enter a date in the format e.g., 12-13-2025") # prompting the user for the expected input format
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
            a - Add new task to list
            r - Remove task from list
            c - Change task details
            p - Output and print task list to file
            q - Quit
        Choose an option:
        """
        print(f"****** Task Registry available functions ***********")
        numtasksinlist = usertaskslist.get_num_tasks_in_list()       
        if numtasksinlist>0:
           print(f"=======>>>You have {numtasksinlist} Tasks in your Task Registry!") #get_num_tasks_in_list() for Flag headings
        else:
           print(f"You have no tasks!...") # Flag headings 

        print("a - to add new task ")
        print("r - to remove an old task because it is done ")
        print("c - to change details of a task")
        print("p - to Print and Output Task List! ")        
        print("q - to Quit ")
        print("*******************************************************************************")
        menuopt = requeststrinput("Choose an option:","menu")
        print("*******************************************************************************")
        match menuopt: 
            case "a":
                print(f"Menu {menuopt.upper()} - Add a Task")
                stilladding = True                     
                while stilladding:
                    itp = createTaskList()
                    usertaskslist.add_item(itp) 
                    useryesno = requeststrinput("Would you like to add another task? Y/N :",False)
                    if useryesno.lower() != 'y':
                        stilladding=False
                        break  # Exit the loop if the condition is met                                           
                print("Completed updating task list...")

            case "r":
                print(f"Menu {menuopt.upper()} - Remove task from list")                
                stillremoving = True               
                while stillremoving and usertaskslist.get_num_tasks_in_list()>0:
                    itp = processTaskItems(usertaskslist,"r") #calling this function passing in the usertaskslist object and setting the R flag for removals                   
                    while itp == None: #ITP is none if the user selected an Invalid option
                        itp = processTaskItems(usertaskslist,"r") #the second condition prompts for an alternate retry
                        continue 
                    else:
                        usertaskslist.remove_item(itp)
                        if usertaskslist.get_num_tasks_in_list()>0 :
                            useryesno = requeststrinput("Would you like to remove another task? Y/N :",False)
                            if useryesno.lower() != 'y':
                                stillremoving=False
                                break  # Exit the loop if the condition is met
                        else: 
                            stillremoving=False
                            break

            case "c":
                print(f"Menu {menuopt.upper()} - Change task items in list ")
                stillchanging = True
                     
                while stillchanging and usertaskslist.get_num_tasks_in_list()>0:
                    itp = processTaskItems(usertaskslist,"c") #calling this function passing in the usertaskslist object and setting the C flag for modifications
                    while itp == None: #ITP is none if the user selected an Invalid option
                        itp = processTaskItems(usertaskslist,"c")
                        continue 
                    else:
                        usertaskslist.modify_item(itp)
                        if usertaskslist.get_num_tasks_in_list()>0 :
                            useryesno = requeststrinput("Would you like to change another task? Y/N :",False)
                            if useryesno.lower() != 'y':
                                stillchanging=False
                                break  # breaking the loop
                        else: 
                            stillchanging=False
                            break

            case "p":
                print(f"Menu {menuopt.upper()} - Print current task descriptions ")
                usertaskslist.print_description()
            case _:
                # it should never reach this case for default        
                print_functions()
                
        print_functions()
    except Exception as e:
        print(f"An error occurred within func-print_functions(): {e}. Exiting program.") 
        sys.exit() 

def processTaskItems(TaskList,typecommand): #Defined function to help user pick which items they want to remove or modify from list, turned into 1 function
    try:
        if TaskList.get_num_tasks_in_list() == 0:
            print(f"Sorry! You do not have any tasks. ")
            return None
        else:
            print(f"You have {TaskList.get_num_tasks_in_list()} item(s) in your task list")

            itemchglist = {}
            for index, item in enumerate(TaskList.get_tasks_in_list()):
                print(f" Task#{(index+1)}: {item.task_name}") #prints the task list
                itemchglist.update({(index+1):item}) #using a dictionary to store the latest itp objects in the list
                
           
            if typecommand == "r":
                itprem = requeststrinput("Which task do you want to remove? Enter Task#: ","combination")

                if itprem.isdigit():
                    if int(itprem) in itemchglist:
                        itp = itemchglist.get(int(itprem))
                        print(f"Remove {itp.task_name} ... from List ...")
                        return itp
                    else:
                        print(f" Item#{itprem} NOT FOUND in list or is Invalid. ")
                else:
                    itpfound = False
                    for key, itpobj in itemchglist.items():
                        if itpobj.task_name == itprem:
                            itp = itemchglist.get(key)
                            itpfound=True                           
                            break                       
                    if itpfound == True:
                        print(f"Remove {itp.task_name} ... from List ...")                       
                        return itp
                    else:
                        print(f" Task#{itprem} NOT FOUND in list or is Invalid. ")
            else:
                itprem = requeststrinput("Which task do you want to modify? Enter TaskNo#: ","combination")

                if itprem.isdigit():
                    if int(itprem) in itemchglist:
                        itp = itemchglist.get(int(itprem))
                        print(f"Modify {itp.task_name} ... in List ...")
                        return itp
                    else:
                        print(f" Task#{itprem} NOT FOUND in list or is INVALID. ")
                else:
                    itpfound = False
                    for key, itpobj in itemchglist.items():
                        if itpobj.task_name == itprem:
                            itp = itemchglist.get(key)
                            itpfound=True                           
                            break                       
                    if itpfound == True:
                        print(f"Modify {itp.task_name} ... in List ...")                       
                        return itp
                    else:
                        print(f" Item#{itprem} NOT FOUND in list or is INVALID. ")
                    
    except Exception as e:
        print(f"An error occurred within func-processTaskItems(): {e}. Exiting program.")
        sys.exit() 

def createTaskList(): # Function for instantiation of the Task object 
    try:        
        taskname = requeststrinput("Enter the task name: ",False)
        taskdate = requeststrinput(f"Enter the target completion date for {taskname}: ","date")
        taskpriority = requeststrinput(f"Enter the priority [1-5 where 1 being highest] for {taskname}: #","combination")
        taskdescription = requeststrinput(f"Enter the description for the task: ",False)
        taskobj = TaskItem(taskname, taskdate, int(taskpriority),taskdescription) #create the task object
        
        return taskobj
    except Exception as e:
        print(f"An error occurred within func-createTaskList(): {e}. Exiting program.")
        sys.exit() 

def modifyTaskList(TaskItem): # Function for modifying the task object attributes
    try:        
        print(f" Let's change the task details for {TaskItem.task_name} ")
        
        taskpriority = requeststrinput(f"Change the priority for {TaskItem.task_name} was {int(TaskItem.task_priority)}: #","combination")
        taskdescription = requeststrinput(f"Change the Description of {TaskItem.task_name} was {TaskItem.task_description} :",False)

        TaskItem.task_priority=int(taskpriority)
        TaskItem.task_description=taskdescription
        
        print("Thanks! Your task "+TaskItem.task_name+" has been updated! ")
        return TaskItem
    except Exception as e:
        print(f"An error occurred within func-modifyTaskList(): {e}. Exiting program.") 
        sys.exit() 

##################### program main ##################################################

class TaskList: #Defines the new TaskList class
   
    def __init__(self, username, current_date, task_list): #constructor for class object with 3 attributes
        self.username = username
        self.current_date = current_date
        self.__task_list = task_list

    def add_item(self,TaskItem):
        #Adds an item to task_list list. 
        print("adding new task...")
        self.__task_list.append(TaskItem)
                            
    def remove_item(self,TaskItem):
        #Removes item from task_list list
        print("removing task item..")
        self.__task_list.remove(TaskItem)
                
    def modify_item(self,TaskItem):
        #Modifies the attributes of task "
        print("modifying task item...")
        upditp = modifyTaskList(TaskItem)
                           
    def get_num_tasks_in_list(self):
        #Returns total number of tasks
        return len(self.__task_list)

    def get_tasks_in_list(self):
        return self.__task_list
            
                  
    def print_description(self):
        #Prints each task and write them to date file        
        print(f"{self.username.upper()}'s Tasks- {self.current_date.upper()}")
        print("Task Registry")
        with open(f"{current_date}.txt", "w") as file: #using with open will automatically help us close the resource                       
            for itp in self.__task_list:
                print(f"{itp.task_name} : {itp.task_description} | Target Completion:{itp.task_completedby.upper()} | Priority:{itp.task_priority}")
                file.write(f"{itp.task_name} : {itp.task_description} | Target Completion:{itp.task_completedby.upper()} | Priority:{itp.task_priority}\n")
            
         

class TaskItem: #Task Item Object - class
  def __init__(self, task_name, task_completedby, task_priority, task_description): #constructor for class TaskItem with 4 attributes necessary for tracking tasks
    self.task_name = task_name
    self.task_completedby = task_completedby
    self.task_priority = task_priority
    self.task_description = task_description

print("*******************************************************************************")
print(f"!!Welcome to Easy Task Tracker!! Today is {current_date.upper()}!!!")

task_list = [] #defines a tasks list Array object
menuoptions = ["a","r","c","p","q"] #define valid menu options to work the task tracking program

username = requeststrinput(f"Please enter your Name: ",False)
usertaskslist = TaskList(username, current_date,task_list) #initialized the user task object 
      
if __name__ ==  '__main__': print_functions() #calling the main - mainprog to run

#####################program end ####################################
