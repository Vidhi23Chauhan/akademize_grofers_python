def is_prime(n):
    start = 2
    stop = n-1

    i = start
    while(i <= stop):
        if n % i == 0:
            return False

        i += 1

    return True


def print_is_prime_status(n):
    if is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")


def main():
    print_is_prime_status(2)
    print_is_prime_status(3)
    print_is_prime_status(4)
    print_is_prime_status(5)
    print_is_prime_status(6)
    print_is_prime_status(11)
    print_is_prime_status(12)


main()

"""
2 is a prime number
3 is a prime number
4 is not a prime number
5 is a prime number
6 is not a prime number
11 is a prime number
12 is not a prime number

"""
