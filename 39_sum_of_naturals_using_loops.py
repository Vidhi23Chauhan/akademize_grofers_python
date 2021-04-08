def get_sum(n):
    s = 0
    for i in range(1, n+1):
         s = s + i

    return s

def main():
    n = int(input("Enter n: "))
    sum = get_sum(n)
    print(f"Sum of first {n} Natural numbers = {sum}")

main()

"""
Enter n: 5
Sum of first 5 Natural numbers = 15

"""
