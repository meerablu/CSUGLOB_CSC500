############### BST datatype program start ###################################################
import sys # import basic sys library
import time # import basic time library
from datetime import datetime #import datetime because of need for dob date comparator
import json # import json library for easy preload data of various data types

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
            sys.exit()                        
    except Exception as e:
        print(f"An error occurred within func-requeststrinput(): {e}. Exiting program.")  

def currentprinttimeinms():
    try:
       milliseconds =round(time.time() * 1000 * 1000) #time function returns in microseconds 
       """1 millisecond = 1000 microsecond 
          1 second = 1000 millisecond 
          60 second = 1 minute """
       return milliseconds
    except Exception as e:
        print(f"An error occurred within currentprinttimeinms(): {e}. Exiting program.")
        sys.exit() # system exit

def snakey_plays_adt():
    try:       
       whileuserunexited = exitprogram()
       """Renders the app continues           
            """
       while whileuserunexited:       
            testtype = requeststrinput("Enter 1 (for BST Demonstration) | 2 (for Linked List Demonstration)==>","digit")
            datafile = "babies_50.json"
            babymapdata = preloadjsondata(datafile)
            """preloading our data set of all kinds of data types, string, integers, enums, float, from a JSON data file etc."""
               
            if testtype == "1":              
                baby_bst = baby_BST(0,1)
                comparedata = requeststrinput("Enter 1 (for name) | 2 (for weight) | 3 (for gender)| 4 (for dob) ==>","digit")
                """we are able to change the mapping constructs in the BST by specifying 1-4 for its BST map comparator fields/datatypes"""
                populate_bst(babymapdata,baby_bst,int(comparedata))

                print(f" Count babies in BST {baby_bst.size} ")                
                delete_babybst(baby_bst,int(comparedata))               
                print(f" Count babies in BST {baby_bst.size} ")
                showbsttree = requeststrinput("Enter 1 (for Inorder Traversal) | 2 (for Preorder Traversal) | 3 (for Postorder Traversal)| ==>","digit")
                match int(showbsttree):
                    case 1:
                        print(f"{baby_bst.inorder()}")
                    case 2:
                        print(f"{baby_bst.preorder()}")
                    case 3:
                        print(f"{baby_bst.postorder()}")
                
                search_babybst(baby_bst,int(comparedata))
                
                smallestbaby = baby_bst.findMin(baby_bst.root)
                biggestbaby = baby_bst.findMax(baby_bst.root)
                print(f"Smallest Baby is {smallestbaby.key} valued with {smallestbaby.comparedata}")
                print(f"Biggest Baby is {biggestbaby.key} valued with {biggestbaby.comparedata}")
            else:
                """we kept the linked list implementation very straight forward simple to compare search performance against
                list based map implementations vs tree based map implementations"""
                baby_linkedlist = baby_LinkedList()
                populate_bll(babymapdata,baby_linkedlist,"name")
                
                delete_babylinkedlist(baby_linkedlist)
                search_babylinkedlist(baby_linkedlist)
                                                                                  
    except Exception as e:
        print(f"An error occurred within snakey_plays_adt(): {e}. Exiting program.")
        sys.exit() 

def search_babybst(baby_bst,datacomp):
    try:
       continuesearch=True
       searchit = 1
       timetook=0
       print(f" Count babies in BST {baby_bst.size} ")    
       while continuesearch:  
          
           if datacomp == 1:   # name str
                babysearchval = requeststrinput("Enter name of baby to Search e.g. Lucy Brown ==>> ","")
                millistart =currentprinttimeinms()
                thebaby = baby_bst.search(babysearchval,datacomp)
                milliend =currentprinttimeinms()
           elif datacomp == 2: # weight float
                babysearchval = requeststrinput("Enter weight of the baby to Search e.g. Lucy Brown is 9.3 ==>> ","")
                millistart =currentprinttimeinms()
                thebaby = baby_bst.search(babysearchval,datacomp)
                milliend =currentprinttimeinms()                
           elif datacomp == 3: # gender
                print("Unsupported comparator for delete/search for right now over gender because it is binary or rather non unique")
                return baby_bst
           elif datacomp == 4: # dob
                babysearchval = requeststrinput("Enter dob of baby to Search e.g. Lucy Brown is 2024-04-28 ==>> ","")
                millistart =currentprinttimeinms()
                thebaby = baby_bst.search(babysearchval,datacomp)
                milliend =currentprinttimeinms()
           else:
                print("Unsupported comparator for delete/search")
                return baby_bst
  
           if thebaby is not None:                             
                print(
                    f"Found the Baby!! "
                    f"{thebaby.bnode.get('name')} (key={thebaby.key})"
                )                
                timetook= timetook + int(int(milliend)-int(millistart))
                print(f"Current Elapse time: {timetook} ms")
           else:
                print(f"{babysearchval} Not found!!")
                timetook= timetook + int(int(milliend)-int(millistart))
                print(f"Current Elapse time: {timetook} ms")
                     
           cont = requeststrinput("Continue searching? Y/N: ","")
           if cont.upper() != "Y":
               continuesearch=False
               print(f"Total average time : {int(timetook/searchit)} ms ")    
               return baby_bst
           else:
               searchit = searchit+1
               
    except Exception as e:
        print(f"An error occurred within search_babybst(): {e}. Exiting program.")
        sys.exit()
        
def delete_babybst(baby_bst,datacomp):
    try:
       continuedelete=True
       while continuedelete:  
          
           if datacomp == 1:   # name str
                babysearchval = requeststrinput("Enter name of baby to discharge e.g. Lucy Brown ==>> ","")
                thebaby = baby_bst.search(babysearchval,datacomp)
           elif datacomp == 2: # weight float
                babysearchval = requeststrinput("Enter weight of the baby to discharge e.g. Lucy Brown is 9.3 ==>> ","")
                thebaby = baby_bst.search(babysearchval,datacomp)
           elif datacomp == 3: # gender scope search would be too broad
                print("Unsupported comparator for delete/search for right now over gender because it is binary or rather non unique")
                return baby_bst
           elif datacomp == 4: # dob
                babysearchval = requeststrinput("Enter dob of baby to discharge e.g. Lucy Brown is 2024-04-28 ==>> ","")
                thebaby = baby_bst.search(babysearchval,datacomp)
           else:
                print("Unsupported comparator for delete/search")
                return baby_bst
  
           if thebaby is not None:                             
                print(
                    f"Found the Baby!! "
                    f"{thebaby.bnode.get('name')} (key={thebaby.key})"
                )                
                baby_bst.delete(thebaby.comparedata, thebaby.key)
           else:
                print(f"{babysearchval} Not found!!")
                     
           cont = requeststrinput("Continue ? Y/N: ","")
           if cont.upper() != "Y":
               continuedelete=False
               return baby_bst
    except Exception as e:
        print(f"An error occurred within delete_babybst(): {e}. Exiting program.")
        sys.exit()
        
def delete_babylinkedlist(baby_linkedlist):
    try:
       continuedelete=True
       while continuedelete:  
           babyname = requeststrinput("Discharge baby? e.g. Lucy Brown ==>> ","")
           thebaby = baby_linkedlist.search(babyname)

           if thebaby != -1:
                baby_linkedlist.delete(babyname)
                print(f"{thebaby.bname} is discharged!!")
                     
           cont = requeststrinput("Continue ? Y/N: ","")
           if cont.upper() != "Y":
               continuedelete=False
               return baby_linkedlist
    except Exception as e:
        print(f"An error occurred within  delete_babylinkedlist(): {e}. Exiting program.")
        sys.exit()

def search_babylinkedlist(baby_linkedlist):
    try:
       continuesearching=True
       searchit = 1
       timetook=0
       print(f" Count babies in BLL {baby_linkedlist.size()} ")
       while continuesearching:  
           babyname = requeststrinput("Enter name of your baby? e.g. Lucy Brown ==>> ","")

           millistart =currentprinttimeinms()
           thebaby = baby_linkedlist.search(babyname)           
           milliend =currentprinttimeinms()

           if thebaby != -1:
                print(f"Found {thebaby.bname}!!")
           else:
                print(f"{babyname} Not Found!")
                    
           timetook= timetook + int(int(milliend)-int(millistart))
           print(f"Current Elapse time: {timetook} ms")
            
           cont = requeststrinput("Continue searching? Y/N: ","")
           if cont.upper() != "Y":
               print(f"Total average time : {int(timetook/searchit)} ms ")          
               continuesearching=False
               return
           else:
                searchit = searchit+1       
    except Exception as e:
        print(f"An error occurred within search_babylinkedlist(): {e}. Exiting program.")
        sys.exit() # system exit

def populate_bst(babymapdata,baby_bst,comparedata):
    """We now populate our BST with the baby list """
    try:
        babycount= len(babymapdata)
        print(f"Populating Count: {babycount}")
        comparevalue = "name"
        match comparedata:
            case 1:
                comparevalue = "name"
            case 2:
                comparevalue = "weight"
            case 3:
                comparevalue = "gender"
            case 4:
                comparevalue = "dob"
            case _:
                comparevalue = "name"

        #print(f"comp value is --> {comparevalue}")
        for i in range(babycount):           
            key  = babymapdata[i]['idnum']
            baby_bst.insert(key, babymapdata[i],babymapdata[i][comparevalue],comparedata)          

        if not baby_bst.is_balanced():
            print(" Tree is not Balanced")
        else:
            print(" Tree is Balanced!!!")
        return baby_bst
    except Exception as e:
        print(f"An error occurred within populate_bst(): {e}. Exiting program.")
        sys.exit()

def populate_bll(babymapdata,baby_linkedlist,comparedata):
    """We now populate our BST with the baby list """
    try:
        babycount= len(babymapdata)
        print(f"Populating Count: {babycount}")
       
        for i in range(babycount):           
            key  = babymapdata[i]['idnum']
            baby_linkedlist.insert(babymapdata[i][comparedata])          
        return baby_linkedlist
    except Exception as e:
        print(f"An error occurred within populate_bll(): {e}. Exiting program.")
        sys.exit()

###########################Data Preload ###############################################
        
def preloadjsondata(loadfile):
    """Preloading with a simple KV dataset which carries multiple data types using built in json load into dictionary"""
    try:
       with open(loadfile, 'r') as file:
             babylistdata = json.load(file)    
       return babylistdata
    except Exception as e:
        print(f"An error occurred within preloadjsondata(): {e}. Exiting program.")
        sys.exit() 
        
######################################BST Map Imp start ###################################
class baby_Node:
    """our baby node class will have a key with the baby id; and then the value is the baby element data
       it has the left pointer and the right pointer just like the deque, except for the rule will be
       the left kid is always skinnier than the parent and the right kid, the right kid is the fatty kid
    """
  
    def __init__(self, key, bnode=None, comparedata="",datacomtype=1):
        self.key = key #this will register our baby ID#
        self.bnode = bnode #this will be our json element
        self.comparedata = comparedata #this is our signature valuation comparator field
        self.datacomtype = datacomtype #this is our signature valuation comparator field type
        self.left = None #left node
        self.right = None #right node


    def __gt__(self,  other):
        """Define self greater-than comparison for meaning of how data needs to be compared for left/right."""
        return self.comparedata > other.comparedata

    def __lt__(self, other):
        """Define self less-than comparison for meaning of how data needs to be compared for left/right."""
        return self.comparedata < other.comparedata

    def __eq__(self, other):
        """Define self equals comparison for meaning of how data needs to be compared for left/right."""
        equaleval = False
        return self.comparedata == other.comparedata
    
    def __repr__(self):
        return f"baby_Node(c={self.comparedata}, k={self.key})"
    
class baby_BST:
    def __init__(self,size,datacomtype):
        self.root = None
        self.size = 0
        self.datacomtype = 1 #default comp type is 1 is for name is for string

    def insert(self, key, bnode=None, comparedata ="", datacomtype=1):
        if datacomtype == 1:
            comparedata = str(comparedata).upper().strip()

        if self.root is None: #during insert when the root is none, then put the baby there as the root node, return
            self.root = baby_Node(key,bnode,comparedata,datacomtype)
            self.size = self.size+1
            self.key = key
            self.bnode = bnode
            self.comparedata = comparedata
            self.datacomtype = datacomtype
            return
        self._insert_recursive(self.root, key, bnode, comparedata,datacomtype)
        """otherwise the tree keeps moving to put the kid to left or right, if the kid is fatter, they are on the right"""

    def _insert_recursive(self, currootnode, key, bnode, comparedata,datacomtype):
        if datacomtype == 1:
            comparedata = str(comparedata).upper().strip()
        """well if the comparators found the same i move them from left to right"""
        if comparedata < currootnode.comparedata:
            #print(f"leftie {comparedata} < {currootnode.comparedata} ")
            if currootnode.left is None:
                currootnode.left = baby_Node(key, bnode,comparedata,datacomtype)
                self.size = self.size+1
            else:
                self._insert_recursive(currootnode.left, key, bnode,comparedata,datacomtype)
        elif comparedata > currootnode.comparedata:
            #print(f"rightie {comparedata} > {currootnode.comparedata} ")
            if currootnode.right is None:
                currootnode.right = baby_Node(key, bnode,comparedata,datacomtype)
                self.size = self.size+1
            else:
                self._insert_recursive(currootnode.right, key, bnode,comparedata,datacomtype)
        elif comparedata == currootnode.comparedata:
           
            print(f"they are sort of same should i put them left or right ??")
            """if the left spot is vacant, i put it there else i put it on the right only to maintain balance"""
            if currootnode.left is None:
                currootnode.left = baby_Node(key, bnode,comparedata,datacomtype)
                self.size = self.size+1
            elif currootnode.right is None:
                currootnode.right = baby_Node(key, bnode,comparedata,datacomtype)
                self.size = self.size+1
            else:
                self._insert_recursive(currootnode.left, key, bnode,comparedata,datacomtype) 


    def findMin(self, bnode):
        """The smallest baby in the tree is the one left most leaf."""
        while bnode.left:
            bnode = bnode.left
        return bnode #the left most leaf holds the min comparator value

    def findMax(self, bnode):
        """The largest baby in the tree is the one right most leaf."""
        while bnode.right:
            bnode = bnode.right
        return bnode #the right most leaf holds the max comparator value
    
    def _ord(self, comparedata, key): #used this to simulate a tuple based comparison for x,y
        return (comparedata, key)

    def delete(self, comparedata, key):
        self.root, deleted = self._delete(self.root, comparedata, key)
        if deleted:
            self.size = self.size- 1
            
        if not self.is_balanced():
            print(" Tree is Not Balanced")
        return deleted

    def _delete(self, curnode, comparedata, key):
        if curnode is None:
            return None, False

        target = self._ord(comparedata, key) #my target node to delete
        here = self._ord(curnode.comparedata, curnode.key) #where current position is

        if target < here:
            curnode.left, deleted = self._delete(curnode.left, comparedata, key)
            return curnode, deleted
        elif target > here:
            curnode.right, deleted = self._delete(curnode.right, comparedata, key)
            return curnode, deleted

        # --- found node to delete ---
        if curnode.left is None and curnode.right is None:
            return None, True
        if curnode.left is None:
            return curnode.right, True
        if curnode.right is None:
            return curnode.left, True

        # two children: replace with inorder successor (min in right subtree)
        succ = self.findMin(curnode.right)
        curnode.key = succ.key
        curnode.bnode = succ.bnode
        curnode.comparedata = succ.comparedata
        curnode.right, _ = self._delete(curnode.right, succ.comparedata, succ.key)
        return curnode, True

    def height(self, curnode=None):   
        """
        Computes the height of a subtree.
        Height definition is:
        - Empty tree (None) has height -1
        - Leaf node has height 0
        - Height = 1 + max(left subtree height, right subtree height)

        This function is used by the balance checker.
        """
        curnode = self.root if curnode is None else curnode
        def h(n):
            return -1 if n is None else 1 + max(h(n.left), h(n.right))
        return h(curnode)

    def is_balanced(self):# returns (balanced_bool, height) in one pass       
        """
            Detects whether the BST is height-balanced.
            A tree is considered balanced if:
            - For EVERY node in the tree,
              the height difference between its left and right subtrees is at most 1.

            IMPORTANT:
            - This function only alerts the user about the tree being imbalanced or balanced.
            - No self balancing is implemented here for the tree.
            """
        def check(n):
            if n is None:
                return True, -1
            lb, lh = check(n.left)
            if not lb:
                return False, 0
            rb, rh = check(n.right)
            if not rb:
                return False, 0
            return (abs(lh - rh) <= 1), 1 + max(lh, rh)

        balanced, _ = check(self.root)
        return balanced
    
    def search(self, comparedata, datacomtype):
        """
        we are searching our directory of babies using their respective compare data - for example its just the name field
        we search left and right and until we find it we return the baby node
        """
        
        try:
            curnode = self.root        
            while curnode:
                match datacomtype:
                    case 1: #string comparator value for names          
                        if str(comparedata).upper().strip() < str(curnode.comparedata).upper().strip():
                            curnode = curnode.left
                        elif str(comparedata).upper().strip() > str(curnode.comparedata).upper().strip():
                            curnode = curnode.right
                        else:
                            print(f" FOUND --> {curnode.bnode.get('name')} {curnode.key}")
                            return curnode  #or return curnode
                    case 2: #float comparator value for weight
                        if float(comparedata) < float(curnode.comparedata):
                            curnode = curnode.left
                        elif float(comparedata) > float(curnode.comparedata):
                            curnode = curnode.right
                        else:
                            return curnode  #or return curnode
                    case 4: #date comparator value for dob                   
                        if datetime.strptime(comparedata, "%Y-%m-%d").date() < datetime.strptime(curnode.comparedata, "%Y-%m-%d").date():
                            curnode = curnode.left
                        elif datetime.strptime(comparedata, "%Y-%m-%d").date() > datetime.strptime(curnode.comparedata, "%Y-%m-%d").date():
                            curnode = curnode.right
                        else:
                            return curnode  #or return curnode
            return None
        
        except ValueError:
            print("Invalid data being entered. Try again!")
            return None

    def inorder(self): #inorder traversals are reading from left --> root --> right 
        result = []
        self._inorder(self.root, result)
        return result 

    def _inorder(self, bnode, result):
        if bnode:
            self._inorder(bnode.left, result)
            result.append(bnode.key)
            self._inorder(bnode.right, result)

    def preorder(self): #preorder traversals are reading from root --> left ---> right 
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, bnode, result):
        if bnode:
            result.append(bnode.key)
            self._preorder(bnode.left, result)
            self._preorder(bnode.right, result)

    def postorder(self): #preorder traversals are reading from left ---> right --> root
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, bnode, result):
        if bnode:
            self._postorder(bnode.left, result)
            self._postorder(bnode.right, result)
            result.append(bnode.key)

    
######################################BST Map Imp end ###################################


######################################List based Linked List Imp ###################################
class baby_Node2:
    def __init__(self, bname=None, next=None):
        self.bname = bname
        self.next = next

    def __str__(self):        
        return str(self.bname)
    
class baby_LinkedList: #singly linked list
     def __init__(self):
        self.head = None # The head is None at first
    
     def insert(self, bname):
        """Adds a new baby to the end of the list."""
        new_bname = baby_Node2(bname)
        
        if self.head is None:
            self.head = new_bname #assigning the new baby as the first head element
            return

        last_bname= self.head #if the list is not empty, we check the current node starting from the head as the last node        
        while last_bname.next is not None:  # while there is a next we havent found the last node order
            last_bname = last_bname.next  #we keep on moving towards the next          
        last_bname.next = new_bname 

     def delete(self, babyname):
        cur_baby = self.head
        # the order is the head , therefore we move the pointer
        if cur_baby and str(cur_baby.bname.upper().strip()) == babyname.upper().strip():
            self.head = cur_baby.next
            return 
        prev_baby = None
        while cur_baby and str(cur_baby.bname.upper().strip()) != babyname.upper().strip():
            prev_baby = cur_baby
            cur_baby = cur_baby.next
        if cur_baby is None:            
            return
        prev_baby.next = cur_baby.next
 
     def search(self,bname):
        """searches the list and prints finds the node."""
        cur_baby = self.head
        index = 0
        while cur_baby:
            babyname = str(cur_baby.bname)
            if babyname.upper().strip() == bname.upper().strip():
                return baby_Node2(bname)
            cur_baby = cur_baby.next
            index=index+1  
        return -1
            
     def display(self):
        """Traverses the order list and prints the data of each node."""
        cur_baby = self.head
        while cur_baby:
            babyname = str(cur_baby.bname)
            print(f"Baby(s) ==>> : {baby_Node2(babyname)} ")
            cur_baby= cur_baby.next
        
     def size(self):
        cur_baby = self.head
        count=0
        while cur_baby:
            count=count+1
            cur_baby = cur_baby.next
        return count
######################################End Linkedlist Imp ###################################


############### main program ###################################################
print(f"*******************************************")
print(f"Snakey's BST Babies - We are here to review n learn!!")
print(f"*******************************************")
if __name__ ==  '__main__': snakey_plays_adt()
############### program end ###################################################

