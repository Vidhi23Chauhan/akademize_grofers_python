def get_sum(n):
    s = 0
    i = 1
    while i <=n:
         s = s + i
         i = i + 1

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
