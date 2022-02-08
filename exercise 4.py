"""This code takes the student's name and score, then when the name 'X' is
input, the code will display the average score of all students, and the name
and score of the best performing student
Made by Daniel Fraser
7/02/2022"""

topname = []
avggrade = []
name = "daniel"
print("NOTE: to exit the code, enter a student with the name 'X' and a score "
      "of '0'")
while name != 'X':
    name = (input("What is the student's name? "()))
    grade = int(input("What is the student's grade? "))

    avggrade.insert(0, grade)
    topname.insert(0, name)

highestgrade = max(avggrade)

position = avggrade.index(highestgrade)
print(topname[position], "Got the highest grade!")

print("With a grade of", highestgrade)

avggrade = sum(avggrade)/len(avggrade)
print("The average grade is", avggrade)
