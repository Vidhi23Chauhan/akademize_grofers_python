def foo():
    print("foo")

def bar():
    print("bar")

def main():
    print("Start of main")
    foo()
    bar()
    print("End of main")

# Start here
print("Hello functions")
main() # invoking the function main
foo()
bar()
print("Bye functions!")

"""
Hello functions
Start of main
foo
bar
End of main
foo
bar
Bye functions!

"""