
############### Data Processing Program start ###################################################
import sys # import basic sys library
import time #import time for calculations
import re #import regex for pattern parsing
import random #import randomizer to help shuffle data

def exitprogram(): # function to exit the program
    try:
        user_input = input("Press Enter to continue or Type Q to exit program! ")
        if user_input.upper() == 'Q': 
            print("Program will now exit...Thank you!")
            sys.exit() # program exit
        else:
            return True # program continues
    except Exception as e:
        print(f"An error occurred within func-exitprogram(): {e}. Exiting program.") 

def requeststrinput(verbiage,inputtype): # generic function for user input
    try:        
        inputval = input(verbiage) #pass in verbiage to prompt the user
        checkinginputval = True        

        while checkinginputval:
            if inputtype == "":
                if inputval!="":                
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        return inputval 
                else:
                    print("Sorry! You have not entered anything yet. ") #reprompting for user input
                    inputval =requeststrinput(f"{verbiage}","")
            elif inputtype == "digit":
                if inputval!="":
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        if inputval.isdigit() and int(inputval) >= 0:
                            return inputval 
                        else:
                            print("Sorry! Your entry is Invalid. ")                          
                            inputval =requeststrinput(f"{verbiage}","digit")  
                else:
                    print("Sorry! You have not entered any options. ") 
                    inputval =requeststrinput(f"{verbiage}","digit")                                
        else:
            print(f"Exiting program...Thank you!")
            sys.exit() # calling system.exit                       
    except Exception as e:
        print(f"An error occurred within func-requeststrinput(): {e}. Exiting program.")  
  
def currentprinttimeinms():
    try:
       milliseconds =round(time.time() * 1000) #time function returns fraction in seconds 
       """1 millisecond = 1000 microsecond 
          1 second = 1000 millisecond 
          60 second = 1 minute """
       return milliseconds
    except Exception as e:
        print(f"An error occurred within currentprinttimeinms(): {e}. Exiting program.")
        sys.exit() # system exit
        
def program_start():
    try:
        whileuserunexited = exitprogram()
        """Renders the app continues           
            """
        usgeolostacklist = pullprocessdata()
          
        while whileuserunexited:
           #geolocontext = requeststrinput("Enter search context by City or Zip (others)City-Zip|City-state|Sqmi : ","")
           geolocontext = requeststrinput("Enter search context by| City or Zip |: ","")
           limit = requeststrinput("Enter search limit note: 0 for full dataset i.e., no limit)|0, 10, 100, 1000 or 10000|: ","digit")
           
           arrraydata =putdatatoarray(usgeolostacklist,geolocontext.lower().strip(),limit)
          
           dowhat = requeststrinput("Enter 1 for BinarySearch OR 2 for LinearSearch  : ","digit")


           if dowhat=="1": #The Binary Search Algorithm
               print(f"For BinarySearch, we can search by Zip codes or City names.")              
               print(f"SIZE of current data array {arrraydata.size()} the first is {arrraydata.get(0)}")
               
               print(f"Sorting data...")
               arrsorted =sortingarray( arrraydata )               
               print(f"After sorting first became {arrsorted[0]}")

               if geolocontext.lower().strip() == "zip":
                   cityorzip = requeststrinput("Enter the Zipcode to search : ","digit")
               else:
                   cityorzip = requeststrinput("Enter the City to search : ","")

               tstart = currentprinttimeinms()
               binarysearch(usgeolostacklist,arrsorted,cityorzip)
               tend = currentprinttimeinms()
               print(f"Total time BS: {(tend-tstart)} miliseconds")
               
           else: #The Linear Search Algorithm
               print(f"For LinearSearch, we can search by Zip codes or City names.")
               
               print(f"SIZE of current data array {arrraydata.size()} the first is {arrraydata.get(0)}")
               print(f"Jumbling zip and city data...")
               arrunsorted =jumbleuparray( arrraydata )               
               print(f"After jumbling first became {arrunsorted[0]}")

               if geolocontext.lower().strip() == "zip":
                   cityorzip = requeststrinput("Enter the Zipcode to search : ","digit")
               else:
                   cityorzip = requeststrinput("Enter the City to search : ","")

               tstart = currentprinttimeinms()
               linearsearch(usgeolostacklist,arrunsorted,cityorzip)
               tend = currentprinttimeinms()
               print(f"Total time LS: {(tend-tstart)} miliseconds")
              
                                    
    except Exception as e:
        print(f"An error occurred within program_start(): {e}. Exiting program.")
        sys.exit() # system exit

def binarysearch(geolocobj,sortedarrayobj,searchkey):
    try:
         foundvalue=None
         
         left = 0
         right = len(sortedarrayobj) - 1

         while left <= right: # Calculate the middle index using integer division
             midind = (left + right) // 2
             
             if sortedarrayobj[midind].lower().strip()==searchkey.lower().strip():
                foundvalue=sortedarrayobj[midind]
                break
             elif sortedarrayobj[midind].lower().strip() < searchkey.lower().strip():
                left = midind + 1  #search in right half
             else:
                right = midind - 1 #search in left half    

         if foundvalue != None:
             geoobj = geolocobj.findbyvalue(foundvalue)
             print(f"FOUND IT!!  {geoobj.zipcode} is {geoobj.city} in {geoobj.state}. It is {geoobj.sqmi} Sq Miles. ")
         else:
             print(f"NOT FOUND!! {searchkey}")
             geoobj = None
             
         return geoobj
    except Exception as e:
        print(f"An error occurred within binarysearch(): {e}. Exiting program.")
        sys.exit() # system exit

def linearsearch(geolocobj,unsortedarrayobj,searchkey):
    try:
         foundvalue=None
         for i in range(len(unsortedarrayobj)):
             if unsortedarrayobj[i].lower().strip()==searchkey.lower().strip():
                 foundvalue=unsortedarrayobj[i]
                 break

         if foundvalue != None:
             geoobj = geolocobj.findbyvalue(foundvalue)
             print(f"FOUND IT!!  {geoobj.zipcode} is {geoobj.city} in {geoobj.state}. It is {geoobj.sqmi} Sq Miles. ")
         else:
             print(f"NOT FOUND!! {searchkey}")
             geoobj = None
             
         return geoobj
    except Exception as e:
        print(f"An error occurred within linearsearch(): {e}. Exiting program.")
        sys.exit() # system exit

def sortingarray(arrayobj):
    """this function is created to purposely sortthe data to make it sorted so it
    simulates closer to reality when we run the binary search compares."""
    try:
        sorted_array = sorted(arrayobj)       
        return sorted_array 
    except Exception as e:
        print(f"An error occurred within jumblesortedarray(): {e}. Exiting program.")
        sys.exit() # system exit
        
def jumbleuparray(arrayobj):
    """this function is created to purposely randomize the data to make it unsorted so it
    simulates closer to reality when we run the linear search compares."""
    try:
        shuffled_array = random.sample( sorted(arrayobj), arrayobj.size())        
        return shuffled_array 
    except Exception as e:
        print(f"An error occurred within jumblesortedarray(): {e}. Exiting program.")
        sys.exit() # system exit

def putdatatoarray(usgeolostacklist,data,limit):
    """this function is created to put the linear value data sets into the array so then
    we can run our two search algorithms against the array in sorted for binary search and or unsorted fashion for linear search"""
    try:
        arrayobj = geo_sorted_array()
        sortedarray = usgeolostacklist.collectdata(data, arrayobj,limit)
        return sortedarray       
    except Exception as e:
        print(f"An error occurred within putsortedarray(): {e}. Exiting program.")
        sys.exit() # system exit
        
def pullprocessdata():
    """this function is created with pattern regex to quickly parse through the downloaded public
    US zip code , geo location data or information for purposes of simulating data pipeline processing algorithms and render"""
    try:
        pattern = r'^([\d.]+),,([\d.]+),"(MULTIPOLYGON\s*\(+.*?\)+)",([\w.(\s*)(+.*?\)?-?\/?-]+),([\d.]+),([\d.]+),,([\w.(\s*)]+),([\d.]+)'

        with open("Boundaries__US_Zip_Codes.csv", "r") as file: 
            alllines = file.readlines()
            #Shape__Area,LATITUDE,SQMI,the_geom,CITY,OBJECTID,ZIPCODE,LONGITUDE,STATE,Shape__Length
        ind = 0

        usgeololist = geolo_Stack()
        print("Loading data...")
        for linebyline in alllines:
            if ind==0:
                ind = ind+1
                continue
            
            if len(linebyline) != 0:
                match = re.search(pattern, linebyline)
                if match:
                    ind = ind+1
                    area = match.group(1) # Shape Area
                    sqmi = match.group(2) #sq mi
                    zipcode   = match.group(6) # zipcode
                    city = match.group(4) # city
                    state = match.group(7) # state
                    
                    geoloobj = geolocations(zipcode, sqmi, city, state, area) # we objectize the geoloc object for benefit of its accessors
                    usgeololist.append(geoloobj) #and then we store them into the stack based list                             
        print(f"TOTAL geolocations: {usgeololist.size()}") #the total is correct based on the source data
        return usgeololist       
                   
    except Exception as e:
        print(f"An error occurred within pullprocessdata(): {e}. Exiting program.")
        sys.exit() # system exit
        
##################### program main ##################################################

class geolocations:
    def __init__(self, zipcode, sqmi, city, state, area):
        self.zipcode = zipcode
        self.sqmi = sqmi
        self.city = city
        self.state = state
        self.area = area

######################################Geo array Imp ###################################
class geo_sorted_array:
    def __init__(self):
        self.geo_sorted_array = []

    def append(self,geoloc):
        self.geo_sorted_array.append(geoloc)

    def get(self,pos):
        return self.geo_sorted_array[pos]
        
    def isempty(self):
        if len(self.geo_sorted_array) == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.geo_sorted_array)

    def __iter__(self):
        """Implement the iterable interface to allow method sorting"""
        return iter(self.geo_sorted_array)

######################################End Geo array Imp ###################################

######################################List based Stack Imp ###################################
class geolo_Stack:
    def __init__(self):
        self.geolo_stack = []

    def append(self,geoloc):
        self.geolo_stack.append(geoloc)

    def findbyvalue(self,dataval):
        for i in range(len(self.geolo_stack)):
            geolobj = self.geolo_stack[i]
            if dataval.isdigit():
                if geolobj.zipcode == dataval.strip():
                    return geolobj
            else:
                if geolobj.city.lower().strip() == dataval.lower().strip():
                    return geolobj
                
    def pop(self):
        if not len(self.geolo_stack) == 0:
            geolo = self.geolo_stack.pop()
            return geolo
        else:
            return None 

    def collectdata(self,data, arrayobj,limit):
        rangelen = int(limit)
        if int(limit)==0:
            rangelen = len(self.geolo_stack) #full range, search all data
            
        for i in range(rangelen):                
            match data:
                case "zip":
                    arrayobj.append(f"{self.geolo_stack[i].zipcode}")
                case "city":    
                    arrayobj.append(f"{self.geolo_stack[i].city}")
                case "city-zip":    
                    arrayobj.append(f"{self.geolo_stack[i].city,self.geolo_stack[i].zipcode }")
                case "city-state":    
                    arrayobj.append(f"{self.geolo_stack[i].city,self.geolo_stack[i].state }")
                case "sqmi":    
                    arrayobj.append(f"{self.geolo_stack[i].zipcode,self.geolo_stack[i].sqmi}")
        return arrayobj             
    
    def isempty(self):
        if len(self.geolo_stack) == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.geolo_stack)
######################################End Stack Imp ###################################

###############main program ###################################################
print(f"*******************************************")
print(f"Welcome to Snakey Data processing program  - It will be fun to watch!!")
print(f"*******************************************")
if __name__ ==  '__main__': program_start()
############### program end ###################################################

