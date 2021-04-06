a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print(f"Max = {a}")
elif b > a and b > c:
    print(f"Max = {b}")
else:
    print(f"Max = {c}")
    

"""
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/15_max_of_3_numbers_logical_operators.py
Enter a: 1
Enter b: 2
Enter c: 3
Max = 3

"""