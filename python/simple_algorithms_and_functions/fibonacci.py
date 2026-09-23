
#-------------------------------------------------------------------------------------
# Fibonacci sequence
# The Fibonacci sequence is a famous number pattern where each number is the sum of
# the two before it, starting with 0 and 1 giving 0, 1, 1, 2, 3, 5, 8, 13, and so on
#-------------------------------------------------------------------------------------

def fibonacci():
  x1,x2,x3,loop = 0,1,0,0
    
  print("0,1,", end="")

  while loop < 10:
     x3 = x1 + x2
     print(x3, end=",")
     x1 = x2
     x2 = x3
     loop += 1

fibonacci()
