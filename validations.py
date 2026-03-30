
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
        identificator = int(input("\nType the student's ID: "))
    except ValueError:
        print("\n!....Hey! You may type the ID number, without blank spaces....!")








#Testing area
"""for i in range(5):
    id_validation()"""
