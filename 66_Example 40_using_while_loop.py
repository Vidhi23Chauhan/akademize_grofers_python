def get_sum(n):
    s = 0
    i = 1
    while i <=n:
        s = s + i*i*i
        i = i + 1
    return s

def main():
    n = int(input("Enter n:"))
    sum = get_sum(n)
    print(f"Sum of cube of {n} Natural numbers = {sum}")

main()


"""
Enter n:3
Sum of cube of 3 Natural numbers = 36

"""