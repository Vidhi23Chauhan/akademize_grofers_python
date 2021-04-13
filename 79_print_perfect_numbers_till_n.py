def is_perfect(n):
    i = 1
    sum = 0
    while i < n:
        if n % i == 0:
            sum += i
        i += 1

    return n == sum


def main():
    for i in range(1,1000):
        if is_perfect(i):
            print(i)
        i = i + 1

main()

"""
6
28
496

"""