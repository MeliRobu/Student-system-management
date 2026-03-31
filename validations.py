
# Funtion for validate a student name
def name_validation():
    name = input("\nWhat is the student's name?: ")
    if name.isalpha():
        return name
    else:
        print("\n!...Hey! You may type ONLY a name, please try again....!")
        return name_validation()

# Funtion for validate a student's ID
def id_validation():
    try: 
        identity = int(input("\nType the student's ID: "))
        return identity
    except ValueError:
        print("\n!....Hey! You may type the ID number, without blank spaces....!")
        return id_validation()
    
# Funtion for validate the student's age
def age_validation():
    try: 
        age = int(input("\nType the student's age: "))
        return age
    except ValueError:
        print("\n!....Hey! You may type the number AGE....!")
        return age_validation()

# Funtion for validate the course or program
def program_validation():
    program = input("\nWhat is the student's course or program?: ")
    if program.isalpha():
        return program
    else:
        print("\n!...Hey! You may type ONLY a name, please try again....!")
        return program_validation()

# Funtion for validate student's status

def status_validation():
    status= input("Student status, type A (active) or I (inactive): ").upper()
    if status == "A" or status == "I":
        return status
    else: 
        print("!....You may insert ONLY  'A' or 'I'....!")
        return status_validation()

# Funtion for validates the menu option
def menu_validation():
    try:
        option= int(input("Please select a number from the menu: "))
        if 0 < option <=6:
            return option
        else:
            print("!...Not a valid option, try again....!")
    except ValueError:
        print("\n!...You have to type ONLY a number, try again...!")
        return menu_validation()





#Testing area
"""for i in range(5):
    status_validation()"""
