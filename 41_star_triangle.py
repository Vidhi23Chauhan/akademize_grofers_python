def space(n):
    for i in range(n):
        print(" ",end = "")


def print_triangle(n):
    for i in range(n):
        print(f"+ ",end = "")
    print()




def main():
    for i in range(10):
        space(10-i)
        print_triangle(i+1)


main()

"""

         + 
        + + 
       + + + 
      + + + + 
     + + + + + 
    + + + + + + 
   + + + + + + + 
  + + + + + + + + 
 + + + + + + + + + 
+ + + + + + + + + + 

"""

