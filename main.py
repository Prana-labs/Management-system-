import json
from abc import ABC, abstractmethod
from pathlib import Path

database = "school_data.json"
data = {"students" : [], "teacher" : []}

if Path(database).exists():
    with open(database, 'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data, f, indent=4)


class Persons(ABC):
    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def registered(self):
        pass 

    @abstractmethod
    def show_details(self):
        pass 

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False


class Student(Persons):

    def get_roles(self):
        return "student"
    
    def register(self):
        name = input("tell your name :- ")
        age = int(input("tell your age :- "))
        email = input("tell your email :- ")
        roll_no = int(input("tell your roll_no :- "))

        if not Persons.validate_email(email):
            print("invalid Email")
            return
        
        for i in data['students']:
            if i['roll_no'] == roll_no:
                print("student already exist")
                return
            
        data['students'].append({
            "name" : name,
            "age" : age,
            "email" : email,
            "roll_no": roll_no,
            "grades" : {}

        })

        save()
        print(f"Student {name} has registered!!")

    def show_details(self):
        pass

    def registered(self):
        pass 

class Teacher(Persons):

    def get_roles(self):
        return "student"
    
    def register(self):
        name = input("tell your name :- ")
        age = int(input("tell your age :- "))
        email = input("tell your email :- ")
        subject = input("tell your subject :- ")
        emp_id = int(input("tell your emp_id :- "))

        if not Persons.validate_email(email):
            print("invalid Email")
            return
        
        for i in data['teacher']:
            if i['emp_id'] == emp_id:
                print("student already exist")
                return
            

        data['teacher'].append({
            "name" : name,
            "age" : age,
            "email" : email,
            "subject" : subject,
            "emp_id": emp_id,
        })
        save()
        print(f"Teacher {name} has registered!!")

    def show_details(self):
        pass

    def registered(self):
        pass

    



stud = Student()
teache = Teacher()

print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add grade")
print("press 4 to show a student details")
print("press 5 to show a teacher details")

choice = int(input("please tell your your choice"))

if choice == 1:
    stud.register()
elif choice == 2:
    teache.register()
