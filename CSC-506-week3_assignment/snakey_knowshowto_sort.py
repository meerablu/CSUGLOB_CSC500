
############### Data Sorting Program start ###################################################
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
       microseconds =round(time.time() * 1000 * 1000) #time function returns fraction in seconds 
       """1 millisecond = 1000 microsecond 
          1 second = 1000 millisecond 
          60 second = 1 minute """
       return microseconds
    except Exception as e:
        print(f"An error occurred within currentprinttimeinms(): {e}. Exiting program.")
        sys.exit() # system exit
        
def program_start():
    try:
        whileuserunexited = exitprogram()
        """Renders the app continues           
            """
          
        while whileuserunexited:
           N = requeststrinput("Enter N series index for dataset: (for example 1=1000,2=5000, 3=10000, 4=50000, 5=100000: ","")

           numbersdataset = generatedataset(N)
           #print(f"Size of dataset: {len(numbersdataset)} First element: {numbersdataset[0]} Last element: {numbersdataset[len(numbersdataset)-1]} ")
           numbersdataset =desortarray(numbersdataset,"")
           #print(f"Size of dataset: {len(numbersdataset)} First element: {numbersdataset[0]} Last element: {numbersdataset[len(numbersdataset)-1]} ")
           #printarray(numbersdataset)
    
           #numbersdataset =sortarray(numbersdataset)
           #print(f"Size of dataset: {len(numbersdataset)} First element: {numbersdataset[0]} Last element: {numbersdataset[len(numbersdataset)-1]} ")
           numbersdataset =desortarray(numbersdataset,"p")
           #print(f"Size of dataset: {len(numbersdataset)} First element: {numbersdataset[0]} Last element: {numbersdataset[len(numbersdataset)-1]} ")
           numbersdataset = reversearray(numbersdataset)
           print(f"Size of dataset: {len(numbersdataset)} First element: {numbersdataset[0]} Last element: {numbersdataset[len(numbersdataset)-1]} ")

           if int(N) >5 or int(N) == 0:
               printarray(numbersdataset)
           
           typesort = requeststrinput("Enter T series for type sort: (for example 1=Bubble,2=Insertion,3=Selection,4=Merge: ","")
           match typesort:
            case "1":
                print(f" Snakey going to do bubble sort...")
                tstart=currentprinttimeinms()
                numbersdataset =bubblesort(numbersdataset)
                tend=currentprinttimeinms()
                print(f" Snakey took {tend-tstart} microseconds...")
            case "2":
                print(f" Snakey going to do insertion sort...")
                tstart=currentprinttimeinms()
                numbersdataset =insertionsort(numbersdataset)
                tend=currentprinttimeinms()
                print(f" Snakey took {tend-tstart} microseconds...")
            case "3":
                print(f" Snakey going to do selection sort...")
                tstart=currentprinttimeinms()
                numbersdataset =selectionsort(numbersdataset)
                tend=currentprinttimeinms()
                print(f" Snakey took {tend-tstart} microseconds...")                
            case "4":
                print(f" Snakey going to do merge sort...")
                tstart=currentprinttimeinms()
                numbersdataset =mergesort(numbersdataset)
                tend=currentprinttimeinms()
                print(f" Snakey took {tend-tstart} microseconds...")  

           print(f"POSt sort | Size of dataset: {len(numbersdataset)} First element: {numbersdataset[0]} Last element: {numbersdataset[len(numbersdataset)-1]} ")
                                                 
    except Exception as e:
        print(f"An error occurred within program_start(): {e}. Exiting program.")
        sys.exit() # system exit

        
def mergesort(arrayobj):
    """this function is the merge sorter."""
    try:
        arrsize = len(arrayobj)
       
        if arrsize <= 1: #this array is too short for any sorts.
            return arrayobj
        else:
            breakmid = arrsize //2

        leftchunkarr = arrayobj[:breakmid] #left chunk - from 0 to mid
        rightchunkarr =arrayobj[breakmid:] # right chunk - from break to end

        mergesort(leftchunkarr)
        mergesort(rightchunkarr)

        x=0
        y=0
        ind=0
               
        while x < len(leftchunkarr) and y < len(rightchunkarr):
            if leftchunkarr[x] < rightchunkarr[y]:
                arrayobj[ind] = leftchunkarr[x] #moving lesser values to left side
                x = x+1
            else:
                arrayobj[ind] = rightchunkarr[y] #keeping heavier values to the right
                y = y+1
            ind=ind+1

        while x < len(leftchunkarr):
            arrayobj[ind] = leftchunkarr[x]
            x = x+1
            ind=ind+1
            
        while y < len(rightchunkarr):
            arrayobj[ind] = rightchunkarr[y]
            y= y+1
            ind=ind+1
            
        return arrayobj
    except Exception as e:
        print(f"An error occurred within mergesort(): {e}. Exiting program.")
        sys.exit() # system exit

def selectionsort(arrayobj):
    """this function is the selection sorter."""
    try:
        arrsize = len(arrayobj)    
        for x in range(arrsize):
            min=x
            for y in range(x+1,arrsize):
                 if arrayobj[min]> arrayobj[y]:                    
                    min=y
            tmp=arrayobj[x]
            arrayobj[x]=arrayobj[min]
            arrayobj[min]=tmp           
        return arrayobj
    except Exception as e:
        print(f"An error occurred within selectionsort(): {e}. Exiting program.")
        sys.exit() # system exit
        
def insertionsort(arrayobj):
    """this function is the insertion sorter."""
    try:
        arrsize = len(arrayobj)
        x=1
        for x in range(arrsize):
            #print(f"IS {arrayobj[x-1]} GT {arrayobj[x]}")
            tmp=arrayobj[x]
            y=x-1
            while y>=0 and arrayobj[y]>tmp :
                arrayobj[y+1]=arrayobj[y]
                y=y-1

            arrayobj[y+1]=tmp

        return arrayobj
    except Exception as e:
        print(f"An error occurred within insertionsort(): {e}. Exiting program.")
        sys.exit() # system exit

def bubblesort(arrayobj):
    """this function is the bubble sorter."""
    try:
        arrsize = len(arrayobj)    
        for x in range(arrsize):
            cur = x           
            for y in range(arrsize-cur-1):                
                nxt = y+1
                #print(f"IS {arrayobj[y]} GT {arrayobj[nxt]}")               
                if arrayobj[y]> arrayobj[nxt]:   
                    tmp = arrayobj[y]
                    arrayobj[y]=arrayobj[nxt]
                    arrayobj[nxt]=tmp
                    #print(f"SWAPPED {arrayobj[y+x]} with {arrayobj[nxt]} ....")                

        return arrayobj
    except Exception as e:
        print(f"An error occurred within bubblesort(): {e}. Exiting program.")
        sys.exit() # system exit
        
def generatedataset(ndataset):
    """this function is created to generte the numbers data set as per instructions of
        this assignment."""
    try:
        numbers_arr_dataset = []
        rangeval =5
        match ndataset:
            case "1":
                rangeval = 1000
            case "2":
                rangeval = 5000
            case "3":
                rangeval = 10000
            case "4":
                rangeval = 50000
            case "5":
                rangeval = 100000
                
        for x in range(rangeval):
            numbers_arr_dataset.append(x+1)
        return numbers_arr_dataset 
    except Exception as e:
        print(f"An error occurred within generatedataset(): {e}. Exiting program.")
        sys.exit() # system exit

def printarray(arrayobj):
    try:
        for i in range(len(arrayobj)):
            print(f"{arrayobj[i]}")
        
    except Exception as e:
        print(f"An error occurred within printarray(): {e}. Exiting program.")
        sys.exit() # system exit
        
def sortarray(arrayobj):
    """this function is created to purposely sort the data if it is unsorted and
    neede to be sorted. """
    try:
        sorted_array = sorted(arrayobj)       
        return sorted_array 
    except Exception as e:
        print(f"An error occurred within sortarray(): {e}. Exiting program.")
        sys.exit() # system exit

def reversearray(arrayobj):
    """this function is created to purposely reverse the order of the sort. It is non adaptive
    and does not care if the list is first sorted or not. This means to sort in descending,
    we have to first run the list through the sort function. """
    try:
        arrsize = len(arrayobj)
        reversearr = []
        while arrsize>0:
            ind = arrsize-1
         
            reversearr.append(arrayobj[ind])
            arrsize=ind
        return reversearr
    except Exception as e:
        print(f"An error occurred within reversearray(): {e}. Exiting program.")
        sys.exit() # system exit
        
def desortarray(arrayobj, part):
    """this function is created to partially sort the data if it is the p value is passed in. """
    try:
        sortdt = len(arrayobj)
        if part=="p":
            midind =sortdt//2
            lastind = sortdt
            partarray=arrayobj[midind:lastind]
            partarray = random.sample( sorted(partarray), len(partarray))
            unsorted_array = arrayobj[0:midind]+partarray            
        else:
            unsorted_array = random.sample( sorted(arrayobj), sortdt)
                        
        return unsorted_array
    except Exception as e:
        print(f"An error occurred within desortarray(): {e}. Exiting program.")
        sys.exit() # system exit


###############main program ###################################################
print(f"*******************************************")
print(f"Welcome to Snakey knows how to sort program  - It will be fun to watch!!")
print(f"*******************************************")
if __name__ ==  '__main__': program_start()
############### program end ###################################################

