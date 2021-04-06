a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    if a > c:
        print(f"Max = {a}")
    else:
        print(f"Max = {c}")
else:
    if b > c:
        print(f"Max = {b}")
    else:
        print(f"Max = {c}")

"""
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/11_max_of_3_numbers_nested_blocks.py
Enter a: 3
Enter b: 6
Enter c: 9
Max = 9
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/11_max_of_3_numbers_nested_blocks.py
Enter a: 10
Enter b: 4
Enter c: 9
Max = 10
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/11_max_of_3_numbers_nested_blocks.py
Enter a: 3
Enter b: 9
Enter c: 5
"""