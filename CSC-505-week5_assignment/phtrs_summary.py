############### PHTRS program start ###################################################
import sys # import basic sys library
import calendar #import calendar library to prettify the dates
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
            sys.exit() # Exit gracefully
        else:
            return True # return to main for flow of execution
    except Exception as e:
        print(f"An error occurred within func-userwishestoexit(): {e}. Exiting program.") 

def requeststrinput(verbiage,inputtype): # generic function defined to capture string type inputs or prompts
    try:        
        inputval = input(verbiage) #actual verbiage is getting passed into the function for prompting the user
        checkinginputval = True        

        while checkinginputval:

            if inputtype == "":
                if inputval!="":                
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        return inputval # this is for user entering as long as non empty string 
                else:
                    print("Sorry! You have not entered anything yet. ") # user prompt for empty string
                    inputval = input(verbiage)
            elif inputtype == "menuopt":
                if inputval!="":
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        if inputval.isdigit() and int(inputval) <4 and int(inputval) > 0:
                            return int(inputval)
                else:
                    print("Sorry! You have not entered any options. ") # user prompt for empty string
                    inputval = input(verbiage)
        else:
            print(f"Exiting program...Thank you!")
            sys.exit() # calling system.exit                       
    except Exception as e:
        print(f"An error occurred within func-requeststrinput(): {e}. Exiting program.") 


def phtrs_actorsession(actortype, pothole, person_name):
    try:
        if actortype == 1: #actor - the citizen

                citizenwantstodo = requeststrinput(f" Enter [1] Report Pothole | [2] Repair status | [3] File a Claim | [4] Claim status | Your selection = ","menuopt")   
                if citizenwantstodo == 1:             
                                                      
                    pothole.reporter_name=person_name #same session won't require the person to re-enter name every time

                    ph_size = requeststrinput("Please enter size of the pothole from scale of 1-10: ","")                
                    pothole.ph_size=ph_size

                    ph_location = requeststrinput("Please enter location of pothole e.g., 'middle of road', 'curb', etc.: ","")                
                    pothole.ph_location=ph_location

                    ph_address = requeststrinput("Please enter your address - street name and zip code: ","")                
                    pothole.ph_address=ph_address

                    ph_severity = requeststrinput("Please state the severity of the pothole e.g., 'urgent' or 'can wait', etc.: ","")                
                    pothole.ph_severity=ph_severity

                    pothole.datereported = f"{current_day}-{current_month_name}-{current_year}"

                    totphrequests =gettotalph_requests()
                    phindticketnum = totphrequests+1
                                               
                    addpotholetodict(pothole, phindticketnum)

                    yourticketnum = f"TNo:"+str(phindticketnum)
                    totphrequests =gettotalph_requests()

                    print(f"Please keep your Ticket# [ {yourticketnum} ]")
                    print(f"Total pothole service requests in queue = {totphrequests} ")                        
                    print(f"Thank you for reporting a pothole!!")
                        
                elif citizenwantstodo == 2:
                       loadph_serviceregistry()
      
                       ticketnumber = requeststrinput("Please enter your ticket number (Enter 99 example for TNo:99): ","")
                       retrievestatusofpotholerepair(ticketnumber,"fixstatus")

                elif citizenwantstodo == 3:
                       print(f"***********Helping your raise a damage claim")
                       print(f"***********Apologies - this has not been implemented yet.")
                elif citizenwantstodo == 4:
                       print(f"***********Helping your retrieve claim status")
                       print(f"***********Apologies - this has not been implemented yet.")
                                                 
        elif actortype == 2: #actor public works admin 
                print("*****************************************")
                print(f"Welcome to the PHTRS - Public works Admin system!")
                loadph_serviceregistry() #read the registry
                totphrequests =gettotalph_requests()
                adminwantstodo = requeststrinput(f" Enter [1] Assign repair crew | [2] Mark repair status | [3] Resolve a Claim | [4] Update claim | Your selection = ","menuopt")   
                if adminwantstodo == 1:             
                    
                    if totphrequests > 0 :
                        printlistofpotholes(pothole)
                        ticketnumber = requeststrinput("Please enter your ticket number (Enter 99 example for TNo:99): ","")
                        retrievestatusofpotholerepair(ticketnumber,"assignjoborder")
                        print(f"Thank you for working this request !!")
                    else:
                        print(f"***********There are no pending tickets at the moment.")
                                            
                elif adminwantstodo == 2:
                    print(f"Total pothole service requests in queue = {totphrequests} ")                        
                   
                    ticketnumber = requeststrinput("Please enter your ticket number (Enter 99 example for TNo:99): ","")
                    retrievestatusofpotholerepair(ticketnumber,"updaterepairstatus")
                    print(f"Thank you for working this request !!")

                elif adminwantstodo == 3:
                       print(f"***********Helping your raise a damage claim")
                       print(f"***********Apologies - this has not been implemented yet.")
                elif adminwantstodo == 4:
                       print(f"***********Helping your retrieve claim status")
                       print(f"***********Apologies - this has not been implemented yet.")
                       
        elif actortype == 3: # actor public works contractor 
                print("*****************************************")
                print(f"Welcome to the PHTRS - Public works Contractor system!")
                loadph_serviceregistry() #read the registry
                totphrequests =gettotalph_requests()
                contractorwantstodo = requeststrinput(f" Enter [1] Review job orders | [2] Assign a crew | [3] Mark repair status | Your selection = ","menuopt")   
                if contractorwantstodo == 1:             
                    
                    if totphrequests > 0 :
                        printlistofpotholes(pothole)
                        #ticketnumber = requeststrinput("Please enter your ticket number (Enter 99 example for TNo:99): ","")
                        #retrievestatusofpotholerepair(ticketnumber,"assignjoborder")
                        #print(f"Thank you for working this request !!"
                    else:
                        print(f"***********There is nothing at the moment!")
                                            
                elif contractorwantstodo == 2:
                    print(f"Total pothole service requests in queue = {totphrequests} ")                        
                   
                    ticketnumber = requeststrinput("Please enter your ticket number (Enter 99 example for TNo:99): ","")
                    retrievestatusofpotholerepair(ticketnumber,"assigncrew")
                    print(f"Thank you for taking this request !!")

                elif contractorwantstodo == 3:
                    ticketnumber = requeststrinput("Please enter your ticket number (Enter 99 example for TNo:99): ","")
                    retrievestatusofpotholerepair(ticketnumber,"resolveit")
                    print(f"Thank you for completing this repair !!")
                

    except Exception as e:
        print(f"An error occurred within func-phtrs_actorsession(): {e}. Exiting program.") 

        
def phtrs_demo_proto(actortype,personname): # main python program that accepts input from the citizen     
    try:        
        whileuserunexited = userwishestoexit()
        """Renders the app continues           
            """
        while whileuserunexited:       
            if personname == "" : 
                personname = requeststrinput("Please enter your name: ","")  

            newpotholeobj = pothole() #new pothole for request loop

            if actortype == 0:
                print(f"This is a New Session************")
                actortype = requeststrinput(f" Enter [1] for Citizen | [2] for Portal Admin | [3] For Contractor | Your selection = ","menuopt")   
                
                phtrs_actorsession(actortype,newpotholeobj,personname)
            else:
                phtrs_actorsession(actortype,newpotholeobj,personname)
                                                
            phtrs_demo_proto(actortype,personname)  
    except Exception as e:
        print(f"An error occurred within func-phtrs_demo_proto(): {e}. Exiting program.")
        sys.exit() # system exit


##################### program main ##################################################

ph_serviceregistry = {} #defines a registry list of pothole service requests
ph_regfile_path = "potholesregistry.txt" 

def loadph_serviceregistry():
    try:
        with open(ph_regfile_path, "r") as file:
            alllines = file.readlines()

        for linebyline in alllines:  
            if len(linebyline) != 0:
                rconst = linebyline.split("|")
                potholeobj = pothole() #redefine
                if len(rconst) > 1:            
                    potholeobj.reporter_name = rconst[1]
                    potholeobj.ph_severity = rconst[3]
                    potholeobj.ph_size = rconst[4]
                    potholeobj.ph_location = rconst[5]
                    potholeobj.ph_address = rconst[6]
                    potholeobj.repair_priority = rconst[7]
                    potholeobj.datereported = rconst[2]
                    potholeobj.fix_status = rconst[8]
                    potholeobj.job_order = rconst[9]
                    potholeobj.crewtype = rconst[10]
        
                    potholeticket = rconst[0]
                    potholeticket=potholeticket.replace("TNo:", "")
                    update_potholeticket = {f"TNo:{potholeticket}": potholeobj}
                    ph_serviceregistry.update(update_potholeticket)           
    except Exception as e:
        print(f"An error occurred within func1-loadph_serviceregistry(): {e}. Exiting program.")        
    
def addpotholetodict(self, phticketnum):
        open_potholeticket = {f"TNo:"+str(phticketnum): self}
        ph_serviceregistry.update(open_potholeticket)
        #write it to file as well
        with open(ph_regfile_path, "a") as file: #local text file for persistence storage                       
            file.write(f"TNo:{phticketnum}|{self.reporter_name}|{self.datereported}|{self.ph_severity}|{self.ph_size}|{self.ph_location}|{self.ph_address}|{self.repair_priority}|{self.fix_status}|{self.job_order}|{self.crewtype}\n")
                
def updatepotholetodict(self, phticketnum):
        update_potholeticket = {f"TNo:"+str(phticketnum): self}
        ph_serviceregistry.update(update_potholeticket)
        with open(ph_regfile_path, "r") as file: #local text file for persistence storage                       
             alllines = file.readlines()

        updatedlinnes = ""
        for linebyline in alllines:  
            if len(linebyline) != 0:
                rconst = linebyline.split("|")
                potholeobj = pothole() #redefine
                if len(rconst) > 1:
                    potholeticket = rconst[0]
                    potholeticket=potholeticket.replace("TNo:", "")
                    if potholeticket == phticketnum:
                        updatedlinnes = updatedlinnes +f"TNo:{phticketnum}|{self.reporter_name}|{self.datereported}|{self.ph_severity}|{self.ph_size}|{self.ph_location}|{self.ph_address}|{self.repair_priority}|{self.fix_status}|{self.job_order}|{self.crewtype}"
                    else:                       
                        updatedlinnes = updatedlinnes +f"{linebyline}"
        with open(ph_regfile_path, "w") as file: #local text file for persistence storage                       
                    file.write(updatedlinnes)
        
                               
def retrievestatusofpotholerepair(ticketnumber,attribute):
        tnumref = f"TNo:{ticketnumber}"
        if ph_serviceregistry.get(tnumref):
            userpotholeobj = ph_serviceregistry.get("TNo:"+ticketnumber)
            if attribute == "":
                print(f" Your pothole severity was {userpotholeobj.ph_severity}")
            elif attribute == "fixstatus":
                print(f"Hi {userpotholeobj.reporter_name.upper()}. You reported a pothole on {userpotholeobj.datereported}")
                print(f" Your {userpotholeobj.ph_severity} pothole's repair status is: {userpotholeobj.fix_status.upper()}")
            elif attribute == "resolveit":
                print(f"This pothole was reported {userpotholeobj.datereported}")
                userpotholeobj.fix_status="FIXED"
                updatepotholetodict(userpotholeobj,ticketnumber)
                print(f" {ticketnumber} {userpotholeobj.ph_severity} pothole's repair status is now: {userpotholeobj.fix_status.upper()}")
            elif attribute == "updaterepairstatus":
                print(f"This pothole was reported {userpotholeobj.datereported}")
                userpotholeobj.fix_status="Work in progress"
                updatepotholetodict(userpotholeobj,ticketnumber)
                print(f" {ticketnumber} {userpotholeobj.ph_severity} pothole's repair status is now: {userpotholeobj.fix_status.upper()}")
            elif attribute == "assignjoborder":
                print(f"This pothole was reported {userpotholeobj.datereported}")
                userpotholeobj.job_order="assigned" 
                updatepotholetodict(userpotholeobj,ticketnumber)
                print(f" {ticketnumber} {userpotholeobj.ph_severity} pothole's has a job order assigned now: {userpotholeobj.job_order.upper()}")
            elif attribute == "assigncrew":
                print(f"This {ticketnumber} repair request was reported {userpotholeobj.datereported}")
                if userpotholeobj.ph_severity=="urgent":
                    userpotholeobj.crewtype="GroupA"
                else:
                    userpotholeobj.crewtype="GroupB"
                updatepotholetodict(userpotholeobj,ticketnumber)
                print(f" {ticketnumber} {userpotholeobj.ph_severity} pothole's has a job assigned to: {userpotholeobj.crewtype.upper()}")

            return ph_serviceregistry.get(ticketnumber)
        else:
            print(f"Ticket number entered is invalid!")

def processpotholerepair():
        topdeckticketnumber = next(iter(ph_serviceregistry.items()))
        potholeobj = topdeckticketnumber.get(topdeckticketnumber.key())
        print(f"Your next in queue ticket number is : {topdeckticketnumber.key()} : Opened by [{potholeobj.reporter_name}] on [{potholeobj.datereported}]")    
        
def gettotalph_requests():
        line_count = 0
        with open(ph_regfile_path, "r") as f:
            for line in f:
                if len(line) >0:
                    line_count += 1
        total_requests = line_count
        return total_requests

def printlistofpotholes(self):
        print(f"************************************")
        index = 0
        total_potholes = len(ph_serviceregistry)
        for key, value in ph_serviceregistry.items():
            index += 1
            potholeobj = value
            print(f" Pothole#{index} : {key} - Raised by {potholeobj.reporter_name} on {potholeobj.datereported}. Its severity is [{potholeobj.ph_severity}], [{potholeobj.repair_priority}] FP: {potholeobj.ph_severity} Status=[{potholeobj.fix_status}] ")
            
class pothole: #defines the pothole class
    #location = middle of road, curb, size = 1-10, repair priority = urgent, canwait - crewtype can be groupA or groupB    
    def __init__(self, reporter_name="", ph_severity="",ph_size="",ph_location="", ph_address="",repair_priority="", datereported="", fix_status="OPEN", job_order="", crewtype=""):         
        self.reporter_name = reporter_name
        self.ph_severity = ph_severity
        self.ph_size = ph_size
        self.ph_location = ph_location
        self.ph_address = ph_address
        self.repair_priority = repair_priority
        self.datereported = datereported
        self.fix_status = fix_status
        self.job_order = job_order
        self.crewtype = crewtype
        
        
###############PHTRS program ###################################################
print(f"*******************************************")
print(f"WELCOME to PHTRS portal online !!! Date: {current_day} {current_month_name.upper()}, {current_year}")
print(f"*******************************************")
if __name__ ==  '__main__': phtrs_demo_proto(0,"")
###############IDEAL Developer program end ###################################################

