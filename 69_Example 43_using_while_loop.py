def get_factorial(n):
    fact = 1
    i = 1
    while i <=n:
        fact = fact * i
        i = i + 1

    return fact

def main():
    print(f"3! = {get_factorial(3)}")
    print(f"5! = {get_factorial(5)}")

main()

"""
3! = 6
5! = 120

"""