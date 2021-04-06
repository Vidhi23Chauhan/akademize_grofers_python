marks_1 = int(input("Enter marks1: "))
marks_2 = int(input("Enter marks2: "))
marks_3 = int(input("Enter marks3: "))

THRESHOLD = 30 #All Caps stands for constants

total = marks_1 + marks_2 + marks_3
avg = total / 3

if marks_1 >= THRESHOLD and marks_2 >= THRESHOLD and marks_3 >= THRESHOLD:
    status = "PASS"
else:
    status = "FAILED"

print("===================================")
print("-------- Report ---------")
print("Marks_1   :   " + str(marks_1))
print("Marks_2   :   " + str(marks_2))
print("Marks_3   :   " + str(marks_3))
print("Total     :   " + str(total))
print("Percentage:   " + str(avg))
print("Status    :   " + status)



"""
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/17_student_grade.py
Enter marks1: 20
Enter marks2: 50
Enter marks3: 80
===================================
-------- Report ---------
Marks_1   :   20
Marks_2   :   50
Marks_3   :   80
Total     :   150
Percentage:   50.0
Status      : FAILED
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/17_student_grade.py
Enter marks1: 50
Enter marks2: 60
Enter marks3: 70
===================================
-------- Report ---------
Marks_1   :   50
Marks_2   :   60
Marks_3   :   70
Total     :   180
Percentage:   60.0
Status      : PASS

"""