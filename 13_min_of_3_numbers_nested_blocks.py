a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b:
    if a < c:
        print(f"Min = {a}")
    else:
        print(f"Min = {c}")
else:
    if b < c:
        print(f"Max = {b}")
    else:
        print(f"Max = {c}")

"""
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/13_min_of_3_numbers_nested_blocks.py
Enter a: 1
Enter b: 2
Enter c: 3
Min = 1

"""