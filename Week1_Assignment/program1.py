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
            num1 = int(inputnum1)
            inputnum2 = input("Enter number 2: ")
            num2 = int(inputnum2)
            print("You have entered "+inputnum1 +" and "+inputnum2)
            addednum = num1+num2
            subdednum = num1-num2
            print("when adding them together, "+ inputnum1+"+"+ inputnum2 +"="+ str(addednum) )
            print("when subtracting them, "+ inputnum1+"-"+ inputnum2 +"="+ str(subdednum) )
            input("Press enter to continue...")
            mainprog()  # Unless user explicitly exits the program would return
    except Exception as e:
        print("An error has occurred: {e}")
        print("Exiting program...")
        sys.exit() # Exit out from exception

mainprog() # calling mainprog and running until exit


