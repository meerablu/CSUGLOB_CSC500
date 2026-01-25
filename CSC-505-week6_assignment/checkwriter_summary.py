############### check writer program start ###################################################
import sys # import basic sys library
from array import array 
from decimal import Decimal #for processing cents
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
            return True 
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
                        return inputval 
                else:
                    print("Sorry! You have not entered anything yet. ") # user prompt for empty string
                    inputval = input(verbiage)
            elif inputtype == "yesno":
                if inputval!="":
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        if inputval.lower() == "y" or inputval.lower() == "n":
                            return inputval
                        else:
                            print("Please enter Y or N ") 
                            inputval = input(verbiage)
                else:
                    print("Sorry! You have not entered any options. ") 
                    inputval = input(verbiage)
            elif inputtype == "moneyvalue":
                stillcheckinginputval = True
                while stillcheckinginputval:
                    if not inputval == "" : 
                        if "." in inputval:
                            numlist = inputval.split('.')
                            if len(numlist)==2:
                                if not numlist[0].isdigit(): 
                                    print("Dollar$$ value is invalid!") 
                                    inputval = input(verbiage)
                                    continue
                                elif not numlist[1].isdigit(): 
                                    print("Dollar$$ value is invalid!")
                                    inputval = input(verbiage)
                                    continue
                                else: 
                                    dollaramount = round(Decimal(inputval),2) 
                                    
                                    stillcheckinginputval=False
                                    return dollaramount
                                    #break  
                            else:
                                print("Dollar$$ value is invalid!") 
                                inputval = input(verbiage)
                                continue
                                                     
                        else:
                            if inputval.isdigit(): 
                                dollaramount = round(Decimal(inputval),2) 
                                stillcheckinginputval=False
                                return dollaramount
                                    #
                                #break
                            else:
                                print("Dollar$$ value is invalid!")
                                inputval = input(verbiage)
                                continue
                    else:
                        print("Dollar value can not be empty!")
                        inputval = input(verbiage)
                        continue
        else:
            print(f"Exiting program...Thank you!")
            sys.exit() # calling system.exit                       
    except Exception as e:
        print(f"An error occurred within func-requeststrinput(): {e}. Exiting program.")  

def confirm_issuecheck(dollarvalue,check):
    try:
        confirmcheck = requeststrinput(f"Are you ready to issue this check of amount ${dollarvalue}? Y/N ","yesno")
        if confirmcheck.lower() == "y":
            check.dollarvalue =dollarvalue
            return True
        else:
            return False       
    except Exception as e:
        print(f"An error occurred within func-confirm_issuecheck(): {e}. Exiting program.")
        sys.exit() # system exit
        
def write_check(check): # main python program 
    try:        
        whileuserunexited = userwishestoexit()
        
        """Renders the app continues           
            """
        while whileuserunexited:       
             
            writeacheck = requeststrinput("Are you ready to continue to write a check? Y/N ","yesno")
            if writeacheck.lower() == "y":
                payorname = requeststrinput("Enter your name: ","")            
                payeename = requeststrinput("Enter check recipient name: ","")
                amountvalue = requeststrinput("Enter check amount $: ","moneyvalue")
                checknote = requeststrinput("Enter check memo: ","")

                check.payor_name =payorname
                check.payee_name =payeename
                check.checkdate = f"{current_month_name} {current_day}, {current_year}"
                check.checknote =checknote
                check.dollarvalue =amountvalue

                checkisconfirmed = confirm_issuecheck(amountvalue,check)

                while not checkisconfirmed:
                    amountvalue = requeststrinput("Enter check amount $: ","moneyvalue")
                    checkisconfirmed = confirm_issuecheck(amountvalue,check)
                else:
                    convertdollaramount(check)
                    generatecheck(check)
                               
            else:
                print(f"Please come back when you are ready. Thank you !")
                write_check(check) 

            newcheck = paycheck()                                         
            write_check(newcheck) 
    except Exception as e:
        print(f"An error occurred within func-write_check(): {e}. Exiting program.")
        sys.exit() # system exit


##################### check writer program main ##################################################
unit_valuemap = {"1": "one","2": "two","3": "three","4": "four","5": "five","6": "six","7": "seven","8": "eight","9": "nine"} 
tens_valuemap = {"10": "ten","11":"eleven","12":"twelve","13":"thirteen","14":"forteen","15":"fifteen", "16":"sixteen","17":"seventeen","18":"eigteen","19":"nineteen","20": "twenty","30": "thirty","40": "forty","50": "fifty","60": "sixty","70": "seventy","80": "eighty","90": "ninety"}
digitsteps_valuemap = {"1digit":"unit", "2digit":"tens", "3digit":"hundred", "4digit":"thousand",  "5digit":"thousand", "6digit":"thousand", "7digit": "million"}


def processdollar(amount):
    try:
        valuedollar = "zero"
        digitvalue = int(amount)
        lendigit = len(amount)
        print(f"No digits? {lendigit}")
        if digitvalue>0: 
            if lendigit == 1: #process below ten(s) dollars value
                valuedollar = unit_valuemap.get(str(digitvalue))

            elif lendigit == 2: #process ten(s) dollars value
                valuedollar = processtensrange(amount)

            elif lendigit == 3: #process hundred(s) dollars value 
                valuedollar = processhundredsrange(amount)
                          
            elif lendigit == 4: #process thousand(s) dollars value
                valuelabel = digitsteps_valuemap.get(f"{lendigit}digit")
                
                unit_thou_value = int(amount[0])                
                firstpart = unit_valuemap.get(str(unit_thou_value)) #X thousand                
                remainderfromthou = digitvalue - int(f"{unit_thou_value}000") 
                 
                if remainderfromthou > 0:
                    hundredparts = processhundredsrange(str(remainderfromthou))
                    valuedollar = firstpart +" "+valuelabel +" and "+hundredparts                                                                           
                else:
                    valuedollar = firstpart +" "+valuelabel   

            elif lendigit == 5: #process ten thousand(s) dollars value
                valuelabel = digitsteps_valuemap.get(f"{lendigit}digit")

                unit_tenthou_value = int( f"{amount[0]}{amount[1]}")
                thousandtens =  str(unit_tenthou_value)[0]
                remainderthousandtens = str(unit_tenthou_value)[1]
                
                if remainderthousandtens == "0":                    
                    firstpart = tens_valuemap.get(f"{thousandtens}0") #XX thousands
                else:
                    if unit_tenthou_value > 19:
                        firstpart = tens_valuemap.get(f"{thousandtens}0")+" "+unit_valuemap.get(remainderthousandtens) #XX thousands
                    else:#10-19
                        if unit_tenthou_value == 10:
                            firstpart = tens_valuemap.get(f"{thousandtens}0")+" " #XX thousands
                        else:
                            firstpart = tens_valuemap.get(f"{unit_tenthou_value}")+" " #XX thousands
                                                               
                remainderfromtenthou = digitvalue - int(f"{unit_tenthou_value}000")
                             
                if remainderfromtenthou > 0:
                    if remainderfromtenthou < 99:
                        
                        hundredparts = processhundredsrange(str(remainderfromtenthou))                         
                        valuedollar = firstpart +" "+valuelabel +" and "+ hundredparts

                    elif remainderfromtenthou < 999:
                        
                        hundredparts = processhundredsrange(str(remainderfromtenthou))
                        valuedollar = firstpart +" "+valuelabel +" and "+ hundredparts  
                    else:# remainderfromtenthou < 9999:
                        print(f"should not be here")                                                                                  
                else:
                    valuedollar = firstpart +" "+valuelabel
                    
            elif lendigit == 6: #process hundred thousand(s) dollars value
                valuelabel = digitsteps_valuemap.get(f"{lendigit}digit")
                #break the first part and second part
                thousandvalue = f"{amount[0]}{amount[1]}{amount[2]}"
                hundredvalue = f"{amount[3]}{amount[4]}{amount[5]}"
                
                hundredthouparts = processhundredsrange(str(thousandvalue))
                hundredparts = processhundredsrange(str( hundredvalue))
                
                valuedollar = hundredthouparts +" "+valuelabel +" "+hundredparts
            elif lendigit == 7:
                valuelabel = digitsteps_valuemap.get(f"{lendigit}digit")
                valuelabel2 = digitsteps_valuemap.get(f"6digit")
                
                millionvalue = f"{amount[0]}"
                thousandvalue = f"{amount[1]}{amount[2]}{amount[3]}"
                hundredvalue = f"{amount[4]}{amount[5]}{amount[6]}"


                hundredthouparts = processhundredsrange(str(thousandvalue))
                hundredparts = processhundredsrange(str( hundredvalue))              
                
                valuedollar = unit_valuemap.get(str(millionvalue)) +" "+valuelabel+" "+hundredthouparts +" "+valuelabel2+" "+ hundredparts 

            elif lendigit > 7:

                print(f"{amount} dollar exceeded range!!!Exiting program")
                valuedollar = ""
                sys.exit() # system exit
                
            
        return valuedollar
    except Exception as e:
        print(f"An error occurred within func-processdollar(): {e}. Exiting program.")
        sys.exit() # system exit

def processhundredsrange(amount):
    try:
        valuehundreds = ""
        digitvalue = int(amount)

        if digitvalue > 99:
            valuelabel = digitsteps_valuemap.get(f"3digit")
            unit_hun_value = int(amount[0])
            firstpart = unit_valuemap.get(str(unit_hun_value))                
            remaindertens = digitvalue - int(f"{unit_hun_value}00") 
            if remaindertens > 0:
                secondpart = processtensrange(str(remaindertens))
                valuehundreds = firstpart+ " "+valuelabel +" "+secondpart
            else:
                valuehundreds = firstpart +" "+valuelabel      
        else:
            valuehundreds = processtensrange(amount)
                                                        
        return valuehundreds      
    except Exception as e:
        print(f"An error occurred within func-processhundredsrange(): {e}. Exiting program.")
        sys.exit() # system exit

    
def processtensrange(amount):
    try:
        valuetens = "zero"
        digitvalue = int(amount)

        if digitvalue>0: #automatically assumes 2 positions because but can still be leading zero
            if digitvalue>9 :                                
                
                if digitvalue<20:
                    
                    tensvalue = digitvalue
                    firstpart = tens_valuemap.get(str(tensvalue))
                    valuetens = f"{firstpart}"
                else:
                    
                    unitvalue = int(str(digitvalue)[1]) 
                    tensvalue = digitvalue-unitvalue 
                    firstpart = tens_valuemap.get(str(tensvalue))
                    secondpart = unit_valuemap.get(str(unitvalue))
                    valuetens = f"{firstpart} {secondpart}"
            else:               
                valuetens = unit_valuemap.get(str(digitvalue))            
        return valuetens      
    except Exception as e:
        print(f"An error occurred within func-processtensrange(): {e}. Exiting program.")
        sys.exit() # system exit

def convertdollaramount(self):
    try:
        amountvaluedollar = processdollar(str(self.dollarvalue).split(".")[0])
        amountvaluecents = processtensrange(str(self.dollarvalue).split(".")[1])

        processedvalue = f"{amountvaluedollar} dollar(s) and {amountvaluecents} cents"       
        self.dollaramount=processedvalue
    except Exception as e:
        print(f"An error occurred within func-convertdollaramount(): {e}. Exiting program.")
        sys.exit() # system exit
    
def generatecheck(self):
        print(f"*******************************************************************************")
        print(f"**********************Bank of Python Proppie Check$$$**************************")
        print(f"Pay to: {self.payee_name}                        DATE:{self.checkdate}")
        print(f"Sum of: {self.dollaramount} only.   Total: ${self.dollarvalue}")
        print(f"For: {self.checknote}                                                          ")
        print(f"Payor signed: {self.payor_name}                                                ")
        print(f"*******************************************************************************")
        print(f"*******************************************************************************")
                                  
class paycheck: #defines the paycheck class - it has the payee, payor, date and the amount values 
    def __init__(self, payor_name="", payee_name="",checkdate="",checknote="", dollarvalue="",dollaramount="", checkstatus=""):         
        self.payor_name = payor_name
        self.payee_name = payee_name
        self.checkdate = checkdate
        self.checknote = checknote
        self.dollarvalue = dollarvalue
        self.dollaramount = dollaramount
        self.checkstatus = checkstatus
        
paycheckobj = paycheck()    
###############Check Writer program ###################################################
print(f"*******************************************")
print(f"WelCOme to Check writer program - Helps you write the dollar amount$$$ !!")
print(f"*******************************************")
if __name__ ==  '__main__': write_check(paycheckobj)()
############### program end ###################################################

