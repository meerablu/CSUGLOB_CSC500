#####################program start ##################
import sys

def mainprog(): # Our function name mainprog
 
    print(f"My first cat's name is {mylovelycat1.name}. He is a {mylovelycat1.breed} and his chip# is {mylovelycat1.get_chipno()}.") 
    print(f"My second cat's name is {mylovelycat2.name}. She is a {mylovelycat2.breed} and her chip# is {mylovelycat2.get_chipno()}.")
    """ we see the other attributes are callable via getter method inline and the private attribute needs to be called from the class' defined getter method/function
    """
    try:
       print(f"My first cat's name is {mylovelycat1.name}. He is a {mylovelycat1.breed} and his chip# is {mylovelycat1.__chipno}.") #we can see it breaks here 
       print(f"My second cat's name is {mylovelycat2.name}. She is a {mylovelycat2.breed} and her chip# is {mylovelycat2.__chipno}.")
                 
    except Exception as e:
        print(f"An error occurred: {e} Exitting the program..") #and the error message says that it does not see it or in other words it is Hidden!
        sys.exit() # Exit out from exception
        
##################### program main ##################################################

class PetCat: #Defines the new ShoppingCart class
    def __init__(self, breedval, chipnoval, nameval): #constructor for class object with 3 attributes
        self.__chipno = chipnoval #__chipno is a Private attribute of the PetCat class
        self.breed = breedval #breed is a public attribute
        self.name = nameval #name is also a public attribute 

    def get_chipno(self):
        #Class' self defined getter method which is able to access the private attribute __chipno
        return self.__chipno

mylovelycat1 = PetCat("Turkish Van","456238242","babyone") #instantiated an instance of Class PetCat - cat1
mylovelycat2 = PetCat("Turkish Van","834782392","babytwo") #instantiated another instance of Class PetCat - cat2
    
if __name__ ==  '__main__': mainprog() #calling the main - mainprog to run
#####################program end ####################################
