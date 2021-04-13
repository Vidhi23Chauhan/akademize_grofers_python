def is_perfect(n):
    i = 1
    sum = 0
    while i < n:
        if n % i == 0:
            sum += i
        i += 1

    return n == sum


def main():
    print("Is Perfect number:")
    print(f"1 -> {is_perfect(1)}")
    print(f"2 -> {is_perfect(2)}")
    print(f"6 -> {is_perfect(6)}")
    print(f"28 -> {is_perfect(28)}")
    print(f"496 -> {is_perfect(496)}")
    print(f"548 -> {is_perfect(548)}")


main()

"""
Is Perfect number:
1 -> False
2 -> False
6 -> True
28 -> True
496 -> True
548 -> False

"""

"""
A perfect number is a positive integer that is equal to the sum of its positive divisors,
excluding the number itself.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Other perfect numbers are 28, 496, and 8,128.

"""