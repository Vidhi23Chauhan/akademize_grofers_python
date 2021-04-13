def is_armstrong(n):
    i = n
    sum = 0
    while i > 0:
        rem = i % 10
        sum += rem*rem*rem
        i //= 10 # same as i = i // 10

    return n == sum


def main():
    for i in range(1,1000):
        if is_armstrong(i):
            print(i)
        i = i + 1


main()

"""
1
153
370
371
407

"""