#####################program start ##################
import sys
import array

def userwishestoexit(): # generic function defined to capture program exit Q
    try:
        user_input = input("Press enter to continue or Type Q to quit! ")
        if user_input.upper() == 'Q': # if the user enters a q or Q the program ends
            print("Exiting program...Thank you!")
            sys.exit() # calling system.exit
        else:
            return True # otherwise continue with the program flow
    except Exception as e:
        print("An error occurred within func-userwishestoexit(): {e}. Exiting program.") # print out the error

def requeststrinput(verbiage,checktype): # generic function defined to capture string type inputs or prompts
    try:        
        inputval = input(verbiage) #actual verbiage is getting passed into the function for prompting the user
        checkinginputval = True
        while checkinginputval:
            if inputval!="":
                if checktype==True: #this is specially validating additional logic if needed e.g. was thinking in case user is not typing item names freely
                    if inputval in myShoppinglist: #comparing the utterance with the inventory to see if it is actually available, but the req did not mention this so it is not used
                        #print("\'"+inputval+"\' is OK!") #this was my debug line only 
                        break
                    else:
                        print("Sorry! You've entered \'"+inputval+"\' which is Invalid!") # letting user know they need to enter a valid digit
                        inputval = input(verbiage)
                else:
                    #print("\'"+inputval+"\' is OK!") #this was my debug line only 
                    break                
            else:
                print("Sorry! You have not entered anything yet. ") # letting the user reenter because it was empty
                inputval = input(verbiage)
                
        return inputval    
    except Exception as e:
        print(f"An error occurred within func-requestnumericinput(): {e}. Exiting program.") # print out the error

def requestnumericinput(verbiage,checktype): # generic function defined to capture numerical type input
    try:        
        inputval = input(verbiage) #actual verbiage is getting passed in to be prompted
        checkinginputval = True
        while checkinginputval:
            if inputval!="":
                if checktype==True: #this is meant to introduce additional logic for validation

                    try: # ie. checking for that float input 
                        float(inputval)
                        #print("\'"+inputval+"\' is OK!") #this was my debug line only 
                        checkinginputval =False
                        break
                    except ValueError:
                        print("Sorry! You've entered \'"+inputval+"\' which is Invalid!") # allow the user to reenter until its a valid float before moving on
                        inputval = input(verbiage)            
                else:
                    
                    if inputval.isdigit(): #checking to see if input conforms to digit for quantity
                        #print("\'"+inputval+"\' is OK!") #this was my debug line only 
                        checkinginputval =False
                        break
                    else: #if not allow user to reenter until its a valid digit as well
                        print("Sorry! You've entered \'"+inputval+"\' which is Invalid!") # letting user know they need to enter a valid digit
                        inputval = input(verbiage)
            else:
                  print("Sorry! You have not entered anything yet. ") # letting user know they need to enter a valid digit
                  inputval = input(verbiage)
        return inputval    
    except Exception as e:
        print(f"An error occurred within func-requestnumericinput(): {e}. Exiting program.") # print out the error



def createShoppingCart(): # Defined function name mainprog
    try:
        print("Welcome to Shopping Cart!!")
        myShoppinglist = []
        whileuserunexited = userwishestoexit()
        while whileuserunexited: #while the program hasnt been exitted by user request

            #defined below grouping for item 1 and each allows for type checking
            item1name = requeststrinput("Enter the First item name: ",False)
            item1price = requestnumericinput("Enter the price for "+item1name+": $",True)
            item1quantity = requestnumericinput("Enter the Quantity for "+item1name+": #",False)
            itemobj1 = ItemToPurchase(item1name, float(item1price), int(item1quantity))

            #defined below grouping for item 2 and each allows for type checking as well
            item2name = requeststrinput("Enter the Second item name: ",False)
            item2price = requestnumericinput("Enter the price for "+item2name+": $",True)
            item2quantity = requestnumericinput("Enter the Quantity for "+item2name+": #",False)
            itemobj2 = ItemToPurchase(item2name, float(item2price), int(item2quantity))

            myShoppinglist.append(itemobj1.item_name) #only extra adding into array, not really utilized
            myShoppinglist.append(itemobj2.item_name)#only extra adding into array, not really utilized
            print("Thanks! Your requested items are "+itemobj1.item_name+" and "+itemobj2.item_name+"! ")

            totalcostitem1 = itemobj1.item_quantity*itemobj1.item_price #calculations for item 1
            totalcostitem2 = itemobj2.item_quantity*itemobj2.item_price #calculations for item 2
            print(itemobj1.item_name+" x"+str(itemobj1.item_quantity)+" @ $"+str(itemobj1.item_price)+" = $"+str(totalcostitem1)) #print outs based on program requirements
            print(itemobj2.item_name+" x"+str(itemobj2.item_quantity)+" @ $"+str(itemobj2.item_price)+" = $"+str(totalcostitem2)) #print outs based on program requirements

            totalcost = totalcostitem1+totalcostitem2 #summation total cost
            print("Total: $"+str(totalcost)) # print outs for total cost of both items
           

            createShoppingCart()  # Unless user explicitly exits the program would return
    except Exception as e:
        print(f"An error occurred within func-createShoppingCart(): {e}. Exiting program.") # print out the error
        sys.exit() 

##################### program main ##################
        
myShoppinglist = []
class ItemToPurchase: #Define Class name
  def __init__(self, item_name, item_price, item_quantity): #constructor for class object with 3 attributes
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity

if __name__ ==  '__main__': createShoppingCart() #calling the main - mainprog to run

#####################program end ##################
