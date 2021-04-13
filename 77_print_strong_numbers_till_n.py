def get_factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i

    return fact


def is_strong(n):
    i = n
    sum = 0
    while i > 0:
        rem = i % 10
        sum += get_factorial(rem)
        i //= 10

    return n == sum


def main():
    for i in range(1,1000):
        if is_strong(i):
            print(i)
        i = i + 1

main()

"""
1
2
145

"""