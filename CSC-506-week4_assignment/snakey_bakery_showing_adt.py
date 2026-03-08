############### ADT program part 2 start ###################################################
import sys 
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

def currentprinttimeinms():
    try:
       milliseconds =round(time.time() * 1000 * 1000) #time function returns fraction in micro seconds 
       """1 millisecond = 1000 microsecond 
          1 second = 1000 millisecond 
          60 second = 1 minute """
       return milliseconds
    except Exception as e:
        print(f"An error occurred within currentprinttimeinms(): {e}. Exiting program.")
        sys.exit() # system exit
        
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

        
def operate_bakery(numsodo,numfoca,numbagu,batchcont_sodo,batchcont_bagu,batchcont_foca):
    try:
         print(f"********* Running Bakery***********************")
         newbreadprocessqueue = breadprocessorders_LinkedList()
         
         sodostack = bread_Stack()
         sodostack =addbread("sourdough",numsodo, newbreadprocessqueue,sodostack,batchcont_sodo,batchcont_bagu,batchcont_foca,0)

         bagustack = bread_Stack()
         bagustack =addbread("baguette",numbagu, newbreadprocessqueue,bagustack,batchcont_sodo,batchcont_bagu,batchcont_foca,0)

         focastack = bread_Stack()
         focastack =addbread("focaccia",numfoca, newbreadprocessqueue,focastack,batchcont_sodo,batchcont_bagu,batchcont_foca,0)

         print(f"TOTAL in Bread linked process Queue: {newbreadprocessqueue.size()} ")
     
         #as we added our bread in the queue --> they go into the breadorders linkedlist --> breadprocessorders_LinkedList
         #we are going to start batching the breads of their specified batch sizes 

         needmobread = True      
         while needmobread:
             needmobread = requeststrinput(f"Need to add more bread? Y/N ","")
             if needmobread.upper() != "Y":
                 needmobread = False
                 break
             sodostack =needmorebread("sourdough",sodostack, newbreadprocessqueue,batchcont_sodo,batchcont_bagu,batchcont_foca,numsodo )
             focastack =needmorebread("focaccia", focastack, newbreadprocessqueue,batchcont_sodo,batchcont_bagu,batchcont_foca,numfoca )
             bagustack =needmorebread("baguette", bagustack, newbreadprocessqueue,batchcont_sodo,batchcont_bagu,batchcont_foca,numbagu)
             
         print(f"TOTAL in Baguette processing Stack: { bagustack.size()} ")
         print(f"TOTAL in Sourdough processing Stack: { sodostack.size()} ")
         print(f"TOTAL in Focaccia processing Stack: { focastack.size()} ")

         """Added to stack means they were Proofed/Preped, Now we just bake them in Good old Queue for FIFO"""
         breadbakequeue = bread_Queue()
         for i in range(sodostack.size()):
             mysourdough =sodostack.pop()
             breadbakequeue.enqueue(mysourdough)
         
         for i in range(bagustack.size()):
             mybaguette = bagustack.pop()
             breadbakequeue.enqueue(mybaguette)
     
         for i in range(focastack.size()):
             myfocaccia = focastack.pop()
             breadbakequeue.enqueue(myfocaccia)

         print(f"Bakings in Total All Breads batch Combined: { breadbakequeue.size()}")
         breadpackers = breadpackagers_Deque()
         for i in range(breadbakequeue.size()):
             bakedbread = breadbakequeue.dequeue()
             breadpackers.addFront(bakedbread) #sell the old one first
             #print(f"===========>>>> {bakedbread} is BAKED.. now ready to Pack...")
         
         breadpackers.examine_forward()

         breadpackers.display()
         #breadpackers.display_backward()
         
         return breadpackers
          
         print(f"****************************************************")                           
    except Exception as e:
        print(f"An error occurred within func-operate_bakery(0: {e}. Exiting program.") 


def preparebread(breadtype, breadcount, batchcount, breadqueue, breadstack, breadind):
    try:
         cumulatedbatchcnt=int(breadqueue.findtype(f"{breadtype}"))

         #if my stack hadnt been pushed yet - it will be zero
         #in that case by breadcount is my cumulatedbatchcnt
         
         if int(cumulatedbatchcnt) >= int(batchcount):
             if(breadstack.size()==0):
                 breadcount =cumulatedbatchcnt
            
             for i in range(int(breadcount)):
                if(breadstack.size()==0):
                    breadnum=1
                else:
                    breadnum=breadstack.size()+1
                mycurbread = breadqueue.search(f"{breadtype}_{breadnum}")
                breadstack.push(f"{mycurbread}")
  
         #print(f"How many breads in current stack ===> {breadstack.size()} -- the last is {breadstack.peek()}")
 
    except Exception as e:
        print(f"An error occurred within preparebread(): {e}. Exiting program.")
        sys.exit() # system exit

def needmorebread(breadtype, breadstack, breadqueue,batchcont_sodo,batchcont_bagu,batchcont_foca,breadind ):
    try:
         
         addmobread = requeststrinput(f"Enter number of {breadtype} breads to bake: ","digit")
         breadstack =addbread(breadtype,addmobread, breadqueue,breadstack,batchcont_sodo,batchcont_bagu,batchcont_foca,breadind)

         return breadstack
    except Exception as e:
        print(f"An error occurred within needmorebread(): {e}. Exiting program.")
        sys.exit() # system exit

        
def addbread(breadtype,breadcount, newbreadprocessqueue,breadstack, batchcont_sodo,batchcont_bagu,batchcont_foca, breadind):
    try:
         if int(breadind) > 0:
             breadind = cumulatedbatchcnt=int(newbreadprocessqueue.findtype(f"{breadtype}"))

         #print(f"Adding number of {breadtype}s ==>> {breadcount} more , totalling to {int(breadcount)+int(breadind)}")
        
         for i in range(int(breadcount)):
                breadtoinsert = f"{breadtype}_{int(breadind)+(i+1)}"
                newbreadprocessqueue.insert(f"{breadtoinsert}")

         newbreadprocessqueue=newbreadprocessqueue     

         preparebread(breadtype, breadcount, batchcont_sodo, newbreadprocessqueue, breadstack,breadind)
         
         return breadstack   
    except Exception as e:
        print(f"An error occurred within addbread(): {e}. Exiting program.")
        sys.exit() # system exit
         

def bakery_run_business():
    try:       
       whileuserunexited = exitprogram()
       """Renders the app continues           
            """
       while whileuserunexited:       

            print("WE ARE BAKING Sourdoughs, Focacias and Baguettes !!!!")

            batchcntsourdough = requeststrinput("Enter Sourdough batch count: ","digit")
            batchcntbaguette = requeststrinput("Enter Baguette batch count: ","digit")
            batchcntfocaccia = requeststrinput("Enter Focaccia batch count: ","digit")

            """ we keep adding until the stack is overflowing with the batches to be prepared,
            we start baking using the queue and then we pack using the deque
            and when packing we examine the bread quality and we can reject some batches from the deque from the back
            
            the packing step in the deque where we can remove the bad bread from the rear, otherwise we shelf the good ones to the
            shelf to be sold -- in between the stack lets us pop the breads after proofing easily and lets us know the last number
            of the type bread from the linked list which then helps us move it into the baking queueu which is in fifo, and then dequeue them
            into the packing conveyor which is a deque allowing for front and back removals"""

            numberofsourdough = requeststrinput("Initial# of Sourdough breads to produce: ","digit")
            numberofbaguette = requeststrinput("Initial# of Baguette breads to produce: ","digit")           
            numberoffocaccia = requeststrinput("Initial# of Focaccia breads to produce: ","digit")

            tstart = currentprinttimeinms()
            packedbreadqueue = operate_bakery(numberofsourdough,numberoffocaccia,numberofbaguette,batchcntsourdough,batchcntbaguette,batchcntfocaccia)
            tend = currentprinttimeinms()
 
            if packedbreadqueue.isEmpty():
                print(f"NOTHING is READY!! Have to Redo!!")   
            else:                
                print(f"PACKAGED & GOOD Quality Bread Ready for the Shelf!! -->> {packedbreadqueue.size()} TOTAL ")            

            print(f"********************* Total time Operations: {(tend-tstart)} ms *********************")              

            print(f"********************* COMPLETE FOR PERIOD *********************")
            print(f"***************************************************************")
           
            
    except Exception as e:
        print(f"An error occurred within bakery_run_business(): {e}. Exiting program.")
        sys.exit() # system exit
        
##################### ADT part 2 program main ##################################################
        
######################################List based Queue Imp ###################################
class bread_Queue:
    def __init__(self):
        self.bread_queue = []

    def enqueue(self,bread):
        self.bread_queue.append(bread)

    def dequeue(self):
        if not len(self.bread_queue) == 0:
            bread = self.bread_queue[0]
            self.bread_queue = self.bread_queue[1:] 
            return bread
        else:
            return None

    def front(self): #same to peek
        if not len(self.bread_queue) == 0:
            bread = self.bread_queue[0]
            return bread
        else:
            return None 

    def isEmpty(self):
        if len(self.bread_queue) == 0:
            return True
        else:
            return False        

    def size(self):
        return len(self.bread_queue)
######################################End Queue Imp ###################################

######################################List based Stack Imp ###################################
class bread_Stack:
    def __init__(self):
        self.bread_stack = []

    def push(self,bread):
        print(f"Working {bread} to stack...")
        self.bread_stack.append(bread)

    def pop(self):
        if not len(self.bread_stack) == 0:
            bread = self.bread_stack.pop()
            return bread
        else:
            return None 

    def peek(self):
        toplen = len(self.bread_stack)
        if toplen == 0:
            return None
        else:
            bread = self.bread_stack[toplen-1]
            return bread
        
    def isEmpty(self):
        if len(self.bread_stack) == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.bread_stack)
######################################End Stack Imp ###################################

######################################List based Linked List Imp ###################################
class Node1:
    def __init__(self, breadwork_order=None, next=None):
        self.breadwork_order = breadwork_order 
        self.next = next

    def __str__(self):        
        return str(self.breadwork_order)
    
class breadprocessorders_LinkedList: #singly linked list
     def __init__(self):
        self.head = None # The head is None at first
    
     def insert(self, breadwork_order):
        """Adds a new order to the end of the list."""
        new_breadwork_order = Node1(breadwork_order)
        
        if self.head is None:
            self.head = new_breadwork_order #assigning the new order as the first head element
            return

        last_breadwork_order = self.head #if the list is not empty, we check the current order starting from the head as the last node        
        while last_breadwork_order.next is not None:  # while there is a next we havent found the last node order
            last_breadwork_order = last_breadwork_order.next  #we keep on moving towards the next          
        last_breadwork_order.next = new_breadwork_order 

     def delete(self, orderind):
        cur_work_order = self.head

        # the order is the head , therefore we move the pointer
        if cur_work_order and str(cur_work_order.breadwork_order) == orderind:
            self.head = cur_work_order.next
            return 
        prev_work_order = None
        while cur_work_order and str(cur_work_order.breadwork_order) != orderind:
            prev_work_order = cur_work_order
            cur_work_order = cur_work_order.next

        if cur_work_order is None:            
            return
        prev_work_order.next = cur_work_order.next
 
     def search(self,orderind):
        """searches the list and prints finds the node."""
        cur_work_order = self.head
        index = 0
        while cur_work_order:
            ordernum = str(cur_work_order.breadwork_order)
            if ordernum == orderind:
                return Node1(ordernum)
            cur_work_order = cur_work_order.next
            index=index+1
            
        print(f"Bread Order(s) ==>> {orderind} NOT Found ")
        return -1

     def findtype(self,ordertype):
        """searches the list and prints finds the type of bread."""
        cur_work_order = self.head
        index = 0
        found = 0
        while cur_work_order:
            orderref = str(cur_work_order.breadwork_order)
            if orderref.startswith(f"{ordertype}_"):
                found = found+1
            cur_work_order = cur_work_order.next
            index=index+1

        return found
            
     def display(self):
        """Traverses the order list and prints the data of each node."""
        cur_work_order = self.head
        while cur_work_order:
            orderref = str(cur_work_order.breadwork_order)
            print(f"Bread Order(s) ==>> ref: {Node1(orderref)} ")
            cur_work_order = cur_work_order.next
        
     def size(self):
        cur_work_order = self.head
        count=0
        while cur_work_order:
            count=count+1
            cur_work_order = cur_work_order.next
        return count
######################################End Linkedlist Imp ###################################

######################################List based Deque Imp ###################################
class Node2:
     def __init__(self, breadpackager=None, next=None, previous=None):
        self.breadpackager = breadpackager 
        self.next = next
        self.previous = previous

     def __str__(self):        
        return str(self.breadpackager)
    
class breadpackagers_Deque: #doubly linked list
     def __init__(self):
         self.head = None # The head is None at first
         self.tail = None #
		
     def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
     def addRear(self, breadpackager):
        new_node = Node2(breadpackager)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail		
            self.tail.next = new_node
            self.tail = new_node

     def addFront(self, breadpackager):
        new_node = Node2(breadpackager)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
	
     def removeFront(self):
        if self.isEmpty():
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.previous = None
        return removed_node

     def removeRear(self):
        if self.isEmpty():
            return None
        removed_node = self.tail
        self.tail = self.tail.previous
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return removed_node

     def size(self):
        cur_node = self.head
        count=0
        while cur_node:
            count=count+1
            cur_node = cur_node.next
        return count

     def reject_batch(self, cur_node):

        if not cur_node:
            return
        if not cur_node.previous:
            return

        """if cur_node is the tail , its previous is already one advanced element from the tail unfortunately
        because otherwise we wanted to remove from the next of tail which would mean None and this
        posed a challenge to remove the last bread batch """
        prev_node = cur_node.previous
        if prev_node.previous:
            prev_node.previous.next = cur_node
            cur_node.previous = prev_node.previous
        else:
            self.head = cur_node
            cur_node.previous = None

        #prev_node.next = None
        #prev_node.previous = None
        
    
     def examine_forward(self):
        """Traverse the list from head to tail."""
        cur_node = self.head
        ind = 0
        while cur_node:
            print(f"... {cur_node}")
            curbread = str(cur_node)[:5]
            nextbread = str(cur_node.next)[:5]
            ind = ind+1
            if curbread != nextbread:
                rejectbatch = requeststrinput(f"Accept this batch? Y/N ","")
                if rejectbatch.upper() != "Y":
                    print(f"Rejecting {curbread} batch....Last {ind} breads")                    
                    for i in range(ind):
                        if cur_node.next == None:                           
                            self.reject_batch(self.tail) #there is a bug here
                        else:
                            self.reject_batch(cur_node.next)                        
                    ind=0 #reset
                else:
                    ind=0 #reset
            #print(f"..... {cur_node} vs {cur_node.next}")
                    
            cur_node = cur_node.next

     def display_backward(self):
        """Traverse the list from head to tail."""
        cur_node = self.tail
        while cur_node:
            print(f"...{cur_node}")
            cur_node = cur_node.previous

     def display(self):
        """Traverse the list from head to tail."""
        cur_node = self.head
        while cur_node:
            print(f"ON SALE__ {cur_node}")
            cur_node = cur_node.next
            
######################################End Dequue Imp ###################################

###############main program ###################################################
print(f"*******************************************")
print(f"Welcome to Snakey ADT Bakery - We are here to learn baking !!")
print(f"*******************************************")
if __name__ ==  '__main__': bakery_run_business()
############### program end ###################################################

