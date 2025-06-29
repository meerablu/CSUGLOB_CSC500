###############program start ###################################################
import sys # import basic sys library
import math # import basic math library because we have a use for flooring
import numpy as np #import the numpy library for great utilization of 2d arrays

def userwishestoexit(): # defined its own set of function for cleaner code
    try:
        user_input = input("Press enter to continue or Type q/Q to quit! ")
        if user_input.upper() == 'Q': # advise from Kade which Ive applied and thought its better flexibility 
            print("Exiting program...Thank you!")
            sys.exit() # Exit gracefully
        else:
            return True # continue program run flow
    except Exception as e:
        print(f"An error occurred within func-userwishestoexit(): {e}. Exiting program.") # using curly braces to print out the exception and remarking which function is erroring out
        
def requestnumericinput(verbiage,checktype): #avoiding too much redundancy in flow for repeatable phrases - so passed in the verbiage
    try:        
        inputval1 = input(verbiage) #reusing the same input value function now appropriate to capture numeric inputs 
        checkinginputval = True
        while checkinginputval:
                if inputval1.isdigit(): #first checking universally for numerical input forms , whether there is digit conformance
                    if checktype==True: #this is the one for entering the current hour of day - and requires special checking value range 
                         if int(inputval1) >= 0 and int(inputval1) <=23: #TOD only accepts integer numbers from 0 to 23 based on ask of program
                            print("\'"+inputval1+"\' is OK!") #this was my debug line only 
                            break
                         else:
                            print("Sorry! You've entered \'"+inputval1+"\' which is Invalid!") # letting user know they need to enter a valid digit
                            inputval1 = input(verbiage)
                    else: #else this is all good just needed to pass digit validation 
                        print("\'"+inputval1+"\' is OK!") #this was my debug line only
                        break
                   
                else:
                    print("Sorry! You've entered \'"+inputval1+"\' which is Invalid!")                           
                    inputval1 = input(verbiage)
        return inputval1    
    except Exception as e:
        print(f"An error occurred within func-requestnumericinput(): {e}. Exiting program.") # using curly braces to print out the exception and remarking which function is erroring out

def calculatealarmtime(curdayremainhour,totalhour,hrposition):
    try:        
        
        if int(curdayremainhour)>int(totalhour): #still got time in the day, so the alarm will go off later within today                   
            hourtoalarm = int(hrposition)+int(totalhour) #when to alarm is simple, just add total hours to alarm onto current hour position - runs from 0 to 23
            alarmhour12hrf = timeofdayhours[hourtoalarm,1].flatten()[0] #we got the indice of the element so we will get the time literal and flatten out the array
            print("YOUR ALARM WILL BUZZ at "+str(alarmhour12hrf)+" TODAY !!!!!!! ") #Bingo we gotten the value when the Alarm will go off today
            
        else: # the alarm will go off after today - into tomorrow or next day(s)
            balancehrtoalarm = int(totalhour)-int(curdayremainhour) #this is a slightly complicated case for when the day has not enough hours to run for the alarm
            if int(balancehrtoalarm)<24: # the alarm will go off tomorrow because the balance is less than 24 hours over the next day
                alarmhour12hrf = timeofdayhours[balancehrtoalarm,1].flatten()[0] #we got the indice of the element so we will get the time literal and flatten out the array           
                print("YOUR ALARM WILL BUZZ at "+str(alarmhour12hrf)+" TOMORROW !!!!!!! ") #Bingo we gotten the value when the Alarm will go off tomorrow        
            else:
                ruddays = math.floor(int(balancehrtoalarm)/24) #it is going into the next day or even more next days - so we get the run day hours total dividing it by 24h - and we need to floor the value
                ruddays24hr = ruddays*24 #we want to get the total of the hours run in 
                balancehrtoalarm_onday = int(balancehrtoalarm)-int(ruddays24hr) #and then we can get the balance hours for the day after minusing out all the hours for the # days run in
                #print("Balance is "+str(balancehrtoalarm)+" Mod Day is "+str(ruddays)+" for "+str(ruddays24hr)) # this is for debug line purposes to show values
                alarmhour12hrf = timeofdayhours[balancehrtoalarm_onday,1].flatten()[0] #we got the indice of the element so we will get the time literal and flatten out the array           
                
                print("YOUR ALARM WILL BUZZ at "+str(alarmhour12hrf)+" NEXT Day only !!!!!!! ") #Bingo we gotten the value when the Alarm will go off after N days next day
                                         
    except Exception as e:
        print(f"An error occurred within func-calculatealarmtime(): {e}. Exiting program.") # using curly braces to print out the exception and remarking which function is erroring out

def smallalarms(): # Defined function name mainprog
       
    try:
        print("Welcome to Python small Alarms program!")
        whileuserunexited = userwishestoexit()
        
        while whileuserunexited:       
            checkinginputval = True # we keep within the input collection loop before we start to get into the basics of calculating the current hour indice
            while checkinginputval:
                 try:
                     inputcurhour = requestnumericinput("Enter the current hour of the day between hr value 0-23: ",True)
                 except NameError:
                    continue #loop for value
                 else:
                    try:
                        totalhour = requestnumericinput("Enter total number of hours for your alarm: ",False)
                    except NameError:
                        continue #loop for value
                    else:
                        checkinginputval = False
                        break

            hrint_column = timeofdayhours[:, 0] #define the first column in the 2d array - column 0 only 
            indixtime = np.where(hrint_column == inputcurhour) #search the entered current hour value only within the first column to get the current hour position Indice  
           
            hrposition = indixtime[0][0] #will need the actual hour position in the sequential 24 hours time sequence for calculation based on the above derived Indice
            curdayremainhour = 24-hrposition # used to calculate the remaining hours in the day based on the indice position
            #print("hrposition is "+str(hrposition)+" makes remaining hour in day: "+str(curdayremainhour) +" hours.") #my debug line only for clarity
            print("Remaining hours in the day: "+str(curdayremainhour) +" hours.")

            currenthour12hrf = timeofdayhours[indixtime,1].flatten()[0] #we got the indice of the element so we will get the time literal and flatten out the array
            print("Entered Current Time of Day is "+str(currenthour12hrf)+" | (++++ADD) Hours "+str(totalhour)+" hours for Alarm.")
                      
            timealarmgoesoff = calculatealarmtime(curdayremainhour,totalhour,hrposition)
              
            input("Press enter to continue...")
            smallalarms()  # Unless user explicitly exits the program would return
    except Exception as e:
        print(f"An error occurred within func-smallalarms(): {e}. Exiting program.")
        sys.exit() # Exit out from exception

###############program main ###################################################
#timeofdayhours = ("0:12am","1:1am","2:2am","3:3am","4:4am","5:5am","6:6am","7:7am","8:8am","9:9am","10:10am","11:11am","12:12pm","13:1pm","14:2pm","15:3pm","16:4pm","17:5pm","18:6pm","19:7pm","20:8pm","21:9pm","22:10pm","23:11pm") # Using Pythong Tuples for immutability instead of array
timeofdayhours = np.array([
                   [0, "12am"],
                   [1, "1am"],
                   [2, "2am"],
                   [3, "3am"],
                   [4, "4am"],
                   [5, "5am"],
                   [6, "6am"],
                   [7, "7am"],
                   [8, "8am"],
                   [9, "9am"],
                   [10, "10am"],
                   [11, "11am"],
                   [12, "12pm"],
                   [13, "1pm"],
                   [14, "2pm"],
                   [15, "3pm"],
                   [16, "4pm"],
                   [17, "5pm"],
                   [18, "6pm"],
                   [19, "7pm"],
                   [20, "8pm"],
                   [21, "9pm"],
                   [22, "10pm"],
                   [23, "11pm"],
                  ]) # Specified a Fixed Numpy 2d array which helps us print the pretty hours and also needed the actual 0-23 integers predefined

if __name__ ==  '__main__': smallalarms() #calling the main - Alarm program run

###############program end ###################################################

