def print_si(p,n,r):
    si = (p*n*r) / 100
    print(f"Simpe Interest = {si}")

def main():
    p = int(input("Enter Principal: "))
    n = int(input("Enter Time Period of the Loan/Deposit in years: "))
    r = int(input("Enter Rate of Interest: "))
    print_si(p,n,r)


main()

"""
Enter Principal: 200000
Enter Time Period of the Loan/Deposit in years: 2
Enter Rate of Interest: 15
Simpe Interest = 60000.0

"""