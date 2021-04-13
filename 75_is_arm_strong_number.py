def is_armstrong(n):
    i = n
    sum = 0
    while i > 0:
        rem = i % 10
        sum += rem*rem*rem
        i //= 10 # same as i = i // 10

    return n == sum


def main():
    print("Is Arm Strong number:")
    print(f"1 -> {is_armstrong(1)}")
    print(f"2 -> {is_armstrong(2)}")
    print(f"153 -> {is_armstrong(153)}")
    print(f"371 -> {is_armstrong(371)}")
    print(f"370 -> {is_armstrong(370)}")
    print(f"222 -> {is_armstrong(222)}")


main()

"""
Is Arm Strong number:
1 -> True
2 -> False
153 -> True
371 -> True
370 -> True
222 -> False

"""

"""
An Armstrong number is a number such that the sum ! of its digits
raised to the third power is equal to the number ! itself.
In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal 
to the number itself. For example: 153 = 1*1*1 + 5*5*5 + 3*3*3 // 153 is an Armstrong number.

"""