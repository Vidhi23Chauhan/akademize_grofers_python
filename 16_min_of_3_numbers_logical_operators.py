a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b and a < c:
    print(f"Min = {a}")
elif b < a and b < c:
    print(f"Min = {b}")
else:
    print(f"Min = {c}")
    

"""
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/16_min_of_3_numbers_logical_operators.py
Enter a: 1
Enter b: 2
Enter c: 3
Min = 1

"""