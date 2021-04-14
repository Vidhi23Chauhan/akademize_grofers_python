import sys
numbers = [2, 45, 76, 8, 33, 9, 6, 55]

sum = 0
product = 1
max = -sys.maxsize
min = sys.maxsize

for item in numbers:
    sum += item
    product *= item
    if item > max:
        max = item
    if item < min:
        min = item

avg = sum / len(numbers) # len is used to count the number of items


print(f"Sum of {numbers} = {sum}")
print(f"Sum of {numbers} = {product}")
print(f"Average = {avg}")
print(f"Max = {max}")
print(f"Min = {min}")

"""

Sum of [2, 45, 76, 8, 33, 9, 6, 55] = 234
Sum of [2, 45, 76, 8, 33, 9, 6, 55] = 5363107200
Average = 29.25
Max = 76
Min = 2

"""