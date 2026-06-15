# program to manage student records using a dictionary
student_records = {}

while True:
    # menu for users
    print("\n--- STUDENT RECORD MENU ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    # add student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        
        # check duplicate roll number
        if roll in student_records:
            print("Error: A student with this roll number already exists!")
        else:
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            contact = input("Enter Contact Number: ")
            
            # store the data in nested dictionary
            student_records[roll] = {
                "name": name,
                "marks": marks,
                "contact": contact
            }
            print("Student record added successfully!")
            
    # search the sutudent wih roll number
    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        
        if roll in student_records:
            student = student_records[roll]
            print("\n--- Student Found ---")
            print("Roll Number:", roll)
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Contact:", student["contact"])
        else:
            print("Student not found!")
            
    # display all student detail
    elif choice == "3":
        if len(student_records) == 0:
            print("No records found. The database is empty.")
        else:
            print("\n--- All Student Records ---")
            for roll, details in student_records.items():
                print("Roll: " + roll + " | Name: " + details["name"] + " | Marks: " + details["marks"] + " | Contact: " + details["contact"])
                
    # exit the program
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select a number between 1 and 4.")