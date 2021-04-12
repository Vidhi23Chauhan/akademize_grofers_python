def get_factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i

    return fact

def main():
    print(f"3! = {get_factorial(3)}")
    print(f"5! = {get_factorial(5)}")


main()

"""
3! = 6
5! = 120

"""