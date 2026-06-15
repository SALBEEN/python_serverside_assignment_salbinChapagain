#  class to represent a Student
class Student:
    
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = 0.0

    def input_details(self):
        self.name = input("Enter Student Name: ")
        self.roll_number = input("Enter Roll Number: ")
        self.marks = float(input("Enter Marks: "))

    def display_details(self):
        print("\n--- Student Details ---")
        print("Name:        ", self.name)
        print("Roll Number: ", self.roll_number)
        print("Marks:       ", self.marks)
        
# creating obect from class student
student1 = Student()

# calling method 
student1.input_details()

# calling method
student1.display_details()