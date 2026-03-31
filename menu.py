from validations import menu_validation, id_validation
from services import add_student, read_students, register_students, update_student, delete_student, student_info

# Welcome message that initialize the whole program
print("\n\t ------------------------------------------ ")
print("\t| WELCOME TO THE STUDENT MANAGEMENT SYSTEM |")
print("\t ------------------------------------------ ")

# Menu in a loop, that appears util the person chooses to exit.
menu = True
while menu:
    print("|MENU|\n1.Add a new student\n2.Watch the student's list\n3.Update a student information\n4.Delete a student\n5.Exit")
    option= menu_validation()

#Conditions with match-case , based on the selected option from the user, its going to execute a single one
    match option:
        case 1:
            new_student = add_student()
            register_students(new_student)
        case 2:
            students_data= read_students()
            if len(students_data)== 0:
                print("\n||---There is not information yet---||")
            else:
                for student in students_data:
                    print(student)
        case 3:
            print("\nTo update please type the student's ID")
            id_s = input("Type de ID of the student: ")
            new_data = add_student()
            up = update_student(id_s, "ide", new_data)
            if up:
                print("\n***Sucessfull uptade***")
            else:
                print("\nNot founded information")
        case 4:
            print("\nTo delete please type the student's ID")
            id_s = id_validation()
            deleted= delete_student(id_s, "ide")
            if deleted:
                print("\n***Sucessfull delete***")
            else:
                print("\nNot founded information")
        case 5:
            print("\n|PROCESS FINISHED|\n|--IT WAS A PLEASURE TO HELP YOU!--|")
        
        case _:
            print("\nNot a valid option, please try again")
