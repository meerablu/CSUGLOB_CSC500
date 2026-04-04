############### Program start ###################################
import sys 
import time
import json
import heapq
import random
from collections import deque 


def exitprogram(): # function to exit the program by typing q
    try:
        user_input = input("Press Enter to continue or Type Q to exit program! ")
        if user_input.upper() == 'Q': 
            print("Program will now exit...Thank you!")
            sys.exit() # program exit
        else:
            return True # program continues
    except Exception as e:
        print(f"An error occurred within func-exitprogram(): {e}. Exiting program.") 

def requeststrinput(verbiage,inputtype): # Generic user input function
    try:        
        inputval = input(verbiage) #verbiage passed in to prompt the user
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
                    if inputval.lower() == 'q': # program ends
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
       milliseconds =round(time.time() * 1000 * 1000) # current time in microseconds 
       """1 millisecond = 1000 microsecond 
          1 second = 1000 millisecond 
          60 second = 1 minute """
       return milliseconds
    except Exception as e:
        print(f"An error occurred within currentprinttimeinms(): {e}. Exiting program.")
        sys.exit() # system exit
        
def snakey_givepeople_foodwater():
    try:      
       whileuserunexited = exitprogram()
       while whileuserunexited:

           routegraphfile = "snakeys_routeintersections_data.json" #load our graphs with intersections
           neighborhoodroutedata = preloaddata(routegraphfile)
                             
           routegraph = AdjacencyListGraph() #initializes the routing graph, adjacency list repr
           populateAdjacencyListGraph(routegraph, neighborhoodroutedata["intersections"]) #data is populated 

           routegraph.print_graph() #prints it if necessary
           """neighborhood routes of intersections have been established, so we will now know how to locate/dispatch a house request
            for supplies to their nearest supply hub via intersections/serving as the routes mapping 
            """

           homesdatafile = "snakeys_neighborhood_data.json" #load our homes file in the neighborhood
           neighborhomesdata = preloaddata(homesdatafile) 
           supplyhubsdatafile = "snakeys_hubresources_data.json" #load our supply hubs file in the neighborhood
           neighborhoodsupplydata = preloaddata(supplyhubsdatafile)

           snakeyhouses = Houses()
           snakeyhubs = SupplyHubs()
           populate_houses_and_hubs(snakeyhouses, snakeyhubs, neighborhomesdata, neighborhoodsupplydata)
           """populate houses and hubs from data set into our hash table set dict inmplementation
           """
           
           print(f"Total Homes: {snakeyhouses.get_totalHouses()}")
           print(f"Total Supply Hubs: {snakeyhubs.get_totalHubs()}")

           #snakeyhouses.print_allHouses() #we can still print all the homes if needed
           #snakeyhubs.print_allHubs() #we can also print all hubs if needed

           requestqueue = RequestQueue() #Initializing our Tree, min heap for implementing priority queue 
           manageRequests(snakeyhouses,snakeyhubs, routegraph, requestqueue) #Record requests for homes requesting resources

           tstart = currentprinttimeinms()
           requestqueue.print_regsorted_requests(snakeyhouses) #we capture what the pq's originally sorted data
           tend = currentprinttimeinms()
           print(f"Elapse time sort: {int(tend)-int(tstart)}")

           tstart = currentprinttimeinms()
           requestqueue.print_family_only_bubblesorted_requests(snakeyhouses) #we capture bubble sorting by household count to save the largest family first regardless of urgency + distance
           tend = currentprinttimeinms()
           print(f"Elapse time bubble sort: {int(tend)-int(tstart)}")
           
           requestqueue.show_lowest_k_requests(1,snakeyhouses) # we also run quick select to derive the lowest priority req.

           service_dispatch_loop(requestqueue, snakeyhubs) #ability to mark down the requests as done as well

           tstart = currentprinttimeinms()
           requestqueue.print_regsorted_requests(snakeyhouses)
           tend = currentprinttimeinms()
           print(f"Elapse time sort: {int(tend)-int(tstart)}")

           tstart = currentprinttimeinms()
           requestqueue.print_family_only_bubblesorted_requests(snakeyhouses) #we capture bubble sorting by household count to save the largest family first regardless of urgency + distance         
           tend = currentprinttimeinms()
           print(f"Elapse time bubble sort: {int(tend)-int(tstart)}")
           
           requestqueue.show_lowest_k_requests(1,snakeyhouses)
           
           if not exitprogram():
               break                        
    except Exception as e:
       print(f"An error occurred within snakey_givepeople_foodwater(): {e}. Exiting program.")
       sys.exit() # system exit

##################### Request mgt ################################
       
def manageRequests(houses, supplyhubs,routesgraph,requestq):
     try:
       continueaddrequest=True
       while continueaddrequest:  
           raise_request(houses, supplyhubs,routesgraph, requestq)          
           cont = requeststrinput("Continue ? Y/N: ","")
           if cont.upper() != "Y":
               continueaddrequest=False               
     except Exception as e:
        print(f"An error occurred within manageRequests(): {e}. Exiting program.")
        sys.exit()

def raise_request(houses, supplyhubs, routesgraph, requestq):
    owner = requeststrinput("Enter homeowner's name e.g. Snakey Montaneer: ", "")
    houseid = None
    for hid, house in houses.houseid.items(): #for k,v in houses list
        if house.homeowner.lower() == owner.lower():
            houseid = hid
            break
    if not houseid:
        print("Can not find owner's house.")
        return

    resources, nearest = prompt_valid_resources(houseid, houses, supplyhubs, routesgraph) #function finds resources and nearest hub
    urgency = int(requeststrinput("Enter urgency (1-10): ", "digit"))

    dist, hubid, path = nearest[0] #nearest is a supply hub, returns the hashtable hub 0 which is the top nearest

    requestid = requestq.next_request_id()
    req = Request(requestid, houseid, resources, urgency, dist, hubid, path) #initialize the req object 
    requestq.add_request(req) #add it to the priority queue

    print(f"Request {requestid} created and added to queue.")
    
def service_dispatch_loop(requestqueue, hubs):
    try:
       continuedispatch=True
       while continuedispatch:  
           if not requestqueue.heap:
               print("\n No more pending requests!!")
               return
           req_input = requeststrinput("Enter RequestID to dispatch (e.g., REQ-1): ","").upper()

           dispatched = requestqueue.dispatch_request_by_id(req_input)
           if not dispatched:
               print(f" Request {req_input} not found.")
               continue

           print(f"Request {dispatched.request_id} - COMPLETED! ")

           hub = hubs.get_hub(dispatched.hub_id)
            
           cont = requeststrinput("Continue ? Y/N: ","")
           if cont.upper() != "Y":
               print("\nTotal Completed Requests:")
               for r in requestqueue.completed.values():
                   print(r) #we print out all the done requests 
               continuedispatch=False               
    except Exception as e:
       print(f"An error occurred service_dispatch_loop(): {e}. Exiting program.")
       sys.exit()


##################### Special functions - BFS, BubbleSort, QuickSelect, Memberships ###############################################

def prompt_valid_resources(houseid, houses, hubs, graph):
    while True:
        asks = requeststrinput("Enter up to 3 resources separated by commas (e.g., rice, water, medicine): ", "")
        resources = parse_resources(asks, max_items=3)

        if not resources:
            print("Please enter at least one resource.")
            continue

        nearest = find_nearest_hub_for_resources(houseid, resources, houses, hubs, graph)

        if nearest:
            # Update the hub's resources already to mark them immediately - i.e., booked resources
            dist, hubid, path = nearest[0] #hashtable returns supply hub 0 for nearest
            hub = hubs.get_hub(hubid)

            for res in resources:
                if hub.inventory.get(res, 0) <= 0:
                    print(f"Resource '{res}' not available at hub {hubid}. Try again.")
                    nearest = []
                    break

            if not nearest:
                continue

            for res in resources:
                hub.inventory[res] -= 1
                if hub.inventory[res] == 0:
                    hubs.resource_sets[hub.id].discard(res)

            print(f"Resources {resources} are AVAILABLE.")
            print(f"Nearest hub: {hubid} | Distance: {dist} | Route: {path}")
            return resources, nearest


        # Offer partial options based on requested resources that are still available
        print(f"Requested resources {resources} cannot be fulfilled together.")

        any_hubs = hubs_that_can_fulfill_any(hubs, resources)  # UNION
        if not any_hubs:
            print("None of the requested resources are available anywhere. Try different items.")
            continue

        all_hubs = hubs_that_can_fulfill_all(hubs, resources)  # applies the intersection operator
        partial_only_hubs = difference_set(any_hubs, all_hubs) # applies the difference operator

        # Show only available resources from the hubs with available routes
        available_map = {} #map dict
        for res in resources:
            hubs_for_res = hubs.hubs_with_resource(res)
            if hubs_for_res:
                filtered = intersection_set(hubs_for_res, partial_only_hubs)
                available_map[res] = filtered if filtered else hubs_for_res

        if not available_map:
            print("No ptions available. Try different items.")
            continue

        print("\nPartial fulfillment can be made with the following:")
        for res, hubset in available_map.items():
            print(f" {res} (available in hubs: {sorted(hubset)})")

        # Re-enter wanted available resources
        reasks = requeststrinput("Re-enter up to 3 resources separated by commas (choose from above): ","")
        new_asks = parse_resources(reasks, max_items=3)

        if not new_asks:
            print("Please enter at least one resource.")
            continue

        """ Trade off for applying a difference function, otherwise will allow the user to respecify other available resources
        not originally specified. """
        if not Set(new_asks).difference(Set(resources)).is_empty():
            print("Please choose only from the resources you originally requested.")
            continue        
        
        nearest2 = find_nearest_hub_for_resources(houseid, new_asks, houses, hubs, graph)
        if not nearest2:
            print(f"Those resources {new_asks} still cannot be fulfilled together. Try again.")
            continue

        dist, hubid, path = nearest2[0]
        hub = hubs.get_hub(hubid)

        for res in new_asks:
            if hub.inventory.get(res, 0) <= 0:
                print(f"Resource '{res}' just ran out at hub {hubid}. Try again.")
                nearest2 = []
                break

        if not nearest2:
            continue

        for res in new_asks:
            hub.inventory[res] -= 1
            if hub.inventory[res] == 0:
                hubs.resource_sets[hub.id].discard(res)

        print(f"\nPartial request accepted for: {new_asks}")
        print(f"Nearest hub: {hubid} | Distance: {dist} | Route: {path}")

        return new_asks, nearest2
        
def parse_resources(res, max_items=3): #only allowed up to 3 items 
    """ parses the resources requested up to 3 items separated by comma, stripped and removing of any same ones
    """
    parts = [p.strip().lower() for p in res.split(",") if p.strip()]
    dedup = []
    chkd = set()

    for p in parts:
        if p not in chkd:
            chkd.add(p)
            dedup.append(p)
    return dedup[:max_items]

def find_nearest_hub_for_resources(houseid, resources, houses, hubs, graph):
    target_intersection = houses.get_intersection(houseid) #retrieve the house' intersection using hid

    eligible_hubs = hubs_that_can_fulfill_all(hubs, resources) #find all the hubs that can fulfil the resources
    if not eligible_hubs:
        return []  # none can fulfill resource requests

    results = []
    for hubid in eligible_hubs:
        start_intersection = hubs.get_intersection(hubid)
        dist, path = graph.bfs_route_path(start_intersection, target_intersection) #find the nearest hub using eligible hubs interse , mark towards house inters.
        if dist is not None:
            results.append((dist, hubid, path)) #results return as distance, hubid, routepath

    results.sort(key=lambda x: x[0])
    return results

def hubs_that_can_fulfill_any(hubs, resources):
    any_hubs = Set()
    for r in resources:
        any_hubs = union_set(any_hubs, hubs.hubs_with_resource(r)) #making use of union_set operation to find the list of all hubs that had the resources
    return any_hubs

def hubs_that_can_fulfill_all(hubs, resources):
    if not resources:
        return Set() #for failproofing

    sets = [hubs.hubs_with_resource(r) for r in resources]
    if any(len(s) == 0 for s in sets): #if true means no hubs can fullfill all, because there is one resource which zeroed
        return Set() #return empty set

    eligible = sets[0]
    for s in sets[1:]:
        eligible = intersection_set(eligible, s) #intersection across all resource sets
    return eligible
    
def bubble_sort(arr, key):
    """bubble sorting application here to help sort our requests by slight different prioritization - family size first for instance"""
    n = len(arr)
    for i in range(n): #we run through the array elements
        swapped = False
        for j in range(0, n - i - 1): #we run through every next element for evaluation
            if key(arr[j]) > key(arr[j + 1]):
                print(f"{key(arr[j])} gt {key(arr[j + 1])} -- swapping")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                print(f"{key(arr[j])} lt {key(arr[j + 1])} -- nothing swapped")               
        if not swapped: #if nothing is swapped anymore we are done
            break

def quickselect(items, k, key=lambda x: x): #Copilot suggested using the key lambda allowing me to pass in the comparison 3-point tuples value for quick select's comparables
    if k < 0 or k >= len(items):
        raise IndexError("Index out of range")
    arr = list(items)
    def kval(x):
        v = key(x) #extracts the requests, urg,distance and ts
        return v

    left, right = 0, len(arr) - 1 #quick select initializes search range at the beginning

    while True:
        if left == right:
            return arr[left] #already found it

        pivot_index = random.randint(left, right) #the pivot index is selected at a random element instead of at normal last element
        pivot_key = kval(arr[pivot_index]) #pivot key is compared against

        # moving pivot towards the end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        store = left
        for i in range(left, right):
            if kval(arr[i]) < pivot_key:
                arr[store], arr[i] = arr[i], arr[store] #move elements smaller than the pivot to the left
                store += 1

        arr[store], arr[right] = arr[right], arr[store] #pivot arrived at its sorted position

        if k == store:
            return arr[store] #we found the side for the kth element
        elif k < store:
            right = store - 1 #its the right side, until the loop ends
        else:
            left = store + 1 #its the left side, until the loop ends

############################ Data Population Functions #################################
def populate_houses_and_hubs(houseslist, hubslist, homes_data, hubs_data):
    for h in homes_data:
        house = House(
            houseid=h["id"],
            homeowner=h["homeowner"],
            householdCount=h["householdCount"],
            address=h["address"],
            connectsToIntersection=h["connectsToIntersection"]
        )
        houseslist.add_house(house)
    hubs_list = hubs_data.get("supplyHubs", hubs_data)
   
    for d in  hubs_list:
        hub = SupplyHub(
            hubid=d["hubId"],
            name=d["name"],
            address=d["address"],
            locatedAtIntersection=d["locatedAtIntersection"],
            inventory=d["inventory"]
        )
        hubslist.add_hub(hub)
        
def populateAdjacencyListGraph(routegraph, intersections):
    try:
        for intersection, neighbors in intersections.items():
            for neighbor in neighbors:
                routegraph.add_edge(intersection, neighbor)

        return routegraph
    except Exception as e:
        print(f"An error occurred within populateAdjacencyListGraph(): {e}")
        sys.exit()


###########################Data Preload from JSON dataset ##################################     
def preloaddata(loadfile): #Preloading a simple dataset
    try:
       with open(loadfile, 'r') as file:
             jsondataset = json.load(file)    
       return jsondataset
    except Exception as e:
        print(f"An error occurred within preloaddata(): {e}. Exiting program.")
        sys.exit()

######################### Just a regular Stack implementation ##########################
class Stack:
    """Stack class to demonstrate usage and inherent characteristics (LIFO)"""
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("Invalid stack")
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

########################### Houses class and single House entity for Hashtable ########################
class House:
    def __init__(self, houseid, homeowner, householdCount, address, connectsToIntersection):
        self.houseid = houseid
        self.homeowner = homeowner
        self.householdCount = householdCount
        self.address = address
        self.connectsToIntersection = connectsToIntersection
        
class Houses:
    def __init__(self):
        self.houseid = {}              # houseid map to house
        self.address = {}              # address map to houseId
        self.intersection_by_houseid = {}         # intersection map to houseid
        self.houses_by_intersection = {}     # houses in the intersection for reverse lookup

    def add_house(self, house):
        if house.houseid in self.houseid:
            raise ValueError(f"Duplicate house id: {house.houseid}")
        if house.address in self.address:
            raise ValueError(f"Duplicate address: {house.address}")

        self.houseid[house.houseid] = house #we map the houseid to the house objectt in the dict hashtable mapping
        self.address[house.address] = house.houseid #we map the address to the houseid - so if we find by address, it returns the houseid to retrieve the house obj
        self.intersection_by_houseid[house.houseid] = house.connectsToIntersection #we map the houseid to its intersection so, bfs can use the houseid to return the house' intersection

        if house.connectsToIntersection not in self.houses_by_intersection:
            self.houses_by_intersection[house.connectsToIntersection] = set() #creates a set if the house is not there yet in the intersection
        self.houses_by_intersection[house.connectsToIntersection].add(house.houseid) #then we add the house to that intersection

    def get_house(self, houseid):
        return self.houseid[houseid]

    def get_intersection(self, houseid):
        return self.intersection_by_houseid[houseid]

    def print_allHouses(self):
        print("All Houses in the Neighborhood")
        print("--------------------------------")

        if not self.houseid:
            print("No houses yet.")
            return

        for houseid in sorted(self.houseid.keys()): #calling sorted to sort the houses list by their key is a way for displaying data in a more organized fashion
            house = self.houseid[houseid]
            print(
                f"HouseID: {house.houseid} | "
                f"Owner: {house.homeowner} | "
                f"Household Size: {house.householdCount} | "
                f"Address: {house.address} | "
                f"Intersection: {house.connectsToIntersection}"
            )
        
    def get_totalHouses(self):
        return len(self.houseid)

########################### Supply Hubs class and Supply hub single entity for Hashtable #########################
class SupplyHub:
    def __init__(self, hubid, name, address, locatedAtIntersection, inventory):
        self.id = hubid
        self.name = name
        self.address = address
        self.locatedAtIntersection = locatedAtIntersection
        self.inventory = inventory
        
class SupplyHubs:
    def __init__(self):
        self.hubid = {}                  # hubId map to supply hub
        self.intersection_by_hubid = {}     # intersection map to the hubid 
        self.hubs_by_intersection = {}   # hubs in the intersection for reverse lookup
        self.resource_sets = {}          # resources map to the hubid 

    def add_hub(self, hub):
        if hub.id in self.hubid:
            raise ValueError(f"Duplicate hub id: {hub.id}")

        self.hubid[hub.id] = hub # we map the hubid key to the supply hub value
        self.intersection_by_hubid[hub.id] = hub.locatedAtIntersection #we map that hubid to its intersection 

        if hub.locatedAtIntersection not in self.hubs_by_intersection:
            self.hubs_by_intersection[hub.locatedAtIntersection] = set() #we must create the set if the hub is the first seen in the intersection
        self.hubs_by_intersection[hub.locatedAtIntersection].add(hub.id) #then we add the hub using its hub id to the intersection

        self.resource_sets[hub.id] = Set(
            resource for resource, qty in hub.inventory.items() if qty > 0
        )

    def get_hub(self, hubid):
        return self.hubid[hubid]

    def get_intersection(self, hubid):
        return self.intersection_by_hubid[hubid]

    def hubs_with_resource(self, resource):
        result = Set()
        for hubid, resources in self.resource_sets.items():
            if resource in resources:   # works because Set implements __contains__
                result.add(hubid)
        return result

    def print_allHubs(self):
        print("All Hubs in the Neighborhood:")
        print("--------------------------------")

        if not self.hubid:
            print("No hubs loaded.")
            return

        for hubid in sorted(self.hubid.keys()):
            hub = self.hubid[hubid]
            print(
                f"HubID: {hub.id} | "
                f"Name: {hub.name} | "
                f"Address: {hub.address} | "
                f"Intersection: {hub.locatedAtIntersection}"
            )
            
    def get_totalHubs(self):
        return len(self.hubid)

###########################SET ADT Implementation ######################################
class Set:
    """ Custom Set ADT implementation, using hashtable
    """

    def __init__(self, iterable=None):
        self._data = set(iterable) if iterable is not None else set()

    def union(self, other):
        return Set(self._data | self._coerce(other))

    def intersection(self, other):
        return Set(self._data & self._coerce(other))

    def difference(self, other):
        return Set(self._data - self._coerce(other))

    def symmetric_difference(self, other):
        return Set(self._data ^ self._coerce(other))

    def add(self, item):
        self._data.add(item)

    def discard(self, item):
        self._data.discard(item)

    def is_empty(self):
        return len(self._data) == 0

    # --- Python integration for set operations ---
    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __bool__(self):
        return len(self._data) > 0

    def __repr__(self):
        return f"Set({sorted(self._data)})"

    def __or__(self, other):   # A | B
        return self.union(other)

    def __and__(self, other):  # A & B
        return self.intersection(other)

    def __sub__(self, other):  # A - B
        return self.difference(other)

    def __xor__(self, other):  # A ^ B
        return self.symmetric_difference(other)
    
    def _coerce(self, other): #function coerce ensures the different data structures are normalized for set operations
        if isinstance(other, Set):
            return other._data
        if isinstance(other, set):
            return other
        return set(other)

########################### Set Operation functions ###############################################
def _as_set(x):
    return x if isinstance(x, Set) else Set(x)

def intersection_set(a, b):
    return _as_set(a) & _as_set(b)

def union_set(a, b):
    return _as_set(a) | _as_set(b)

def difference_set(a, b):
    return _as_set(a) - _as_set(b)

def symmetric_difference_set(a, b):
    return _as_set(a) ^ _as_set(b)

########################Graph Adjacency List Implementation##################################
class AdjacencyListGraph:
    def __init__(self):
        # adjacency list: intersectionids -> set of connected intersection_ids
        self.connectedints = {}

    def _add_vertex(self, intersection):
        if intersection not in self.connectedints:
            self.connectedints[intersection] = set()
    
    def add_edge(self, intsb, intsa):
        self._add_vertex(intsb)
        self._add_vertex(intsa)
        self.connectedints[intsb].add(intsa) #undirected graphs A link B link A
        self.connectedints[intsa].add(intsb)

    def print_graph(self):
        print("Intersection Routing Graph")
        for intersection in sorted(self.connectedints.keys()):
            neighbors = sorted(self.connectedints[intersection])
            print(f"{intersection} -> {neighbors}")
        
    def bfs_route_path(self, start, target):
        if start not in self.connectedints or target not in self.connectedints:
            return None, [] #prevents runtime errors to ensure both the start point intersection and the target intersection exists in the graph

        queue = deque([start])        # Queue (BFS)
        visited = set([start])        # Set to ensure the intersection is visited only once
        parent = {start: None}        # From the start there was no path

        while queue:
            current = queue.popleft() # take oldest because in bfs the elements are always added from left to right, so the left one is how we walk

            if current == target:
                break

            for neighbor in self.connectedints[current]: #Give me the set of intersections that are directly connected to current.
                if neighbor not in visited:
                    visited.add(neighbor) #add the neighbor to visited list to ensure it wont be revisited
                    parent[neighbor] = current # moving along in the queue
                    queue.append(neighbor)  #makes it explore from this intersection later in the queue 

        if target not in parent:
            return None, []

        stack = Stack() #explicit usage of Stack ADT to satisfy the requirements for using stack 
        intersection = target #stack used here for path reconstruction

        while intersection is not None:
            stack.push(intersection) #we repush the route path intersections into the stack
            intersection = parent[intersection]  #moving target of our intersection in the while

        path = []
        while not stack.is_empty():
            path.append(stack.pop()) #LIFO reflection natural characteristics of the stack 

        distance = len(path) - 1
        return distance, path

######################### Tree Implementation PQ ##############################
class Request:
    def __init__(self, request_id, houseid, resources, urgency, distance, hubid, routepath):
        self.request_id = request_id
        self.houseid = houseid
        self.resources = resources #multiple resource items is supported per request     
        self.urgency = urgency # Lowest number means most urgent - i.e., priority 1
        self.distance = distance # shortest distance by number of route intersections
        self.hub_id = hubid # nearest eligible hub
        self.path = routepath # route for dispatch
        self.timestamp = time.time()

    def __repr__(self):
        #resources_str = ",".join(self.resources)
        return (f"Request(id={self.request_id}, house={self.houseid}, "
                f"resources={self.resources}, urgency={self.urgency}, "
                f"dist={self.distance}, hub={self.hub_id})")
        
class RequestQueue:
    def __init__(self):
        self.heap = []              # heap-based priority queue
        self.active_ids = set()     # hashtable-based set for unique active request ids
        self.completed = {}         # list to store completed requests 
        self._next_id = 1           # way to generate the next request id checking from the last id in the heap

    def next_request_id(self):
        request_id = f"REQ-{self._next_id}"
        self._next_id += 1
        return request_id

    def add_request(self, request):
        if request.request_id in self.active_ids:
            print(f"Request {request.request_id} already exists.")
            return
        heapq.heappush(
            self.heap,
            (request.urgency, request.distance, request.timestamp, request) #priority queue stores 4 elements to the heap
        )
        self.active_ids.add(request.request_id)
                
    def dispatch_request_by_id(self, request_id):
        """
        Remove a specific request from the heap by RequestID,
        mark it as completed, and maintain heap structure.
        """
        for i, (urg, dist, ts, req) in enumerate(self.heap):
            if req.request_id == request_id:
                # Remove from heap
                removed = self.heap.pop(i)
                heapq.heapify(self.heap) #re heapify tree

                # Remove from active set
                self.active_ids.discard(request_id)

                # Mark completed
                self.completed[request_id] = req

                return req  # return the dispatched Request

        return None  # not found
        
    def print_regsorted_requests(self, houses): #PQ already would have sorted the requests in order we defined , urgency then distance
        print("\nPending Requests – Priority Order")
        print("------------------------------------------------")

        if not self.heap:
            print("No pending requests.")
            return

        snapshot_sorted = sorted(self.heap)
        for urg, dist, ts, request in snapshot_sorted:
            house = houses.get_house(request.houseid)
            route_str = " -> ".join(request.path)

            print(
                f"{request.request_id} | "
                f"Urgency={urg} | "
                f"Name={house.homeowner} | "
                f"Hh-Count={house.householdCount} | "
                f"Dist={dist} | "
                f"Reso={request.resources} | "
                f"Route={route_str} | "
                f"Hub={request.hub_id}"
            )
            

    def print_family_only_bubblesorted_requests(self, houses): # bubble set sorts it by family size first , rescue the largest family first above all concept
        print("\nPending Requests – Family-Only (Hh-Count ↓ only)")
        print("------------------------------------------------")

        if not self.heap:
            print("No pending requests.")
            return

        copylist = list(self.heap)

        def family_only_key(item):
            urg, dist, ts, req = item
            hh = houses.get_house(req.houseid).householdCount #family only key based on headcounts only
            return -hh  # descending by household size

        bubble_sort(copylist, key=family_only_key) #lambda sort key by householdid count

        for urg, dist, ts, request in copylist:
            house = houses.get_house(request.houseid)
            print(
                f"{request.request_id} | "
                f"Hh-Count={house.householdCount} | "
                f"Urgency={urg} | "
                f"Dist={dist} | "
                f"Name={house.homeowner}"
            )

    def lowest_ranked_request(self, k):
        if not self.heap: #failproofing
            return None

        copylist = list(self.heap)
        n = len(copylist) #size of heap

        if k < 1 or k > n: #failproofing
            return None

        def priority_key(item):
            return (item[0], item[1], item[2]) #extracts urg, distance, timestamp
        #timestamp is just used as a tiebreaker

        kth_tuple = quickselect(
            copylist,
            n - k,          # inverted k to show reverse of what is the lowest ranking item ie. 1 is higest supposedly but, here became lowest in theory
            key=priority_key #3-valued tuple, how quickselect needs to prioritize the request            
        )
        return kth_tuple[3]  #returns the worst request object


    def show_lowest_k_requests(self, k, houses): #only for reporting purposes to show quickselect usage
        req = self.lowest_ranked_request(k)
        if req is None:
            return
        route_str = " -> ".join(req.path) if getattr(req, "path", None) else "(no route)"
        house = houses.get_house(req.houseid)
        print("\nLowest ranked requests:")
        print("------------------------------------------------")
        print(
                f"RequestID={req.request_id} | "
                f"Urgency={req.urgency} | "
                f"Name={house.homeowner} | "
                f"Dist={req.distance} | "
                f"Reso={req.resources} | "
                f"Route={route_str} | "
                f"Hub={req.hub_id}"
            )

                   
###############main program ###################################################
print(f"*******************************************")
print(f"Welcome to Snakey's ADT-filled Neighborhood - We are here to help one another Survive effectively!!")
print(f"*******************************************")
if __name__ ==  '__main__': snakey_givepeople_foodwater()
############### program end ###################################################

