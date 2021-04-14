names = ["Sravan", "Arun", "Varun"]
wishes = ["Good morning","Good evening","Good night"]

def name(n):
    for i in range(3):
        print(f"{wishes[i]} {names[n]}")
        i += 1


def main():
    for n in range(3):
        name(n)
        n += 1

main() 



"""
Good morning Sravan
Good evening Sravan
Good night Sravan
Good morning Arun
Good evening Arun
Good night Arun
Good morning Varun
Good evening Varun
Good night Varun

"""