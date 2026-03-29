############### graph program start ###################################################
import sys 
import time
import json
import math
import heapq
from datetime import datetime 
from collections import deque


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
       milliseconds =round(time.time() * 1000 * 1000) #time function returns in microseconds 
       """1 millisecond = 1000 microsecond 
          1 second = 1000 millisecond 
          60 second = 1 minute """
       return milliseconds
    except Exception as e:
        print(f"An error occurred within currentprinttimeinms(): {e}. Exiting program.")
        sys.exit() # system exit
        
def snakey_examines_data():
    try:      
       whileuserunexited = exitprogram()
       while whileuserunexited:

           testtype = requeststrinput("Enter 1 (for AdjacencyMatrix Demonstration) | 2 (for Adjacency List Demonstration) |: ","digit")
           datafile = "petownership_data_50.json" #preload our data set
           petgraphdata = preloaddata(datafile)
           
           numdatatoload = requeststrinput("Enter number of data to load, enter 5 to 50 |: ","digit") #allows the user to specify total vertices
           petgraphdata = limit_petowner_data(petgraphdata,int(numdatatoload)) #constructs the data based on normalized pet owner data
           listofPetOwners = build_pet_owners(petgraphdata)
                          
           if testtype=="1":
               graph = AdjacencyMatrixGraph()
               graph = populateAdjacencyMatrixGraph(graph,listofPetOwners)
               graph.print_graph()
               
               graph = removeVertex(graph) 
               graph = traversal(graph)
               graph = findshortestpath(graph)
               
           else:
               graph = AdjacencyListGraph()
               graph = populateAdjacencyListGraph(graph, listofPetOwners)

               graph.print_graph()
               graph = removeVertex(graph) 
               graph = traversal(graph)
               graph = findshortestpath(graph)
                        
    except Exception as e:
       print(f"An error occurred within snakey_examines_data(): {e}. Exiting program.")
       sys.exit() # system exit

######################################################################################

def findshortestpath(graph):
    try:
        continuesearching=True
        searchit = 1
        timetook=0
       
        print(f"To find the shortest path between 2 pet owners. Enter the following.")
        while continuesearching:  
            startpetid = requeststrinput("Enter the PetOwnerId to find from: Example o01 ","")
            endpetid = requeststrinput("Enter the Pet OwnerId fo find to: Example o02 ","")

            millistart =currentprinttimeinms()
            graph.shortest_path(startpetid,endpetid)
            milliend =currentprinttimeinms()
            
            timetook= timetook + int(int(milliend)-int(millistart)) #capture time it took to perform the search
            print(f"Current Elapse time: {timetook} ms")
            
            cont = requeststrinput("Continue searching? Y/N: ","")
            if cont.upper() != "Y":
               print(f"Total average time : {int(timetook/searchit)} ms ") #Average based on overall run cycles         
               continuesearching=False
               return
            else:
                searchit = searchit+1
            
        return graph          
    except Exception as e:
       print(f"An error occurred within findshortestpath(): {e}. Exiting program.")
       sys.exit() # system exit

def traversal(graph):
    try:
        typetraversal = requeststrinput("Enter 1 for BFS | 2 for DFS: ","digit")
        if typetraversal == "1":
            petid = requeststrinput("Enter the Pet ownerId: Example o01 ","")
            graph.bfs(petid)
        else:
            petid = requeststrinput("Enter the Pet ownerId: Example o01 ","")
            graph.dfs(petid)
            
        return graph          
    except Exception as e:
       print(f"An error occurred within traversal(): {e}. Exiting program.")
       sys.exit() # system exit

def removeVertex(graph):
    try:
        testremove = requeststrinput("Would you like to remove a vertex? Y/N: ","")
        if testremove.upper() == "Y":
            petid = requeststrinput("Enter the Pet ownerId: Example o01 ","")
            graph.remove_vertex(petid)
            graph.print_graph()   
        return graph          
    except Exception as e:
       print(f"An error occurred within removeVertex(): {e}. Exiting program.")
       sys.exit() # system exit
       
def populateAdjacencyListGraph(graph, listofPetOwners):
    try:
        # -------- Construct the matrix, add all vertices by owners name --------
        for owner_id, owner in listofPetOwners.items():
            #print(f"{owner_id}")
            graph.add_vertex(owner)

        # -------- Determine similarity & add non directed edges --------
        num = graph.num_vertices
        for i in range(num):
                for j in range(i + 1, num):
                    owner_a = graph.owners[i]
                    owner_b = graph.owners[j]

                    weight = graph.determine_similarity(owner_a, owner_b)
                    if weight > 0: #if weight says there is a correlation between the owners, link them 
                        graph.add_edge(i, j, weight)
        return graph
    except Exception as e:
        print(f"An error occurred within populateAdjacencyListGraph(): {e}. Exiting program.")
        sys.exit()
        
def populateAdjacencyMatrixGraph(graph, listofPetOwners):
    try:
        # -------- Construct the matrix, add all vertices by owners name --------
        for owner_id, owner in listofPetOwners.items():            
            """if owner.cats != {}:
                print(f"CATS===>  {owner.cats}")
            else:
                print(f"Does not own a Cat!!!")
            if owner.dogs != {}:
                print(f"DOGS===>  {owner.dogs}")
            else:
                print(f"Does not own a Dog!!!")"""
            graph.add_vertex(owner)

        # -------- Determine similarity & add non directed edges --------
        num = graph.num_vertices

        for i in range(num):
            for j in range(i + 1, num):  # avoid self & duplicate edges
                owner_a = graph.owners[i]
                owner_b = graph.owners[j]

                weight = graph.determine_similarity(owner_a, owner_b)
                if weight > 0: #if weight says there is a correlation between the owners, link them 
                    graph.add_edge(i, j, weight)
        return graph
    except Exception as e:
        print(f"An error occurred within populateAdjacencyMatrixGraph(): {e}. Exiting program.")
        sys.exit()
        
###########################Data set Control ###############################################

def build_pet_owners(petgraphdata):
    try:
        owners_by_id = {} #dictionary to store the pet owner data for normalizing JSON data

        for item in petgraphdata:
            oid = item.get("owner_id")
            oname = item.get("owner_name", "UNKNOWN_OWNER")

            if oid is None:
                continue
            if oid not in owners_by_id:
                owners_by_id[oid] = PetOwner(oid, oname)
                #Store PetOwner node class in owners_by_id dictionary under key oid

            owner = owners_by_id[oid] #returns the PetOwner class, reusing the oid key to the dictionary 

            pet_type = item.get("pet_type")   # "Cat" or "Dog"
            breed = item.get("breed") # the breed name of the Cat or the Dog
            count = item.get("count", 1) #the count of the cat or dog , serving as weight for the similarity graph

            if pet_type == "Cat":
                owner.add_cat(breed, count)
            elif pet_type == "Dog":
                owner.add_dog(breed, count)
        return owners_by_id #returns the list of all Unique PetOwner initialized / objects
    except Exception as e:
        print(f"An error occurred within build_pet_owners(): {e}. Exiting program.")
        sys.exit()

def limit_petowner_data(petgraphdata, numdatatoload):
    try:
        seen = set()
        loaded_ids = []

        for item in petgraphdata:
            oid = item['owner_id']
            if oid not in seen:
                seen.add(oid)
                loaded_ids.append(oid)
                if len(loaded_ids) == numdatatoload:
                    break
        select_ids = set(loaded_ids)

        limited_data = [item for item in petgraphdata if item['owner_id'] in select_ids]
        return limited_data #this carefully limits and allows us to see the graph is correctly rendered in smaller scale
    except Exception as e:
        print(f"An error occurred within limit_petowner_data(): {e}. Exiting program.")
        sys.exit()
        
###########################Data Preload ###############################################
        
def preloaddata(loadfile):
    """Preloading a simple pet ownership dataset which carries multiple relational data using built in json load into dictionary
       using this data to build the 2 relational graphs - based on similarities graph where owners x owners simulate u , v
    """
    try:
       with open(loadfile, 'r') as file:
             petownershipdata = json.load(file)    
       return petownershipdata
    except Exception as e:
        print(f"An error occurred within preloaddata(): {e}. Exiting program.")
        sys.exit() 

########################### PetOwner class ###############################################
""" Our pet owners data can each have one or more cats based on 1-6 types of cat breeds
    and they can also have one or more dogs based on 1-6 types of dog breeds
    For example, Lucy has a Samoyed and a Turkish Van, Angela has a Golden Retriever and a Turkish Van , because
    Lucy and Angela both shares ownership of at least their cats Turkish Van, being a similar breed, a connection is
    edge is marked (1). Weight in this case increases when they share both same dog, same cat breeds of at least one. For example
    if Lucy has a Samoyed and a Turkish Van, and John has a Samoyed, a Turkish Van and a Bengal cat, then Lucy and John because they both had
    a Samoyed + Turkish Ban, their connection is weighted more, and hence their Edge is weighted more. Similarity graph instead of Incidence
    graph for both my adjacency matrix and adjacency list.
"""
class PetOwner:
    def __init__(self, key_id, name):
        self.key_id = key_id # used as primary key vertex label in the graph
        self.name = name #the pet owners' name
        # Store pets as {breed: count}, separating the set of cats and dogs
        self.cats = {} #dictionary of the owenr's cats
        self.dogs = {} #dictionary of the owner's dogs

    # ---- Adds the cat to the pet owner ----
    def add_cat(self, breed, count=1):
        if breed in self.cats:
            self.cats[breed] += count
        else:
            self.cats[breed] = count

    # ---- Adds the dog to the pet owner ----
    def add_dog(self, breed, count=1):
        if breed in self.dogs:
            self.dogs[breed] += count
        else:
            self.dogs[breed] = count

    def __str__(self):
        return (f"PetOwner(id={self.key_id}, name={self.name}, "
                f"cats={self.cats}, dogs={self.dogs})")

########################Adjacency List Implementation##################################
class AdjacencyListGraph:
    def __init__(self, num_vertices=0):
        self.num_vertices = num_vertices
        self.adj_list = {vtx: set() for vtx in range(num_vertices)} #defines the key of the pet owner, to the set() initialized as empty at first
        self.owners = [None] * num_vertices  # pet owners
        self.owner_idx_by_key = {} #maps an owner keyid to the vertex index

    def add_vertex(self, pet_owner=None):
        idx = self.num_vertices
        self.adj_list[idx] = set()
        self.owners.append(pet_owner) #the pet owner is added to the list
       
        if pet_owner is not None:
            self.owner_idx_by_key[pet_owner.key_id] = idx  # maps owner key id to the vertex index for reference/lookup
        self.num_vertices += 1
        return idx
    
    def add_edge(self, u, v, weight=1):
        self.adj_list[u].add((v, weight)) #the edge is simply added bi-directionaly
        self.adj_list[v].add((u, weight)) #based on the similarity of the 2 owners, u,v and v,u - non directed graph

    def determine_similarity(self,owner_a, owner_b):
        """
        Building the similarity graph - the similarity between pet owners vs pet owners is
        weighted by them sharing similar cat breeds and or dog breeds which are the same and the weight
        is further increased if they share at least one same cat of the same breed and one dog of the same breed as well.
        """
        # Shared cats of the same breed between pet owners in relation
        shared_cats = sum(
            min(owner_a.cats.get(breed, 0), owner_b.cats.get(breed, 0))
            #when comparing a min checks to see if there is at least 1 gt 0, between the 2 owners where their cats are being checked
            for breed in owner_a.cats
        )

        # Shared dogs of the same breed between pet owners in relation
        shared_dogs = sum(
            min(owner_a.dogs.get(breed, 0), owner_b.dogs.get(breed, 0))
            #when comparing a min checks to see if there is at least 1 gt 0, between the 2 owners where their dogs are being checked
            for breed in owner_a.dogs
        )
        """ and then their edge weight based on similarity is a sum of them sharing similarly, both cats and dogs of the same breed
        """
        return shared_cats + shared_dogs

    def remove_vertex(self, key_id): 
        """ 
        We implemented the remove vertex by deleting all incident edges as a way for handling undirected symmetry.
        This saves the need to implement remove_edge() explicitly.
        """
        if key_id not in self.owner_idx_by_key:
            print(f" Owner key_id={key_id} not found")
            return

        vtx = self.owner_idx_by_key[key_id]
        for u in self.adj_list:
            self.adj_list[u] = {(nbr, w) for nbr, w in self.adj_list[u] if nbr != vtx}

        self.adj_list[vtx].clear() #removing all the edges connected to the vertex
        self.owners[vtx] = None

        del self.owner_idx_by_key[key_id]
        

    def print_graph(self):
        for idx, owner in enumerate(self.owners):
            if owner is None:
                print(f"{idx}: [removed]")

        printed = set()
        for u in range(self.num_vertices):
            if self.owners[u] is None:
                continue
            for v, weight in self.adj_list[u]:
                if (v, u) not in printed and self.owners[v] is not None:
                    print(f"{self.owners[u].key_id} ----({weight})---- {self.owners[v].key_id}")
                    printed.add((u, v))               

    def dfs(self, key_id):
        # find start index
        start = next(
            (i for i, owner in enumerate(self.owners)
             if owner is not None and owner.key_id == key_id),
            None
        )
        if start is None:
            print(f"Owner with key_id '{key_id}' not found")
            return

        visited = set() #set adt ensures uniqueness of processed vertex only once
        print("--------DFS Traversal--------")

        def dfs_visit(u):
            visited.add(u)
            print(self.owners[u].key_id, end=" ")
            for v, w in sorted(self.adj_list[u]):     
                if v not in visited and self.owners[v] is not None:
                    dfs_visit(v) #inner recursive loop
        dfs_visit(start)
        print()
    

    def bfs(self, key_id, threshold=1):
        if key_id not in self.owner_idx_by_key:
            print(f"Owner with key_id '{key_id}' not found")
            return

        start = self.owner_idx_by_key[key_id]

        # Validate the start vertex is valid
        if start not in self.adj_list or self.owners[start] is None:
            print("Invalid start vertex")
            return

        visited = set([start])
        queue = deque([start])

        print(f"--------BFS Traversal--------")
        while queue:
            u = queue.popleft()

            # print key_id (not index)
            print(self.owners[u].key_id, end=" ")

            for v, weight in sorted(self.adj_list[u]):
                if self.owners[v] is None:
                    continue
                if weight >= threshold and v not in visited:
                    visited.add(v)
                    queue.append(v)
        print()


    def shortest_path(self, start_key_id, end_key_id, threshold=1):
        """
        Dijkstra's concept.

        Similarity scores which are higher means a lower Cost which suggests the shorter path.
        Similarity to cost evaluation uses the cost formula to infer cost = 1/weight (Higher similarity = lower cost).
        """

        if start_key_id not in self.owner_idx_by_key:
            print(f"Owner with key_id '{start_key_id}' not found")
            return None
        if end_key_id not in self.owner_idx_by_key:
            print(f"Owner with key_id '{end_key_id}' not found")
            return None

        start = self.owner_idx_by_key[start_key_id] #find from key
        end = self.owner_idx_by_key[end_key_id] # to key

        if self.owners[start] is None or self.owners[end] is None:
            print("Start or end vertex has been removed")
            return None

        n = self.num_vertices #if conditions were not falsified we start here , with n
        dist = [math.inf] * n #used for storing the scores for the vertices using infinity 
        prev = [None] * n #previous node from traversal

        dist[start] = 0.0 #cost for stationary point begins with zero
        pq = [(0.0, start)]  # priority queue (distance, vertex)

        while pq: #min heap
            cur_dist, u = heapq.heappop(pq) #returns the tuple with the shortest distance

            if cur_dist != dist[u]:
                continue

            if u == end:
                break

            # check the neighbors
            for v, weight in self.adj_list[u]:
                if self.owners[v] is None:
                    continue
                if weight < threshold:
                    continue

                if weight <= 0: 
                    continue #prevent non divisible error
                cost = 1.0 / weight   # Derive similarity weight as traversal cost                
              

                alt = cur_dist + cost
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(pq, (alt, v))

        if dist[end] == math.inf:
            print(f"No path found from {start_key_id} to {end_key_id}")
            return None

        # --- Reconstruct path to key ids ---
        path_indices = []
        cur = end
        while cur is not None:
            path_indices.append(cur)
            cur = prev[cur]
        path_indices.reverse()

        path_key_ids = [self.owners[i].key_id for i in path_indices] #converts the path indices to key ids for readability

        print("Shortest Path:", " ----- ".join(path_key_ids))
        print("Total Cost:", round(dist[end], 2)) #dist end is total minimum cost to travel from start to end

        return path_key_ids, dist[end]

########################Adjacency Matrix Implementation##################################
class AdjacencyMatrixGraph:
    def __init__(self):
        self.num_vertices = 0 #becomes the total number of pet owners for similarity graph
        self.matrix = [] #the square matrix or table which will be constructed based on the list of owners
        self.owners = [] #the actual list of owners or vertices

    def add_vertex(self, pet_owner):
        self.owners.append(pet_owner)
        self.num_vertices += 1

        # Expand the matrix with the new vertex
        for row in self.matrix:
            row.append(0)

        # Add new row based onthe new vertext
        self.matrix.append([0] * self.num_vertices)
        return self.num_vertices - 1  # vertex index

    def determine_similarity(self,owner_a, owner_b):
        """
        Building the similarity graph - the similarity between pet owners vs pet owners is
        weighted by them sharing similar cat breeds and or dog breeds which are the same and the weight
        is further increased if they share at least one same cat of the same breed and one dog of the same breed as well.
        """
        # Shared cats of the same breed between pet owners in relation
        shared_cats = sum(
            min(owner_a.cats.get(breed, 0), owner_b.cats.get(breed, 0))
            for breed in owner_a.cats
        )

        # Shared dogs of the same breed between pet owners in relation
        shared_dogs = sum(
            min(owner_a.dogs.get(breed, 0), owner_b.dogs.get(breed, 0))
            for breed in owner_a.dogs
        )
        return shared_cats + shared_dogs


    def add_edge(self, u, v, weight):
        if u == v:
            return
        if u < 0 or v < 0 or u >= self.num_vertices or v >= self.num_vertices:
            print("Vertex index out of bounds")
            return

        self.matrix[u][v] = weight #undirected graph
        self.matrix[v][u] = weight

    def remove_vertex(self, key_id):
        # Find the vertex index for the given key_id
        vertex_index = None
        for idx, owner in enumerate(self.owners):
            if owner is not None and owner.key_id == key_id:
                vertex_index = idx
                break

        if vertex_index is None:
            print(f"Vertex with key_id '{key_id}' not found")
            return

        # Call the existing index-based removal
        self._remove_vertex_helper(vertex_index)

    def _remove_vertex_helper(self, vertex):
        if vertex < 0 or vertex >= self.num_vertices:
            print("Vertex not present!")
            return

        self.owners.pop(vertex)
        self.matrix.pop(vertex)

        for row in self.matrix:
            row.pop(vertex)

        self.num_vertices -= 1 #reassign the new number vertices
    
    def print_graph(self):
        # Print the matrix NxN ownersxowners similarity 
        header = [" "] + [owner.key_id for owner in self.owners]
        print("\t ".join(header))

        # Print each row with row label
        for i, row in enumerate(self.matrix):
            row_name = self.owners[i].key_id
            row_val = [str(val) for val in row]
            print(f"{row_name}\t" + "\t".join(row_val))     

    def _get_index_by_key_id(self, key_id):
        for idx, owner in enumerate(self.owners):
            if owner is not None and owner.key_id == key_id:
                return idx
        return None

    def dfs(self, key_id):
        start = self._get_index_by_key_id(key_id)
        if start is None:
            print(f"Owner with key_id '{key_id}' not found")
            return

        visited = [False] * self.num_vertices
        print(f"--------DFS Traversal--------")
        def dfs_visit(u):
            visited[u] = True
            print(self.owners[u].key_id, end=" ")

            # scan row u of adjacency matrix
            for v in range(self.num_vertices):
                if (
                    self.matrix[u][v] != 0 and
                    not visited[v] and
                    self.owners[v] is not None
                ):
                    dfs_visit(v)

        dfs_visit(start)
        print()
    
    def bfs(self, key_id):
        start = self._get_index_by_key_id(key_id)
        """ scans the graph for traversal , from the given starting element using key id
        """
        if start is None:
            print(f"Owner with key_id '{key_id}' not found")
            return

        visited = [False] * self.num_vertices
        
        queue = deque([start]) #it uses a queue to track all the visited elements in the graph
        visited[start] = True

        print(f"--------BFS Traversal--------")

        while queue:
            u = queue.popleft()
            print(self.owners[u].key_id, end=" ")

            # scan row u of adjacency matrix
            for v in range(self.num_vertices):
                if (
                    self.matrix[u][v] != 0 and
                    not visited[v] and
                    self.owners[v] is not None
                ):
                    """
                    For each connected element with edge, which has not yet been visited, and not removed, the function marks it as visited and adds it to the queue
                    """
                    visited[v] = True
                    queue.append(v)

        print()

    
    def shortest_path(self, start_key_id, end_key_id):
        start = self._get_index_by_key_id(start_key_id)
        end = self._get_index_by_key_id(end_key_id)

        if start is None or end is None:
            print("Invalid start or end vertex")
            return

        n = self.num_vertices
        dist = [math.inf] * n
        prev = [None] * n
        visited = [False] * n

        dist[start] = 0

        for _ in range(n):
            # select vertex with smallest distance
            u = min(
                (i for i in range(n) if not visited[i]),
                key=lambda i: dist[i],
                default=None
            )

            if u is None or dist[u] == math.inf:
                break

            visited[u] = True

            for v in range(n):
                weight = self.matrix[u][v]
                if weight > 0 and not visited[v]:
                    cost = 1 / weight #formula to derive cost by weight
                    alt = dist[u] + cost
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u

        if dist[end] == math.inf:
            print("No path found")
            return

        path = []
        cur = end
        while cur is not None:
            path.append(self.owners[cur].key_id)
            cur = prev[cur]
        path.reverse()

        print("Shortest Path:", " ----- ".join(path))
        print("Total Cost:", round(dist[end], 2))
        
###############main program ###################################################
print(f"*******************************************")
print(f"WelCOme to Snakey Montaineer's Graph ADT - We are here for Pets !!")
print(f"*******************************************")
if __name__ ==  '__main__': snakey_examines_data()
############### program end ###################################################

