#####################program start ##################
import sys
from datetime import datetime #import the date time library

current_date = datetime.now().strftime("%B %d %Y") #gets the current date in pretty format -"January 1 2020"

def userwishestoexit(): # generic function defined to capture program exit Q
    try:
        user_input = input("Press enter to continue or Type Q to quit! ")
        if user_input.upper() == 'Q': # if the user enters a q or Q the program ends
            print("Exiting program...Thank you!")
            sys.exit() # calling system.exit
        else:
            return True # otherwise continue with the program flow
    except Exception as e:
        print(f"An error occurred within func-userwishestoexit(): {e}. Exiting program.") # print out the error

def requeststrinput(verbiage,checktype): # generic function defined to capture string type inputs or prompts
    try:        
        inputval = input(verbiage).lower() #actual verbiage is getting passed into the function for prompting the user
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

                elif checktype=="combination": #this method wil allow digit or string
                        if inputval.isdigit():
                            return inputval  
                        else:
                            if inputval == 'q': # if the user enters a q or Q the program ends
                                checkinginputval=False                           
                            else:
                                return inputval  
                elif checktype=="date": #this is amongst the input string prompts to ensure the date conforms to the format requirements
                        if inputval == 'q': # if the user enters a q or Q the program ends
                            checkinginputval=False                           
                        else:
                            try:
                                datetime.strptime(inputval, "%B %d %Y")
                                return inputval
                            except ValueError:
                                print(f"Sorry! You've entered {inputval} which is Invalid! Please enter a valid date format e.g., July 17 2025") # letting user know they need to enter a valid digit
                                inputval = input(verbiage).lower()               
                else:
                    if inputval == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        return inputval # this is for user entering as long as non empty string and is free to enter
            else:
                        print("Sorry! You have not entered anything yet. ") # letting the user reenter because it was empty
                        inputval = input(verbiage).lower()
        else:
            print("Exiting program...Thank you!")
            sys.exit() # calling system.exit
                       
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
                        checkinginputval =False
                        break
                    except ValueError:
                        print(f"Sorry! You've entered {inputval} which is Invalid!") # allow the user to reenter until its a valid float before moving on
                        inputval = input(verbiage)            
                else:                    
                    if inputval.isdigit(): #checking to see if input conforms to digit for quantity                        
                        checkinginputval =False
                        break
                    else: #if not allow user to reenter until its a valid digit as well
                        print(f"Sorry! You've entered {inputval} which is Invalid!") # letting user know they need to enter a valid digit
                        inputval = input(verbiage)
            else:
                  print("Sorry! You have not entered anything yet. ") # letting user know they need to enter a valid digit
                  inputval = input(verbiage)
        return inputval    
    except Exception as e:
        print(f"An error occurred within func-requestnumericinput(): {e}. Exiting program.") # print out the error


def print_menu(): #Defined new Online shopping cart Menu
    try:
        """MENU
            a - Add item to cart
            r - Remove item from cart
            c - Change item quantity
            i - Output items' descriptions
            o - Output shopping cart
            q - Quit
        Choose an option:
        """
        print(f"******{customercart.customer_name.upper()}'s Shopping Cart Menu Options On [{customercart.current_date.upper()}]***********")
        numitemsincart = customercart.get_num_items_in_cart()
        totalcost = customercart.get_cost_of_cart()
        if numitemsincart>0:
           print(f"=======>>>You have {numitemsincart} Items in your Cart!") #get_num_items_in_cart() for Flag headings
           print(f"=======>>>Your Total cost now is ${totalcost} for the Items in your Cart!") #get_num_items_in_cart() for Flag headings
        else:
           print(f"Your cart has 0 items...") # Flag headings 

        print("a - to add item to Cart ")
        print("r - to remove item from Cart ")
        print("c - to change item details or quantity ")
        print("i - to Output Cart items' descriptions! ")
        print("o - to Output your Shopping cart! ")
        print("q - to Quit ")
        print("*******************************************************************************")
        menuopt = requeststrinput("Choose an option:","menu")
        print("*******************************************************************************")
        match menuopt: 
            case "a":
                print(f"Menu {menuopt.upper()} - Add item to purchase")
                stilladding = True                     
                while stilladding:
                    itp = createShoppingCart()
                    customercart.add_item(itp) 
                    useryesno = requeststrinput("Would you like to add another item? Y/N :",False)
                    if useryesno.lower() != 'y':
                        stilladding=False
                        break  # Exit the loop if the condition is met                                           
                print("Finished buying stuff...")

            case "r":
                print(f"Menu {menuopt.upper()} - Remove item from cart")                
                stillremoving = True               
                while stillremoving and customercart.get_num_items_in_cart()>0:
                    itp = inventoryCartItems(customercart,"r") #calling this function passing in the customercart object and setting the R flag for removals                   
                    while itp == None: #ITP is none if the user selected an Invalid option that isnt in the cart
                        itp = inventoryCartItems(customercart,"r") #the second condition prompts for an alternate retry
                        continue 
                    else:
                        customercart.remove_item(itp)
                        #print(f"num items in cart is now {customercart.get_num_items_in_cart()}")
                        if customercart.get_num_items_in_cart()>0 :
                            useryesno = requeststrinput("Would you like to remove another item? Y/N :",False)
                            if useryesno.lower() != 'y':
                                stillremoving=False
                                break  # Exit the loop if the condition is met
                        else: 
                            stillremoving=False
                            break

            case "c":
                print(f"Menu {menuopt.upper()} - Change item in cart ")
                stillchanging = True
                     
                while stillchanging and customercart.get_num_items_in_cart()>0:
                    itp = inventoryCartItems(customercart,"c") #calling this function passing in the customercart object and setting the C flag for modifications
                    while itp == None: #ITP is none if the user selected an Invalid option that isnt in the cart
                        itp = inventoryCartItems(customercart,"c")
                        continue 
                    else:
                        customercart.modify_item(itp)
                        #print(f"num items in cart is now {customercart.get_num_items_in_cart()}")
                        if customercart.get_num_items_in_cart()>0 :
                            useryesno = requeststrinput("Would you like to change another item? Y/N :",False)
                            if useryesno.lower() != 'y':
                                stillchanging=False
                                break  # Exit the loop if the condition is met
                        else: 
                            stillchanging=False
                            break

            case "i":
                print(f"Menu {menuopt.upper()} - Print current cart item descriptions ")
                customercart.print_description()
            case "o":
                print(f"Menu {menuopt.upper()} - Print current cart items ")
                customercart.print_total()
            case _:
                # it should never reach this case for default        
                print_menu()
                
        print_menu()
    except Exception as e:
        print(f"An error occurred within func-print_menu(): {e}. Exiting program.") # print out the error
        sys.exit() 

def inventoryCartItems(ShoppingCart,typecommand): #Defined function to help user pick which items they want to remove or modify from cart, turned into 1 function
    try:
        if len(ShoppingCart.cart_items) == 0:
            print(f"Sorry! Your cart is empty. ")
            return None
        else:
            print(f"You have {len(ShoppingCart.cart_items)} item(s) in your Cart")

            itemchglist = {}
            for index, item in enumerate(ShoppingCart.cart_items):
                print(f" Item#{(index+1)}: {item.item_name}") #printing out the object cart 
                itemchglist.update({(index+1):item}) #using a dictionary to store the latest itp objects in the list
                
           
            if typecommand == "r":
                itprem = requeststrinput("Which item do you want to remove? Enter Item# Or Name: ","combination")

                if itprem.isdigit():
                    #print("indigits")
                    if int(itprem) in itemchglist:
                        itp = itemchglist.get(int(itprem))
                        print(f"Remove {itp.item_name} ... from Cart ...")
                        return itp
                    else:
                        print(f" Item#{itprem} NOT FOUND in cart or is Invalid. ")
                else:
                    itpfound = False
                    for key, itpobj in itemchglist.items():
                        if itpobj.item_name == itprem:
                            itp = itemchglist.get(key)
                            itpfound=True                           
                            break                       
                    if itpfound == True:
                        print(f"Remove {itp.item_name} ... from Cart ...")                       
                        return itp
                    else:
                        print(f" Item#{itprem} NOT FOUND in cart or is Invalid. ")
            else:
                itprem = requeststrinput("Which item do you want to modify? Enter Item# Or Name: ","combination")

                if itprem.isdigit():
                    if int(itprem) in itemchglist:
                        itp = itemchglist.get(int(itprem))
                        print(f"Modify {itp.item_name} ... in Cart ...")
                        return itp
                    else:
                        print(f" Item#{itprem} NOT FOUND in cart or is INVALID. ")
                else:
                    itpfound = False
                    for key, itpobj in itemchglist.items():
                        if itpobj.item_name == itprem:
                            itp = itemchglist.get(key)
                            itpfound=True                           
                            break                       
                    if itpfound == True:
                        print(f"Modify {itp.item_name} ... in Cart ...")                       
                        return itp
                    else:
                        print(f" Item#{itprem} NOT FOUND in cart or is INVALID. ")
                    
    except Exception as e:
        print(f"An error occurred within func-inventoryCartItems(): {e}. Exiting program.") # print out the error
        sys.exit() 

def createShoppingCart(): # Function for instantiation of the ITP object 
    try:        
        itemname = requeststrinput("Enter the purchase item name: ",False)
        itemprice = requestnumericinput(f"Enter the price for {itemname}: $",True)
        itemquantity = requestnumericinput(f"Enter the Quantity for {itemname}: #",False)
        itemdescription = requeststrinput(f"Enter the description of the item: ",False)
        itemobj = ItemToPurchase(itemname, float(itemprice), int(itemquantity),itemdescription) #create the itp object
        
        return itemobj
    except Exception as e:
        print(f"An error occurred within func-createShoppingCart(): {e}. Exiting program.") # print out the error
        sys.exit() 

def modifyShoppingCart(ItemToPurchase): # Function for modifying the ITP object attributes
    try:        
        print(f" Let's change the purchase details for Item {ItemToPurchase.item_name} ")
        itemprice = requestnumericinput(f"Enter the price for {ItemToPurchase.item_name} was ${float(ItemToPurchase.item_price)}: $",True)
        itemquantity = requestnumericinput(f"Enter the Quantity for {ItemToPurchase.item_name} was {int(ItemToPurchase.item_quantity)}: #",False)
        itemdescription = requeststrinput(f"Reenter the Description of {ItemToPurchase.item_name} was {ItemToPurchase.item_description} :",False)
        ItemToPurchase.item_price=float(itemprice)
        ItemToPurchase.item_quantity=int(itemquantity)
        ItemToPurchase.item_description=itemdescription
        
        print("Thanks! Your item "+ItemToPurchase.item_name+" has been updated! ")
        return ItemToPurchase
    except Exception as e:
        print(f"An error occurred within func-modifyShoppingCart(): {e}. Exiting program.") # print out the error
        sys.exit() 

##################### program main ##################################################
cart_items = [] #define cart items list
menuoptions = ["a","r","c","i","o","q"] #define valid menu options

class ShoppingCart: #Defines the new ShoppingCart class
    def __init__(self, customer_name, current_date, cart): #constructor for class object with 3 attributes
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart

    def add_item(self,ItemToPurchase):
        #Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
        print("adding item...")
        cart_items.append(ItemToPurchase)
                            
    def remove_item(self,ItemToPurchase):
        #Removes item from cart_items list. Has a string items name parameter. - Outputs "Item not found in cart" if unfound
        print("removing item...")
        cart_items.remove(ItemToPurchase)
                
    def modify_item(self,ItemToPurchase):
        #Modifies the attributes of ITP - if unfound - "Item not found found in cart"
        print("modifying item...")
        upditp = modifyShoppingCart(ItemToPurchase)
                           
    def get_num_items_in_cart(self):
        #Returns quantity of all items in cart - cart_items[]
        return len(cart_items)
            
    def get_cost_of_cart(self):
        #determines and returns total cost of items in cart.
        totalcost = 0
        for itp in cart_items:
           totalcost = totalcost+ (itp.item_price*itp.item_quantity)
        return round(totalcost)
                            
    def print_total(self):
        #Prints or outputs total ob all items in cart
        print("********************OUTPUT SHOPPING CART********************")       
        print(f"{self.customer_name.upper()}'s Shopping Cart - {self.current_date.upper()}")        
        print(f"Number of Items: {self.get_num_items_in_cart()}") 
        for itp in cart_items:
            print(f"{itp.item_name} {itp.item_quantity} @ ${itp.item_price} = ${(itp.item_price*itp.item_quantity)}")
        print(f"YOUR Total: ${self.get_cost_of_cart()}") 
        print("********************THANK YOU********************")
        """OUTPUT SHOPPING CART
        John Doe's Shopping Cart - February 1, 2020
        Number of Items: 8
        Nike Romaleos 2 @ $189 = $378
        Chocolate Chips 5 @ $3 = $15
        Powerbeats 2 Headphones 1 @ $128 = $128
        Total: $521
        """                  
    def print_description(self):
        #Prints each items description 
        
        print(f"{self.customer_name.upper()}'s Shopping Cart - {self.current_date.upper()}")
        print("Item Descriptions")
        for itp in cart_items:
            print(f"{itp.item_name} : {itp.item_description}")
            
        """John Doe's Shopping Cart - February 1, 2020
        Item Descriptions
        Nike Romaleos: Volt color, Weightlifting shoes
        Chocolate Chips: Semi-sweet
        Powerbeats 2 Headphones: Bluetooth headphones

        """        

class ItemToPurchase: #Item to purchase - class
  def __init__(self, item_name, item_price, item_quantity, item_description): #constructor for class object with 4 attributes, including item_description
    self.item_name = item_name
    self.item_price = item_price
    self.item_quantity = item_quantity
    self.item_description = item_description

print("*******************************************************************************")
print(f"!!Welcome to Python-Snakey Online Shopping Cart!! Today is {current_date.upper()}!!!")
customername = requeststrinput("Please enter your Name: ",False)
customerdate = requeststrinput("Please enter date (e.g., July 17 2025) :","date") 
customercart = ShoppingCart(customername, customerdate, cart_items) #initialized the customer cart object 
      
if __name__ ==  '__main__': print_menu() #calling the main - mainprog to run

#####################program end ####################################
