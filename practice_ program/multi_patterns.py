#the revers triangle
row=5
for i in range(row):
    for j in range(row-i):
        print("*",end=" ")
    print()

"""" the output is in the form of
* * * * *
* * * *
* * * 
* *
* 
"""

for k in range(row+1):
    for l in range(row-k+1):
        print(" ",end=" ")
    # print()
    for m in range(k):
        print("*",end=" ")
    print()
"""       * 
        * * 
      * * * 
    * * * * 
  * * * * * 
  """
for k in range(row+1):
    for l in range(row-k+1):
        print(" ",end="")
    # print()
    for m in range(k):
        print("*",end=" ")
    print()

"""  * 
    * * 
   * * * 
  * * * * 
 * * * * * """

for i in range(row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
