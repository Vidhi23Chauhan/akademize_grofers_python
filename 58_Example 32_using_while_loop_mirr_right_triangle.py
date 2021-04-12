"""
def space(n):
    for i in range(n):
        print(" ",end = "")


def print_triangle(n):
    for i in range(n):
        print(f"+ ",end = "")
    print()




def main():
    for i in range(10):
        space(20-i*2)
        print_triangle(i+1)


main()
"""

i = 1
while i<=10:
  j = 10
  while j >=i:
      print( "  " , end="")
      j= j-1
  k = 1  
  while k <= i:  
      print( "*" , end=" ")  
      k = k + 1
  print()
  i= i+1

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

