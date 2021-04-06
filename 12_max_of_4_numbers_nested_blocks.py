a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a > b:
    if a > c:
        if a > d:
            print(f"Max = {a}")
        else:
            print(f"Max = {d}")
    else: 
        if c > d:
            print(f"Max = {c}")
        else:
            print(f"Max = {d}")
        
else:
    if b > c:
        if b > d:
            print(f"Max = {b}")
        else:
            print(f"Max = {d}")
    else: 
        if c > d:
            print(f"Max = {c}")
        else:
            print(f"Max = {d}")

"""
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/12_max_of_4_numbers_nested_blocks.py
Enter a: 1
Enter b: 2
Enter c: 3
Enter d: 4
Max = 4
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/12_max_of_4_numbers_nested_blocks.py
Enter a: 2
Enter b: 3
Enter c: 4
Enter d: 1
Max = 4
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/12_max_of_4_numbers_nested_blocks.py
Enter a: 3
Enter b: 4
Enter c: 1
Enter d: 2
Max = 4
vidhichauhan@Admins-MacBook-Pro ~ % /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/vidhichauhan/Documents/akademize-grofers-python/12_max_of_4_numbers_nested_blocks.py
Enter a: 4
Enter b: 3
Enter c: 2
Enter d: 1
Max = 4

"""