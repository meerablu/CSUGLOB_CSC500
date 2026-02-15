############### datatype program start ###################################################
import sys # import basic sys library
import time

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

def wrapupcustomers(numberoftables,restauranttablestack, newcustomerinqueue, mealorders, buffertime):
    try:
            
         print(f"--->> How many open orders at the moment: {mealorders.tableorders_size()}")
         
         #we are going to remove the orders and remove them from the linklist
         #we are going to return the tables to the stack after the customer finishes eating         
         #we are going to serve the remaining customer
         mealorders.tableorders_traverse()
         #we are going to traverse meal orders and remove them one by one
         #we are going to return the table to the stack
         preoccupiedtablestofreeup = int(numberoftables)-restauranttablestack.t_size()
         for i in range( int(preoccupiedtablestofreeup)):             
             mealorders.tableorders_delete(f"order-table{i+1}") #the meal has already been served, find it by the name of order and delete
             restauranttablestack.t_append(f"Table_{i+1}")

         print(f"--->> How many Tables are available (after customer leaves): {restauranttablestack.t_size()}")
         print(f"--->> How many open orders at the moment: {mealorders.tableorders_size()}")

         print(f"--->> X How many customers still waiting  (after previous serving size): {newcustomerinqueue.c_size()}")
         if newcustomerinqueue.c_size()>0:
             serving_customer(numberoftables,restauranttablestack, newcustomerinqueue, mealorders, buffertime)
         
         
    except Exception as e:
        print(f"An error occurred within func-rwrapuptables(): {e}. Exiting program.")

def wrapuptables(numberoftables,restauranttablestack):
    try:
                    
         #we are going to return the table to the stack any open tables
         preoccupiedtablestofreeup = int(numberoftables)-restauranttablestack.t_size()
         for i in range( int(preoccupiedtablestofreeup)):             
             restauranttablestack.t_append(f"Table_{i+1}")

         print(f"--->> Total tables back: {restauranttablestack.t_size()}")
         
    except Exception as e:
        print(f"An error occurred within func-rwrapuptables(): {e}. Exiting program.")
        
def serving_customer(numberoftables,restauranttablestack, newcustomerinqueue, mealorderslinklist, buffertime):
    try:
         averageservingsize = int(int(numberoftables)* 0.6) # let us say averageservingsize of restaurant is capable of serving 60% of all tables at a time 
         print(f"Average serving size: {averageservingsize}")
         
         thereisstillwaitingcustomersinque = not newcustomerinqueue.c_isempty() # we want to check queue isempty
         print(f"Are there still customers waiting? {thereisstillwaitingcustomersinque} How many: {newcustomerinqueue.c_size()} ")
         queuecurrentsize = newcustomerinqueue.c_size() # we want to check queue size

         while thereisstillwaitingcustomersinque: 
             for i in range( int(averageservingsize)):
                 if i >0:
                    time.sleep(buffertime)  # Pauses for buffer time and then continues except for the first customer

                 if i>int(queuecurrentsize)-1: #we only serving waiting customers - smaller than capacity
                    break

                 print(f"Serving table : {i+1}") #we going to dequeue our average number of customers , and pop them with tables
                 newcustomerinqueue.c_dequeue()
                 restauranttablestack.t_pop()

                 #we going to place their orders into the linked list
                 mealorder = Node(f"order-table{i+1}")
                 mealorderslinklist.tableorders_append(mealorder)

                              
             #mealorderslinklist.tableorders_traverse()
             print(f"Size of my current order list: {mealorderslinklist.tableorders_size()}")

             remaininginque = newcustomerinqueue.c_size()
             #print(f"Remaining waiting in queue : {remaininginque}") #we going to dequeue our average number of customers
            
             print(f"--->> How many Tables are available (after previous serving size): {restauranttablestack.t_size()}")
             print(f"--->> How many customers still waiting  (after previous serving size): {newcustomerinqueue.c_size()}")

             if remaininginque==0:
                 return
             else:
                 #print(f"We still need to serve: {newcustomerinqueue.c_size()} customers")
                 return
                     
    except Exception as e:
        print(f"An error occurred within func-serving_customer(): {e}. Exiting program.")    

def run_restaurant(numberoftables,averagequeuesize,averageservingtime,averageeattime):
    try:
         print(f"********* Running Restaurant ***********************")
         print(f"Entered restaurant number of tables: {numberoftables}")
         print(f"Entered average customer queue size: {averagequeuesize}")
         print(f"Entered average serve time per customer: {averageservingtime} minutes") #roughly about how many meals are ready / hour
         print(f"Entered average eat time per customer: {averageeattime} minutes") # roughly about how much time the customer eats
         print(f"****************************************************")
         
         timetoprepare = int(averageservingtime)  #minutes for a customer
         timetoeat = int(averageeattime) # minutes for a customer
         # time to prepare and time to eat for a customer is my buffer time
         buffertime = timetoprepare+timetoeat # buffer time is amount of reasonable time to serve one customer
        
         restauranttablestack = tables_Stack()
         for i in range( int(numberoftables)):
             print(f"Set up table: {i+1}") #we going to prepare / open the business tables  
             restauranttablestack.t_append(f"Table_{i+1}")
         print(f"How many Tables are setup: {restauranttablestack.t_size()}")
         
         newcustomerinqueue = customer_Queue()           
         for i in range( int(averagequeuesize)):
             newcustomerinqueue.c_enqueue(f"customer_{i+1}")
         print(f"How many customers in Queue: {newcustomerinqueue.c_size()}")
         
         if int(numberoftables)>0: # if there are open tables we serve our customers
             mealorders = tableorders_LinkedList()  #we begin initializing the meals order linked list       
             serving_customer(numberoftables, restauranttablestack, newcustomerinqueue, mealorders, buffertime)

         wrapupcustomers(numberoftables, restauranttablestack, newcustomerinqueue, mealorders,buffertime)             
         wrapuptables(numberoftables, restauranttablestack)
                           
    except Exception as e:
        print(f"An error occurred within func-compute_restaurant(0: {e}. Exiting program.") 

def currentprinttimeinms():
    try:
       milliseconds =round(time.time() * 1000) #time function returns fraction in seconds 
       """1 millisecond = 1000 microsecond 
          1 second = 1000 millisecond 
          60 second = 1 minute """
       return milliseconds
    except Exception as e:
        print(f"An error occurred within restaurant_open_business(): {e}. Exiting program.")
        sys.exit() # system exit
def restaurant_open_business():
    try:
       
       

       whileuserunexited = exitprogram()
       """Renders the app continues           
            """
       while whileuserunexited:       
            numberoftables = requeststrinput("Enter the total number of tables: ","digit")
            averagequeuesize = requeststrinput("Enter average customers queue size during peak hours: ","digit")
            averageservingtime = requeststrinput("Enter average serve time during peak hour in minutes:" ,"digit")
            averageeattime = requeststrinput("Estimate customers eat time in minutes: ","digit")

            millistart =currentprinttimeinms()
            print(f"Current Elapse time Start: {millistart} ms")
            run_restaurant(numberoftables,averagequeuesize,averageservingtime,averageeattime)
            milliend =currentprinttimeinms()
            print(f"Current Elapse time End: {milliend} ms")
            print(f"Total time in Seconds N(M) : { int(int(milliend)-int(millistart))} milliseconds runtime_ Where N={numberoftables} M={averagequeuesize}")
            
    except Exception as e:
        print(f"An error occurred within restaurant_open_business(): {e}. Exiting program.")
        sys.exit() # system exit
        
##################### ADT program main ##################################################
        
######################################List based Queue Imp ###################################
class customer_Queue:
    def __init__(self):
        self.customer_queue = []

    def c_enqueue(self,customer):
        self.customer_queue.append(customer)

    def c_dequeue(self):
        if not len(self.customer_queue) == 0:
            customer = self.customer_queue[0]
            self.customer_queue = self.customer_queue[1:] #slicing operation to retain the queue with all customers except the one dequeued
            return customer
        else:
            return None 

    def c_isempty(self):
        if len(self.customer_queue) == 0:
            return True
        else:
            return False
        
    def c_size(self):
        return len(self.customer_queue)

######################################End Queue Imp ###################################

######################################List based Stack Imp ###################################
class tables_Stack:
    def __init__(self):
        self.tables_stack = []

    def t_append(self,table):
        self.tables_stack.append(table)

    def t_pop(self):
        if not len(self.tables_stack) == 0:
            table = self.tables_stack.pop()
            return table
        else:
            return None 

    def t_isempty(self):
        if len(self.tables_stack) == 0:
            return True
        else:
            return False
        
    def t_size(self):
        return len(self.tables_stack)

######################################End Stack Imp ###################################

######################################List based Linked List Imp ###################################
class Node:
    def __init__(self, order=None, next=None):
        self.order = order 
        self.next = next

    def __str__(self):        
        return str(self.order)
    
class tableorders_LinkedList: #singly linked list
     def __init__(self):
        self.head = None # The head is None at first
    
     def tableorders_append(self, order):
        """Adds a new order to the end of the list."""
        new_order = Node(order)
        
        if self.head is None:
            self.head = new_order #assigning the new order as the first head element
            return

        last_order = self.head #if the list is not empty, we check the current order starting from the head as the last node        
        while last_order.next is not None:  # while there is a next we havent found the last node order
            last_order = last_order.next  #we keep on moving towards the next          
        last_order.next = new_order # we are at the last node where we assign the next order's pointer


     def tableorders_delete(self, ordernum):
        """Delete the order from the linked list"""
        cur_order = self.head

        # the order is the head , therefore we move the pointer
        if cur_order and str(cur_order.order) == ordernum:
            self.head = cur_order.next
            return 
        # traversal to look for the order num and then delinking/dereferencing it from the list
        prev_order = None
        while cur_order and str(cur_order.order) != ordernum:
            prev_order = cur_order
            cur_order = cur_order.next

        # the order node is not found within the linked list
        if cur_order is None:            
            return
        # overrides the node pointers
        prev_order.next = cur_order.next
        # The order node is removed from the linked list

        
     def tableorders_traverse(self):
        """Traverses the order list and prints the data of each node."""
        cur_order = self.head
        while cur_order:
            orderref = str(cur_order.order)
            print(f"Open Order(s) ref: {orderref} ")
            cur_order = cur_order.next
        
     def tableorders_size(self):
        cur_order = self.head
        count=0
        while cur_order:
            count=count+1
            cur_order = cur_order.next
        return count

######################################End Linkedlist Imp ###################################


###############main program ###################################################
print(f"*******************************************")
print(f"WelCOme to Snakey ADT restaurant - We are here to watch performance !!")
print(f"*******************************************")
if __name__ ==  '__main__': restaurant_open_business()
############### program end ###################################################

