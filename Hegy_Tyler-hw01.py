# Tyler Hegy
# UWYO COSC 1010
# Submission Date: 10/15/2024
# HW 01
# Lab Section: 12
# Sources, people worked with, help given to: Stack Overflow
# Comments:used stack overflow to find the sum function to sum the values in the scores dictionary

# Homework Question:
# 
# You are given a list of dictionaries where each dictionary represents a student and their scores 
# in different subjects.
# 
# Student Data:
students = [
     {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
     {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
     {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
     {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
 ]

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solution
averages={}

for student in students:
    name = student["name"]
    scores = student["scores"]

    average = sum(scores.values())/len(scores)
    averages[name] = average
print (averages)

good_students=[]
for name, value in averages.items():
    if value>80:
        good_students.append(name)
print(f"Students whose average score is greater than 80 : {good_students}")




