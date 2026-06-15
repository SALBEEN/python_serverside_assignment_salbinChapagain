import csv

total_marks = 0
count = 0


with open("demo/student_marks.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        marks = float(row[1])
        total_marks = total_marks + marks
        count = count + 1

# caalculate and print the average
if count > 0:
    average = total_marks / count
    print("Average marks ---->> :", average)
else:
    print("The file was empty.")