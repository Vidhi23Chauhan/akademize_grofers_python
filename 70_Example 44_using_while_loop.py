def get_factorial(n):
    fact = 1
    i = n
    while i > 0:
        fact = fact * i
        i = i - 1

    return fact

def main():
    print(f"3! = {get_factorial(3)}")
    print(f"5! = {get_factorial(5)}")


main()

"""
3! = 6
5! = 120

"""