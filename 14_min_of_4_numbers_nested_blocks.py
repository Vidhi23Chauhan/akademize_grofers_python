a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a < b:
    if a < c:
        if a < d:
            print(f"Min = {a}")
        else:
            print(f"Min = {d}")
    else: 
        if c < d:
            print(f"Min = {c}")
        else:
            print(f"Min = {d}")
        
else:
    if b < c:
        if b < d:
            print(f"Min = {b}")
        else:
            print(f"Min = {d}")
    else: 
        if c < d:
            print(f"Min = {c}")
        else:
            print(f"Min = {d}")

"""
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/14_min_of_4_numbers_nested_blocks.py
Enter a: 1
Enter b: 2
Enter c: 3
Enter d: 4
Min = 1

"""