#Write a program that will read in the data for the data structure above, ie
#reads in a student’s name, then keeps reading in their modules and grades
#(until the user enters a blank module name),
#You can break this up into two parts:
#a. Just read in the module names until the user enters blank,
#b. Then read in the grade as well
#This program can just read in one student (and their module details)
import pprint
list = []
while True:
    student = {}
    student["Student Name"] = input("Enter student name: ")
    if student["Student Name"] == "":
        break
    student["Courses"] = {}
    while True:
        course = input("Enter course name: ")
        if course == "":
            break
        grade = input("Enter grade: ")
        student["Courses"][course] = grade
    list.append(student)

pprint.pprint(list)