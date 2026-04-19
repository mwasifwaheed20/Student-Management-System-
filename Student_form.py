class form:
    def __init__(self,fullname,fathername,age,qualification,email,phone_number,gender):
        self.fullname=fullname
        self.fathername=fathername
        self.age=age
        self.qualification=qualification
        self.email=email
        self.phone_number=phone_number
        self.gender=gender

students = []
def add_new_student():
    fn=input("enter the full name :")
    fathername=input("enter your father name :")
    age=int(input("enter your age :"))
    qf=input("what is your qualification:")
    while True:
        try:
            email=input("enter your email :")
            if "@" in email and "gmail.com" in email:
                break
        except:
            print("invalid email enter again ")
            continue
    while True:
        try:
            phone_number=input("enter your phone number :")
            if phone_number.isdigit() and len(phone_number)==10: #  phone number should be 10 digits because the int strips the leading zeros 
                break
        except ValueError:
            print("invalid input. Please enter a valid phone number.")
            continue
    gender=input("gender:")
    student=form(fn,fathername,age,qf,email,phone_number,gender)
    students.append(student)
    print("Student added successfully!")

def display_students():
    if not students:
        print("No students to display.")
        return
    for student in students:
        print(f"Name: {student.fullname}, Father: {student.fathername}, Age: {student.age}, Qualification: {student.qualification}, Email: {student.email}, Phone: {student.phone_number}, Gender: {student.gender}")

def search_student():
    name = input("Enter the full name to search: ")
    for student in students:
        if student.fullname.lower() == name.lower():
            print(f"Name: {student.fullname}, Father: {student.fathername}, Age: {student.age}, Qualification: {student.qualification}, Email: {student.email}, Phone: {student.phone_number}, Gender: {student.gender}")
            return
    print("Student not found.")

def update_student():
    name = input("Enter the full name to update: ")
    for student in students:
        if student.fullname.lower() == name.lower():
            print("Enter new details (leave blank to keep current):")
            fn = input(f"Full name ({student.fullname}): ") or student.fullname
            fathername = input(f"Father name ({student.fathername}): ") or student.fathername
            age = input(f"Age ({student.age}): ")
            age = int(age) if age else student.age
            qf = input(f"Qualification ({student.qualification}): ") or student.qualification
            email = input(f"Email ({student.email}): ") or student.email
            phone_number = input(f"Phone ({student.phone_number}): ")
            phone_number = int(phone_number) if phone_number else student.phone_number
            gender = input(f"Gender ({student.gender}): ") or student.gender
            student.fullname = fn
            student.fathername = fathername
            student.age = age
            student.qualification = qf
            student.email = email
            student.phone_number = phone_number
            student.gender = gender
            print("Student updated successfully!")
            return
    print("Student not found.")

def delete_student():
    name = input("Enter the full name to delete: ")
    for i, student in enumerate(students):
        if student.fullname.lower() == name.lower():
            students.pop(i)
            print("Student deleted successfully!")
            return
    print("Student not found.")

while True:
    print("\n====== MENU ======") 
    print("1. Add Student\n2. Display\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")
    selection=int(input("select one option:"))
    if selection==1:
        add_new_student()
    elif selection==2:
        display_students()
    elif selection==3:
        search_student()
    elif selection==4:
        update_student()
    elif selection==5:
        delete_student()
    elif selection==6:
        break
    else:
        print("Invalid selection. Please try again.")