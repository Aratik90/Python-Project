# ===== STUDENT MANAGEMENT SYSTEM =====

# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Exit

# Enter your choice:

import json

def save_student():

    with open("students.json", "w") as file:
        json.dump(Students, file, indent=4)

    print("Students saved successfully!")


def load_students():

    global Students

    try:
        with open("students.json", "r") as file:
            Students = json.load(file)

        print("Students Loaded Successfully!")

    except FileNotFoundError:
        Students = []


Students = []

def add_student():
    sid = int(input("Enter Student ID: "))

    if sid <= 0:
            print("Student ID must be Positive")

    for student in Students:
        if student['id'] == sid:
            print("Student ID already Exists!")
            return
        
    name = input("Enter Student Name: ")

    if not name.isalpha():
        print("Name should contain only Letters")
        return
    
    age = int(input("Enter Student Age: "))

    if age <1 or age > 100 :
        print("Age must be between 1 to 100")
        return
    
    course = input("Enter Course: ")

    marks = float(input("Enter Student Marks: "))

    if marks < 0 or marks > 100:
        print("Marks must be between 0 to 100 ")
        return
    


    student = {
    'id': sid,
    'name' : name,
    'age' : age,
    'course' : course,
    'marks' : marks
    }


    Students.append(student)
    save_student()
print("Student Added Successfully")


def view_students():
    if len(Students) ==0:
        print("No Student Records Found.")
        return 
    
    print("\nStudents Records")

    for student in Students:

        print("------------------------------")
        print("ID         :",student["id"])
        print("Name         :",student["name"])
        print("Age         :",student["age"])
        print("Course         :",student["course"])
        print("Marks         :",student["marks"])



def search_student():
    sid = int(input("Enter Student ID: "))

    for student in Students:
        if student["id"] == sid:

            print("Student Found")
            print(student)
            return
        
    print("Student Not Found")


def update_student():
    sid = int(input("Enter Student ID to Update: "))

    for student in Students:

        if student["id"] == sid:

            student["name"] = input("New Name: ")
            student["age"] = int(input("New Age: "))
            student["course"] = input("New Course: ")
            student["marks"] = float(input("New Marks: "))

            save_student()

            print("Record Updated Successfully")
            return
    print("Student Not Found")


def delete_student():
    sid = int(input("Enter Student ID to Delete: "))

    for student in Students:

        if student['id'] == sid:

            student.remove(student)
            save_student()

            print("Student Deleted Successfully")
            return
    print("Student Not Found")

def total_student():
    total = len(Students)

    print("Total student: ",total)

def average_marks():
    if len(Students) == 0:
        print("Record Not Found")
        return
    total = 0

    for student in Students:
        total += student['marks']
    average = total / len(Students)
    print("Average Marks : ",round(average,2))

def topper_student():
    if len(Students) == 0:
        print("Record not found ")
        return
    topper = Students[0]
    for student in Students:
        if student['marks'] > topper['marks']:
            topper = student
    print("\nTopper Student")
    print("-" * 30)
    print("ID     :", topper["id"])
    print("Name   :", topper["name"])
    print("Marks  :", topper["marks"])


def sort_by_marks():
    if len(Students) == 0:
        print("No student record found!")
        return
    sorted_student = sorted(Students,
                            key= lambda student: student["marks"],
                            reverse= True
                            )
    print("\nStudent Sorted by Marks")
    print("-" * 50)

    for student in sorted_student:
        print(
            student["id"],
            student["name"],
            student["age"],
            student["course"],
            student["marks"],
        )

def sort_by_name():
    if len(Students) == 0:
        print("No record found")
        return
    sort_student = sorted(Students,
                          key= lambda student : student["name"],
                          reverse= True
                          ) 
    
    print("\nStudent Sorted by Name")
    print("-" * 50)

    for student in sort_student:
        print(
            student["id"],
            student["name"],
            student["age"],
            student["course"],
            student["marks"],
        )

def search_by_name():
    if len(Students) == 0:
        print("No recor found! ")
        return
    name = input("Enter student Name")
    found = False
    
    for student in Students:
        if student["name"].lower() == name.lower():

            found = True

            print("\nStudent Found")
            print("-" * 30)
            print("ID      :", student["id"])
            print("Name    :", student["name"])
            print("Age     :", student["age"])
            print("Course  :", student["course"])
            print("Marks   :", student["marks"])

    if not found:
        print("Student Not Found!")




# Call all the funcation .

load_students()

while True:

    print("\n=========Student Management System=========")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Student")
    print("7. Average Marks")
    print("8. Topper student")
    print("9. Sort by Marks")
    print("10. Sort by name")
    print("11. Search by student name")
    print("12. Exist")
    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    
    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()
    
    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()
    
    elif choice == "6":
        total_student()

    elif choice == '7':
        average_marks()

    elif choice == "8":
        topper_student()

    elif choice == "9":
        sort_by_marks()
    
    elif choice == "10":
        sort_by_name()

    elif choice == "11":
        search_by_name()
    
    elif choice == "12":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
