"""
SISTEMA DE Gestión de estudiantes El sistema debe permitir:
FEATURES:
• Registrar nuevos estudiantes. (• ID (identificador único), Nombre, Edad, curso/programa, Estado (activo/inactivo))
• Consultar la lista de estudiantes.
• Buscar un estudiante por algún criterio (ej. ID o nombre).
• Actualizar la información de un estudiante.
• Eliminar estudiantes.

"""
# IMPORT other modules
from validations import name_validation, id_validation, age_validation, program_validation,status_validation
import os
import csv 



# Funtion to add a new student, with all the information, and returns in a dictionary to keep that information.

def add_student():
    student_name = name_validation()
    student_id= id_validation()
    student_age= age_validation()
    program = program_validation()
    status= status_validation()
    return {
        "name" : student_name,
        "id": student_id,
        "age": student_age,
        "course/program": program,
        "active/inactive": status
    }
# Defined ride for csv file
DATA_FOLDER= "data"
FILE_CSV = os.path.join(DATA_FOLDER,"students.csv")

# Funtion to create a folder if it does not exists
def create_folder():
    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

# Funtion to watch the student list, we can enumarate a list an show the information in order
# Or we can keep the information in a CVS format and read it.
def read_students():
    if not os.path.exists(FILE_CSV): #Here we vefified if the file actually exists, if dont, it is gonna be created
        return [] # It returns an emphty list
    with open(FILE_CSV, 'r', newline='', encoding= 'utf-8') as file:
        read= csv.DictReader(file)
        return list(read)
        
# Funtion to register a student
def register_students(register):
    create_folder() #Invoke the funtion create folder in case it does not exists
    file_existance= os.path.exists(FILE_CSV) # to verified the existance of the file
    with open(FILE_CSV, 'a', newline='', encoding= 'utf-8') as file: # Here we use append mode to append information to an existance file, not overwrite
        write= csv.DictWriter(file, fieldnames= ["name", "id", "age", "course/program", "active/inactive"])
        if not file_existance:
            write.writeheader()
        write.writerow(register) #this writes a new row on the end of the file

# Funtion for look for an specific student based on something(ex: ID, name)
def student_info(id_s, id):
    information= read_students()
    for student in information:
        if student.get(id)== str(id_s):
            print(f"Name: {student["name"]}, ID: {student["id"]}, Age: {student["age"]}, Course/program: {student["course/program"]}, Active/Inactive: {student["active/inactive"]}")
                
# FUntion for update a student's information

def update_student(id_s, id, new_data):
    information = read_students()
    if len(information) == 0:
        print("\n||---This file is emphty---||")
        return False
    updated = False
    for inf in information:
        if inf.get(id)== str(id_s): #method for search a value from a specific key and validates the existance of the value and the code is comparing it
            inf.update(new_data) #method for update a dictionary
            updated = True
            break
    if updated: #If it is not updated then... overwrite
        with open(FILE_CSV, 'w', newline='', encoding= 'utf-8') as file: #here we use the write mode, to overwrite and uptade the infrmation of a student.
            write= csv.DictWriter(file, fieldnames= information[0].keys()) #this method is used for take the keys from the first opsition of the dictionary
            write.writeheader()
            write.writerows(information)
    return updated 

# Funtion for delete a student
def delete_student(id_s, id):
    information = read_students()
    if len(information) == 0:
        print("\n||---This file is emphty---||")
        return False
    new_information= [] #This list save the rest of data when one student is eliminated
    deleted = False
    for inf in information:
        if inf.get(id)== str(id_s): #method for search a value from a specific key and validates the existance of the value
            deleted= True
        else:
            new_information.append(inf)
    
    with open(FILE_CSV, 'w', newline='', encoding= 'utf-8') as file: 
        write= csv.DictWriter(file, fieldnames= information[0].keys()) 
        write.writeheader()
        write.writerows(new_information)
    
    if deleted == False:
        print("Not founded")


