# Run this once to automatically create the demo CSV file
import csv

demo_data = [
    ["salbeen", 85],
    ["roshan", 90],
    ["sarjak", 78],
    ["ganesh", 92],
    ["pradeep", 88],
    ["nirajan", 88],
    ["abishant", 88],
    ["subid", 88],
    ["ram", 88],
    ["syam", 88],
    ["hari", 88],
    ["raju", 88],
]

with open("student_marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in demo_data:
        writer.writerow(row)

print("Demo file 'student_marks.csv' created successfully!")