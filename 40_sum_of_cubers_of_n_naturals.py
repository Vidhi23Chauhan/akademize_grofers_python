def get_sum(n):
    s = 0
    for i in range(1,n+1):
        s = s + i*i*i
       
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