from validations import menu_validation, id_validation
from services import add_student, read_students, register_students, update_student, delete_student, student_info

# Welcome message that initialize the whole program
print("\n\t ------------------------------------------ ")
print("\t| WELCOME TO THE STUDENT MANAGEMENT SYSTEM |")
print("\t ------------------------------------------ ")

# Menu in a loop, that appears util the person chooses to exit.
menu = True
while menu:
    print("|MENU|\n1.Add a new student\n2.Watch the student's list\n3.Update a student information\n4.Delete a student\n5.Look for a student\n6.Exit")
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
                for i,student in enumerate(students_data):
                    print(f"{i+1}- Name: {student["name"]}, ID: {student["id"]}, Age: {student["age"]}, Course/program: {student["course/program"]}, Active/Inactive: {student["active/inactive"]}\n")
        case 3:
            print("\nTo update please type the student's ID")
            id_s = id_validation()
            new_data = add_student()
            up = update_student(id_s, "id", new_data)
            if up:
                print("\n***Sucessfull uptade***")
            else:
                print("\nNot founded information")
        case 4:
            print("\nTo delete please type the student's ID")
            id_s = id_validation()
            deleted= delete_student(id_s, "id")
            if deleted:
                print("\n***Sucessfull delete***")
            else:
                print("\nNot founded information")
        case 5:
            print("\nTo look for a student please type the ID: ")
            id_s=id_validation()
            look_for= student_info(id_s,"id")

        case 6:
            print("\n|PROCESS FINISHED|\n|--IT WAS A PLEASURE TO HELP YOU!--|")
            menu= False
        case _:
            print("\nNot a valid option, please try again")
"""            if look_for:
                for student in look_for:
                    print(student)
                    print("\n***Student founded***")
            else:
                print("\nNot founded student")"""
