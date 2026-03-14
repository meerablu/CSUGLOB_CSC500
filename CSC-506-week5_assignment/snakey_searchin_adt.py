############### Heap and HT datatype program start ###################################################
import sys # import basic sys library
import time # import basic time library

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

def snakey_test_adt():
    try:
       
       whileuserunexited = exitprogram()
       """Renders the app continues           
            """
       while whileuserunexited:       
            testtype = requeststrinput("Enter 1 (for Hash table test) | 2 (for Heap, Priority Queue Test)==>","digit")
            
            if testtype == "1":
                file = "dataset_babynames.txt"
                preloaddata(file) #preloading our data which is a numbered list of baby names 130 count.
                datacount= len(babylist)
            
                simulatechaining = requeststrinput(f"Current datasize is {datacount}, to test chaining, enter a number smaller than {datacount} otherwise enter 0 ===>","")
                if simulatechaining == "0":
                    babylisthashtable = HashTable(datacount) #initialize the hash table
                else:
                    babylisthashtable = HashTable(int(simulatechaining)) #initialize the hash table with a size smaller than data count, so chaining will occur
                populatehashtable(babylisthashtable)
                print(f"Hash table size populated: {babylisthashtable.size} with Elem count= {babylisthashtable.count} ")
            
                #Now we attempt to search in the hash table - hash table search
                searchhashtable(babylisthashtable)
                wanttodelete = requeststrinput("Do you want to delete some data before continuing? Y/N: ","")
                if wanttodelete.upper() == "Y":
                    babylisthashtable= deletedatainhashtable(babylisthashtable) #we deleted something in the middle position and then gonna search again
                    print(f"Hash table size populated: {babylisthashtable.size} with Elem count= {babylisthashtable.count} ")
                    searchhashtable(babylisthashtable)                
            else:
                file = "dataset_babynames_priority.txt"
                preloaddata(file) #preloading our data which is a priority numbered list of baby names 130 count.
                  
                babylistheapqueue = MaxHeapPriorityQueue() #initialize the heap which is the priority queue adt
               
                populatemaxheap( babylistheapqueue)
                print(f"Heap size populated: {len(babylistheapqueue)} ")               
                print(f"Max node: {babylistheapqueue.peek_max().value} ")
               
                #Now we attempt to search in the Max heap using priority keys - linear search
                searchinmaxheap(babylistheapqueue)
                wanttodelete = requeststrinput("Do you want to delete some data before continuing? Y/N: ","")
                if wanttodelete.upper() == "Y":
                    #babylisthashtable= deletedatainhashtable(babylisthashtable) #we deleted something in the middle position and then gonna search again
                    #print(f"Hash table size populated: {babylisthashtable.size} with Elem count= {babylisthashtable.count} ")
                    babylistheapqueue.delete()                
                    print(f"After Deleting highest priority Baby==>> Heap size populated: {len(babylistheapqueue)} ")
                    print(f"Max node: {babylistheapqueue.peek_max().value} ")
                    searchinmaxheap(babylistheapqueue)  
            
    except Exception as e:
        print(f"An error occurred within snakey_test_adt(): {e}. Exiting program.")
        sys.exit() # system exit


def deletedatainhashtable(babylisthashtable):
    """We now populate our hash table with the baby list """
    try:
       continuedelete=True
       while continuedelete:  
           searchkey = requeststrinput("Enter the key to delete (within hash table): ","digit")
           thebaby = babylisthashtable.search(int(searchkey)).split(":")
           babydata = thebaby[0].split("=")
           print(f"Deleting {babydata[0]} is {babydata[1]} Retrieved from position {thebaby[1]} in the Hashtable.")
           babykey = babydata[0].replace("Baby#","")
           babylisthashtable.delete(int(babykey))
          
           cont = requeststrinput("Continue deleting? Y/N: ","")
           if cont.upper() != "Y":
               continuedelete=False
               return babylisthashtable    
    except Exception as e:
        print(f"An error occurred within deletedatainhashtable(): {e}. Exiting program.")
        sys.exit()


def searchinmaxheap(babylistmaxheap):
    """We now populate our hash table with the baby list """
    try:
       continuesearching=True
       searchit = 1
       timetook=0
       while continuesearching:  
           searchkey = requeststrinput("Enter your priority key# (searching within the heap where the babies are prioritized): ","digit")

           if int(searchkey) == 0 or int(searchkey)> len(babylistmaxheap):
               print(f"Invalid priority key !!")
               continue
           
           millistart =currentprinttimeinms()

           thebaby = babylistmaxheap.search(int(searchkey))
         
           print(f"Data Found! {thebaby.priori} is {thebaby.value} Retrieved from Priority Queue.")

           milliend =currentprinttimeinms()
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
        print(f"An error occurred within searchinmaxheap(): {e}. Exiting program.")
        sys.exit() 
      
def searchhashtable(babylisthashtable):
    """We now populate our hash table with the baby list """
    try:
       continuesearching=True
       searchit = 1
       timetook=0
       while continuesearching:  
           searchkey = requeststrinput("Enter your search key (searching within hash table): ","digit")

           millistart =currentprinttimeinms()

           thebaby = babylisthashtable.search(int(searchkey)).split(":")
           babydata = thebaby[0].split("=")
           if babydata[1]=="removed":
               print(f"Data Not Found! Or {babydata[0]} is removed from Hashtable.")
           else:
               print(f"Data Found! {babydata[0]} is {babydata[1]} Retrieved from index {thebaby[1]} in the Hashtable.")

           milliend =currentprinttimeinms()
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
        print(f"An error occurred within populatehashtable(): {e}. Exiting program.")
        sys.exit() 

def populatehashtable(babyhashtable):
    """We now populate our hash table with the baby list """
    try:
       for priori, value in babylist.items():
            babyhashtable.insert(priori,value) #my key is my priori from the same data set

       return babyhashtable
    except Exception as e:
        print(f"An error occurred within populatehashtable(): {e}. Exiting program.")
        sys.exit()

def populatemaxheap(babymaxheap):
    """We now populate our heap with the baby list """
    try:
       #babymaxheap = MaxHeapPriorityQueue()
       for key, value in babylist.items():
            value = value.replace("\"","").replace("\n","")                       
            babymaxheap.insert(key,value)

       return babymaxheap
    except Exception as e:
        print(f"An error occurred within populatemaxheap(): {e}. Exiting program.")
        sys.exit() 
       
def preloaddata(loadfile):
    """Preloading with a fixed simple KV data using a Python dictionary"""
    try:
       with open(loadfile, "r") as file: 
            alllines = file.readlines()
       for linebyline in alllines:
            if len(linebyline) > 0:
                lineval = linebyline.split(":")
                number=int(lineval[0])
                babyname=lineval[1].replace(",","")
                babynode = {number:babyname}
                babylist.update(babynode)            
    except Exception as e:
        print(f"An error occurred within preloaddata(): {e}. Exiting program.")
        sys.exit() # system exit
        
##################### ADT program main ##################################################

###########################Data Preload ###############################################
babylist = {}  #data source using dictionary 
#######################################################################################

###################################### Start Max Heap Priority Queue Imp ###################################

class Node2: # we are implementing chaining strategy, therefore using a Node to store our key value pairs in the linked list
    def __init__(self, priori, value):
        self.priori = priori
        self.value = value
        
    def __gt__(self,  other):
        """Define self greater-than comparison based on priority."""
        return int(self.priori) > int(other.priori)

    def __lt__(self, other):
        """Define self less-than comparison based on priority."""
        return int(self.priori) < int(other.priori)

    def __eq__(self, other):
        """Define self equals comparison based on priority."""
        equaleval = False
        return int(self.priori) == int(other.priori)
    
    def __repr__(self):
        return f"Node2(p={self.priori}, v={self.value})"
        
class MaxHeapPriorityQueue:
    def __init__(self,node=None):
        
        if node is None:
            self.maxheap = []
            return
        self.maxheap = [Node2(p, v) for (p, v) in node] #we wrap our node elements into of the max heap array 
        self._build_heap()

    def _build_heap(self):
        for i in range(len(self.maxheap)//2 - 1, -1, -1):
            self._heapify_down(i)
            
    def __len__(self):
        return len(self.maxheap)
        
    def _parent_ind(self, index):
        return (index - 1) // 2 #this is also a known formula 

    def _left_child_ind(self, index):
        return 2 * index + 1 #this is a known formulae for the priority queue for the left child

    def _right_child_ind(self, index):
        return 2 * index + 2 #this is a known formulae for the priority queue right child

    def _swap(self, i, j):
        #we take the node from index of j and put it into the arr index of i
        #we then take the old value from index of i and put it into the arr index of j 
        self.maxheap[i], self.maxheap[j] = self.maxheap[j], self.maxheap[i]

    def _heapify_up(self, index): #used as a process to maintain balance and structure of the heap after insertion
        parent_index = self._parent_ind(index)
        # Compare with parent and swap if the current element is larger, continuing until the root
        while index > 0 and self.maxheap[parent_index] < self.maxheap[index]: #i am comparing by the values of babynames in this case instead of their babynum key
            self._swap(index, parent_index) #if the current value is larger than the parent, we swap them
            index = parent_index #then we point up a step index 
            parent_index = self._parent_ind(index) #and the new parent index is gotten from the function with the known formula

    def _heapify_down(self, index): #used as a process to maintain balance and structure of the heap after deletion
        heapsize = len(self.maxheap)
        maxim = index
        left = self._left_child_ind(index)
        right = self._right_child_ind(index)

        if left < heapsize and self.maxheap[left] > self.maxheap[maxim]:
            maxim = left
        if right < heapsize and self.maxheap[right] > self.maxheap[maxim]:
            maxim = right
        if maxim != index:
            self._swap(index, maxim)
            self._heapify_down(maxim)

    def insert(self, priori, value):
        """ keeps on appending and then running heapify up to reorg the node values, keeping it balanced
        from left to right while the parents values are always going to be greater until we reach the top which should be the mmxiumum value"""
        newnode = Node2(priori,value)
        self.maxheap.append(newnode)
        # act of restoring the max heap structure, heapifying it up
        self._heapify_up(len(self.maxheap) - 1)

    def delete(self): #the delete function here for priority queue is deleting the maximum value or root node / extract_max
        if not self.maxheap:
            return None
        max_node = self.maxheap[0]
        # Replace the root with the last element
        self.maxheap[0] = self.maxheap[-1]
        self.maxheap.pop() #we swapped the max node to the position of the tail of the max heap and then we popped it from the array removing it
        self._heapify_down(0) #restoring the balance and structure of the max heap by running heapify down 
        return max_node #returning the max node 

    def peek_max(self):
        if not self.maxheap: 
            return None
        return self.maxheap[0] #because this is the priority queue with max heap, the root is the node with the greatest value or maxim

    def search(self, priori):
        """Iterates and prints the heap structure."""
        for i in range(len(self.maxheap)):
            if self.maxheap[i].priori==priori:
                babynode  = self.maxheap[i] #we found our baby and will know the name of him/her
                return babynode
        return None   
            
    def printheap(self):
        """Iterates and prints the heap structure."""
        for i in range(len(self.maxheap)):
            print(f"{self.maxheap[i].priori} {self.maxheap[i].value}")
            #print(f"Node2{i}.key: {self.maxheap[i]}", end=" | ")
            """left = self.left(i)
            right = self.right(i)
            if left < len(self.maxheap): print(f"L: {self.maxheap[left]}", end=" ")
            if right < len(self.maxheap): print(f"R: {self.maxheap[right]}", end=" ")
            print()"""


######################################End Max Heap Priority Queue Imp ###################################

######################################Start Hash Table Imp with Separate chaining ###################################
class Node: # we are implementing chaining strategy, therefore using a Node to store our key value pairs in the linked list
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class HashTable:
    def __init__(self, size=100):
        self.size = size #we set the default size to 100 , but it can be changed to demonstrate perfect and non perfect hashing
        self.arr_table = [None] * size #we initialize our array hash table with a fixed size
        self.count = 0 #keeping track of number of nodes 

    def _hash(self, key):
        """We then implement the internal hash function."""
        return hash(key) % self.size #we implement the hash function to assign the element into the array position by usign the modulo operator

    def insert(self, key, value):
        """We then implement the insert function to the hash table"""
        index = self._hash(key) #we derive the value of the index from the hash
        #print(f" K{key}={value} is stored in  Array Index==>{index}")
        if not self.arr_table[index]:
            self.arr_table[index] = Node(key, value)
            self.count=self.count+1   
        else:
            # Separate Chaining - this is our collision handling strategy since am not using linear probing
            cur = self.arr_table[index]
            while cur:
                if cur.key == key:
                    cur.value = value #if the key and the value already existed, it is a duplicate - we going to ignore and return
                    return
                if not cur.next: #the next onlooker is not available -- or weve reached the tail, so breaking from loop
                    break
                cur = cur.next #we found our kv at the linked list tail and thats where we pointing at the moment
            newnode = Node(key, value)#then we establish the new node
            newnode.next = self.arr_table[index]#we point the new nodes' next element to original found current element
            self.arr_table[index] = newnode #we then position or swap our hash table's index position with the new node where the new key has been added
            self.count=self.count+1            

    def delete(self, key):
        """When we delete elements from the hash map, we worry about its structural integrirty
        we first search for the element and then we remove it using the pointers in the linked list """
        index = self._hash(key)
        cur = self.arr_table[index] #position the cur on to the index 
        prev = None # establishing a prev node moving through the Linked list
        while cur:
            if cur.key == key:
                if prev: # if the element has a previous
                    prev.next = cur.next # we repoint the nodes accordingly skipping over the cur we to remove
                else:
                    self.arr_table[index] = cur.next # we just repoint to the index to the next in line
                
                self.count=self.count-1 #we then deduct one element node count      
                return
            prev = cur #otherwise the loop continues
            cur = cur.next # cur goes to the next with the loop                  
   
    def search(self, key):
        """Searches for the element using the key value"""
        try:
            index = self._hash(key)
            cur = self.arr_table[index]
            while cur:
                if cur.key == key:
                    #return cur
                    return str(f"Baby#{cur.key}={cur.value}:{index}") # we want to return the element in whole plus mode info to demonstrate the index position achieved with hashing
                cur = cur.next # in the event its chained , in the position we want to find the one that matches the key and return that
            return str(f"{key}=removed:")
        except KeyError as e:
            print(f"{key} is not found, something wrong {e}")
    
######################################End Hashtable Imp with chaining###################################


############### main program ###################################################
print(f"*******************************************")
print(f"Snakey's Heap and Hash table ADT - We are here to review n learn!!")
print(f"*******************************************")
if __name__ ==  '__main__': snakey_test_adt()
############### program end ###################################################

