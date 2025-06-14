import sys

def mainprog(): # Defined function name mainprog
       
    try:
        print("Welcome to Python Program!")
        user_input = input("Press enter to continue or Type Q to quit! ")
        if user_input == 'Q':
            print("Exiting program...Thank you!")
            sys.exit() # Exit gracefully
        else:
            print("Let\'s start this Python Program!")
            inputnum1 = input("Enter number 1: ")
            checkinginputval = True
            while checkinginputval:
                if inputnum1.isdigit():
                    num1 = int(inputnum1)
                    checkinginputval=False
                    break
                else:
                    print(inputnum1+" is not a number")
                    inputnum1 = input("Enter number 1: ")
            
            inputnum2 = input("Enter number 2: ")
            checkinginputval2 = True
            while checkinginputval2:
                if inputnum2.isdigit():
                    num2 = int(inputnum2)                    
                    if(num2>0):
                        checkinginputval2=False
                        break
                    else:
                        print(inputnum2+" can not be zero!")
                        inputnum2 = input("Enter number 2: ")  
                else:
                    print(inputnum2+" is not a number")
                    inputnum2 = input("Enter number 2: ")
             
            print("You have entered "+inputnum1 +" and "+inputnum2)
            multipnum = num1*num2
            dividnum = num1/num2
            print("when multiplying them together, "+ inputnum1+"x"+ inputnum2 +"="+ str(multipnum) )
            print("when dividing them, "+ inputnum1+"-"+ inputnum2 +"/"+ str(dividnum) )
            input("Press enter to continue...")
            mainprog()  # Unless user explicitly exits the program would return
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Exiting program...")
        sys.exit() # Exit out from exception

mainprog() # calling mainprog and running until exit


