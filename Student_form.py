from colorama import Fore, Style, init

init(autoreset=True)

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
    fn=input(f"{Fore.YELLOW}enter the full name :{Style.RESET_ALL}")
    fathername=input(f"{Fore.YELLOW}enter your father name :{Style.RESET_ALL}")
    age=int(input(f"{Fore.YELLOW}enter your age :{Style.RESET_ALL}"))
    qf=input(f"{Fore.YELLOW}what is your qualification:{Style.RESET_ALL}")
    while True:
        try:
            email=input(f"{Fore.YELLOW}enter your email :{Style.RESET_ALL}")
            if "@" in email and "gmail.com" in email:
                break
        except:
            print(f"{Fore.RED}invalid email enter again {Style.RESET_ALL}")
            continue
    while True:
        try:
            phone_number=input(f"{Fore.YELLOW}enter your phone number without start zero :{Style.RESET_ALL}")
            if phone_number.isdigit() and len(phone_number)==10: #  phone number should be 10 digits because the int strips the leading zeros 
                break
        except ValueError:
            print(f"{Fore.RED}invalid input. Please enter a valid phone number.{Style.RESET_ALL}")
            continue
    gender=input(f"{Fore.YELLOW}gender:{Style.RESET_ALL}")
    student=form(fn,fathername,age,qf,email,phone_number,gender)
    students.append(student)
    print(f"{Fore.GREEN}{Style.BRIGHT}Student added successfully!{Style.RESET_ALL}")

def display_students():
    if not students:
        print(f"{Fore.RED}No students to display.{Style.RESET_ALL}")
        return
    print(f"{Fore.CYAN}{Style.BRIGHT}======== STUDENT LIST ========{Style.RESET_ALL}")
    for student in students:
        print(f"{Fore.CYAN}Name: {student.fullname}, Father: {student.fathername}, Age: {student.age}, Qualification: {student.qualification}, Email: {student.email}, Phone: {student.phone_number}, Gender: {student.gender}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}=============================={Style.RESET_ALL}")

def search_student():
    name = input(f"{Fore.YELLOW}Enter the full name to search: {Style.RESET_ALL}")
    found = False
    for student in students:
        if student.fullname.lower() == name.lower():
            print(f"{Fore.GREEN}{student.fullname} found!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Name: {student.fullname}, Father: {student.fathername}, Age: {student.age}, Qualification: {student.qualification}, Email: {student.email}, Phone: {student.phone_number}, Gender: {student.gender}{Style.RESET_ALL}")
            found = True
    if not found:
        print(f"{Fore.RED}Student not found.{Style.RESET_ALL}")

def update_student():
    name = input(f"{Fore.YELLOW}Enter the full name to update: {Style.RESET_ALL}")
    for student in students:
        if student.fullname.lower() == name.lower():
            print(f"{Fore.CYAN}{Style.BRIGHT}Enter new details (leave blank to keep current):{Style.RESET_ALL}")
            fn = input(f"{Fore.YELLOW}Full name ({student.fullname}): {Style.RESET_ALL}") or student.fullname
            fathername = input(f"{Fore.YELLOW}Father name ({student.fathername}): {Style.RESET_ALL}") or student.fathername
            age = input(f"{Fore.YELLOW}Age ({student.age}): {Style.RESET_ALL}")
            age = int(age) if age else student.age
            qf = input(f"{Fore.YELLOW}Qualification ({student.qualification}): {Style.RESET_ALL}") or student.qualification
            email = input(f"{Fore.YELLOW}Email ({student.email}): {Style.RESET_ALL}") or student.email
            phone_number = input(f"{Fore.YELLOW}Phone ({student.phone_number}): {Style.RESET_ALL}")
            phone_number = int(phone_number) if phone_number else student.phone_number
            gender = input(f"{Fore.YELLOW}Gender ({student.gender}): {Style.RESET_ALL}") or student.gender
            student.fullname = fn
            student.fathername = fathername
            student.age = age
            student.qualification = qf
            student.email = email
            student.phone_number = phone_number
            student.gender = gender
            print(f"{Fore.GREEN}{Style.BRIGHT}Student updated successfully!{Style.RESET_ALL}")
            return
    print(f"{Fore.RED}Student not found.{Style.RESET_ALL}")

def delete_student():
    name = input(f"{Fore.YELLOW}Enter the full name to delete: {Style.RESET_ALL}")
    for i, student in enumerate(students):
        if student.fullname.lower() == name.lower():
            students.pop(i)
            print(f"{Fore.GREEN}{Style.BRIGHT}Student deleted successfully!{Style.RESET_ALL}")
            return
    print(f"{Fore.RED}Student not found.{Style.RESET_ALL}")

while True:
    print(f"{Fore.MAGENTA}{Style.BRIGHT}\n====== MENU ======={Style.RESET_ALL}") 
    print(f"{Fore.CYAN}1. Add Student\n2. Display\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit{Style.RESET_ALL}")
    selection=int(input(f"{Fore.YELLOW}select one option:{Style.RESET_ALL}"))
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
        print(f"{Fore.GREEN}{Style.BRIGHT}Thank you! Goodbye!{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Invalid selection. Please try again.{Style.RESET_ALL}")
