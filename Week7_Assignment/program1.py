#####################program start ##################
import sys

def userwishestoexit(): # generic function defined to capture program exit Q
    try:
        user_input = input("Press enter to continue or Type Q to quit! ")
        if user_input.upper() == 'Q': # if the user enters a q or Q the program ends
            print("Exiting program...Thank you!")
            sys.exit() # calling system.exit
        else:
            return True # otherwise continue with the program flow
    except Exception as e:
        print(f"An error occurred within func-userwishestoexit(): {e}. Exiting program.") 

def requeststrinput(verbiage,checktype): # generic function defined to capture string type inputs or prompts
    try:        
        inputval = input(verbiage) #actual verbiage is getting passed into the function for prompting the user
        checkinginputval = True        

        while checkinginputval:
            if inputval!="":
                if checktype=="list": #this is specially for checking valid keys which are the class names in the dictionary
                    if inputval.upper() in classroomdict.keys(): #comparing the inputval from the array menu options defined
                        return inputval  
                    else:
                        if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                            checkinginputval=False                           
                        else:
                            print(f"Sorry! You've entered {inputval} which is Invalid!") # user prompt to retry 
                            inputval = input(verbiage) #case insensitive

                elif checktype=="combination": #this method will allow digit or string
                        if inputval.isdigit():
                            return inputval  
                        else:
                            return inputval                     
                else:
                    if inputval.lower() == 'q': # if the user enters a q or Q the program ends
                        checkinginputval=False                           
                    else:
                        return inputval # this is for user entering as long as non empty string and is free to enter
            else:
                        print("Sorry! You have not entered anything yet. ") # user prompt for empty string
                        inputval = input(verbiage)
        else:
            print("Exiting program...Thank you!")
            sys.exit() # calling system.exit
                       
    except Exception as e:
        print(f"An error occurred within func-requestnumericinput(): {e}. Exiting program.") 



def print_mycourse(studentCourse): #Function to print the student's course details
    try:
        whileuserunexited = userwishestoexit()
        while whileuserunexited:
            print("*******************************************************************************")
            print(f"!!Welcome to Find My Course Program!!!")
           
            if studentCourse.student_name == "": #then the student's name is entered once via the object reference
                studentname = requeststrinput("Please enter your Name: ",False)
                studentCourse.student_name=studentname
                print(f" Welcome {studentCourse.student_name.upper()}")
            else:
                print(f"Hi {studentCourse.student_name}")

            coursename = requeststrinput("Please enter your Course Name: ","list")
            studentCourse.course_name=coursename   
            
            print(f"You've entered Course Name: {studentCourse.course_name.upper()}")

            studentCourse.print_coursedetails()
        
            print_mycourse(studentCourse)
    except Exception as e: #catch all Try/Catch blocks
        print(f"An error occurred within func-print_mycourse(): {e}. Exiting program.") 
        sys.exit()
    
##################### program main ##################################################
classroomdict = {"CSC101":"3004","CSC102":"4501","CSC103":"6755","NET110":"1244","COM241":"1411"}
instructordict = {"CSC101":"Haynes","CSC102":"Alvarado","CSC103":"Rich","NET110":"Burke","COM241":"Lee"}
scheduledict = {"CSC101":"8:00a.m.","CSC102":"9:00a.m.","CSC103":"10:00a.m.","NET110":"11:00a.m.","COM241":"1:00p.m."}

class studentCourse: #student course
  def __init__(self, student_name="", course_name=""): #constructor for class object 
    self.student_name = student_name
    self.course_name = course_name

  def print_coursedetails(self): #function does not return any values or just void
    courseroom=classroomdict.get(self.course_name.upper())
    courseinstructor=instructordict.get(self.course_name.upper())
    courseschedule=scheduledict.get(self.course_name.upper())
       
    print(f"Course Room       : {courseroom}")
    print(f"Course Instructor : {courseinstructor}")
    print(f"Course Schedule   : {courseschedule}")
        
studentcourseobj = studentCourse()    #initialized the object using the defaults              
if __name__ ==  '__main__': print_mycourse(studentcourseobj) #calling the main - mainprog to run

#####################program end ####################################
