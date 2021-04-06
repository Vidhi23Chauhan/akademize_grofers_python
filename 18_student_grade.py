# Inputs
marks_1 = int(input("Enter marks1: "))
marks_2 = int(input("Enter marks2: "))
marks_3 = int(input("Enter marks3: "))

# Contant
THRESHOLD = 30

# Calculations
total = marks_1 + marks_2 + marks_3
avg = total / 3
status = "PASSED"

if marks_1 < THRESHOLD or marks_2 < THRESHOLD or marks_3 < THRESHOLD:
    status = "FAILED"

grade = "A"

if avg < 70 and avg >= 50:
    grade = "B"
else:
    grade = "C"

# Output
print("===================================")
print("-------- Report ---------")
print("Marks_1   :   " + str(marks_1))
print("Marks_2   :   " + str(marks_2))
print("Marks_3   :   " + str(marks_3))
print("Total     :   " + str(total))
print("Percentage:   " + str(avg))
print("Status    :   " + status)
print("Grade    :   " + grade)



"""
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/18_student_grade.py
Enter marks1: 90
Enter marks2: 90
Enter marks3: 50
===================================
-------- Report ---------
Marks_1   :   90
Marks_2   :   90
Marks_3   :   50
Total     :   230
Percentage:   76.66666666666667
Status    :   PASSED
Status    :   C
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/18_student_grade.py
Enter marks1: 50
Enter marks2: 30
Enter marks3: 80
===================================
-------- Report ---------
Marks_1   :   50
Marks_2   :   30
Marks_3   :   80
Total     :   160
Percentage:   53.333333333333336
Status    :   PASSED
Status    :   B
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/18_student_grade.py
Enter marks1: 20
Enter marks2: 90
Enter marks3: 90
===================================
-------- Report ---------
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/18_student_grade.py
Enter marks1: 20
Enter marks2: 90
Enter marks3: 90
===================================
-------- Report ---------
Marks_1   :   20
Marks_2   :   90
Marks_3   :   90
Total     :   200
Percentage:   66.66666666666667
Status    :   FAILED
Grade    :   B
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/18_student_grade.py
Enter marks1: 60
Enter marks2: 50
Enter marks3: 90
===================================
-------- Report ---------
Marks_1   :   60
Marks_2   :   50
Marks_3   :   90
Total     :   200
Percentage:   66.66666666666667
Status    :   PASSED
Grade    :   B
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/18_student_grade.py
Enter marks1: 20
Enter marks2: 30
Enter marks3: 40
===================================
-------- Report ---------
Marks_1   :   20
Marks_2   :   30
Marks_3   :   40
Total     :   90
Percentage:   30.0
Status    :   FAILED
Grade    :   C

"""
